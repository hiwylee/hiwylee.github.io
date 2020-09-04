## Exadata 관련 유틸리티 SQL
### Bundle Patch
```sql

  1* select patch_id,action_time,description from dba_registry_sqlpatch
SQL> /
  PATCH_ID ACTION_TIME                                                                 DESCRIPTION
---------- --------------------------------------------------------------------------- ------------------------------------------------------------------------------------------
  30805684 31-AUG-20 10.50.52.822540 AM                                                OJVM RELEASE UPDATE: 19.7.0.0.200414 (30805684)
  30869156 31-AUG-20 10.50.52.816766 AM                                                Database Release Update : 19.7.0.0.200414 (30869156)

2 rows selected.

```

* CRS 자원의 확인
```bash
<GRID_HOME>/bin/crsctl stat res -t
--------------------------------------------------------------------------------
NAME           TARGET  STATE        SERVER                   STATE_DETAILS       
--------------------------------------------------------------------------------
Cluster Resources
--------------------------------------------------------------------------------
ora.LISTENER_SCAN1.lsnr
      1        ONLINE  ONLINE       d02-0c                                       
ora.LISTENER_SCAN2.lsnr
      1        ONLINE  ONLINE       d02-0b                                       
ora.LISTENER_SCAN3.lsnr
      1        ONLINE  ONLINE       d02-0b                                       
ora.d02-0b.vip
      1        ONLINE  ONLINE       d02-0b                                       
ora.d02-0c.vip
      1        ONLINE  ONLINE       d02-0c                                       
ora.rac112.db
      1        ONLINE  ONLINE       d02-0b                                   
      2        ONLINE  ONLINE       d02-0c                                  
ora.scan1.vip
      1        ONLINE  ONLINE       d02-0c                                       
ora.scan2.vip
      1        ONLINE  ONLINE       d02-0b                                       
ora.scan3.vip
      1        ONLINE  ONLINE       d02-0b
```

```bash
$ <GRID_HOME>/bin/crsctl stat res -t
--------------------------------------------------------------------------------
NAME           TARGET  STATE        SERVER                   STATE_DETAILS       
--------------------------------------------------------------------------------
Local Resources
--------------------------------------------------------------------------------
ora.DATA.dg
               ONLINE  ONLINE       d02-0b                                       
               ONLINE  ONLINE       d02-0c                                       
ora.RECO.dg
               ONLINE  ONLINE       d02-0b                                       
               ONLINE  ONLINE       d02-0c                               
ora.LISTENER.lsnr
               ONLINE  ONLINE       d02-0b                                       
               ONLINE  ONLINE       d02-0c                            
ora.asm
               ONLINE  ONLINE       d02-0b                              
               ONLINE  ONLINE       d02-0c                             
ora.net1.network
               ONLINE  ONLINE       d02-0b                                       
               ONLINE  ONLINE       d02-0c                                                                              

```
### smart Scan
* 
```sql
orcl_high> select n.name,s.value from v$mystat s, v$statname n where n.statistic#=s.statistic# and n.name like '%cell flash cache read%';
NAME                                                                    VALUE
------------------------------------------------------------ ----------------
cell flash cache read hits                                              17229
cell flash cache read hits for controlfile reads                            0
cell flash cache read hits for smart IO                                 17159
orcl_high> select n.name,s.value from v$mystat s, v$statname n where n.statistic#=s.statistic# and n.name like '%physical%optimized%';
NAME                                                                    VALUE
------------------------------------------------------------ ----------------
physical read requests optimized                                        17229
physical read total bytes optimized                               17963958272
...
orcl_high> select n.name,s.value from v$mystat s, v$statname n where n.statistic#=s.statistic# and n.name like '%smart scan%';
NAME                                                                    VALUE
------------------------------------------------------------ ----------------
cell physical IO interconnect bytes returned by smart scan           18662816
...
```
* Cell Disk Usable size 및 Mirroring 
```sql
select  name,
total_mb Total_r,
free_mb free_r,
required_mirror_free_mb req_fee_r,
case name when 'DATA_KRX2A' then  (total_mb-required_mirror_free_mb)/3
else (total_mb-required_mirror_free_mb)/2  end recom_use,
USABLE_FILE_MB  recom_free,
case name when 'DATA_KRX2A' then  total_mb/3
else total_mb/2  end tot_use,
case name when 'DATA_KRX2A' then  free_mb/3
else free_mb/2  end free_use,
case name when 'DATA_KRX2A' then  ((total_mb-free_mb)/3)
else ((total_mb-free_mb)/2) end used
from    v$asm_diskgroup
/

```
* SMART SCAN여부 점검
```sql
set pagesize 999
set lines 190
col sql_text format a70 trunc
col child format 99999
col execs format 9,999
col avg_etime format 99,999.99
col "IO_SAVED_%" format 999.99
col avg_px format 999
col offload for a7

select sql_id, child_number child, plan_hash_value plan_hash, executions execs,
(elapsed_time/1000000)/decode(nvl(executions,0),0,1,executions)/
decode(px_servers_executions,0,1,px_servers_executions/decode(nvl(executions,0),0,1,executions)) avg_etime,
px_servers_executions/decode(nvl(executions,0),0,1,executions) avg_px,
decode(IO_CELL_OFFLOAD_ELIGIBLE_BYTES,0,'No','Yes') Offload,
decode(IO_CELL_OFFLOAD_ELIGIBLE_BYTES,0,0,100*(IO_CELL_OFFLOAD_ELIGIBLE_BYTES-IO_INTERCONNECT_BYTES)
/decode(IO_CELL_OFFLOAD_ELIGIBLE_BYTES,0,1,IO_CELL_OFFLOAD_ELIGIBLE_BYTES)) "IO_SAVED_%",
sql_text
from v$sql s
where upper(sql_text) like upper(nvl('&sql_text',sql_text))
and sql_text not like 'BEGIN :sql_text := %'
and sql_text not like '%IO_CELL_OFFLOAD_ELIGIBLE_BYTES%'
and sql_id like nvl('&sql_id',sql_id)
order by 1, 2, 3
/
```

```sql
SQL> alter session set cell_offload_processing=true;
SQL> select /*+ parallel(s_on, 2) */ count(*) from sales where amount_sold >= 1500;

SQL> alter session set cell_offload_processing=false;
SQL> select /*+ parallel(s_off, 2) */ count(*) from sales where amount_sold >= 1500;
SQL> select substr(SQL_TEXT, 20, 10) SQL_TEXT, IO_INTERCONNECT_BYTES, PHYSICAL_READ_BYTES,
round(IO_INTERCONNECT_BYTES/PHYSICAL_READ_BYTES*100, 2) "TRANS(%)"
from v$sql where sql_text like 'select /*+ parallel(s_%';

```
|SQL_TEXT |  IO_INTERCONNECT_BYTES |PHYSICAL_READ_BYTES|  TRANS(%)|
|---|----:|----:|----:|
|Smart ON|230976|13262848|1.74|
|Smart OFF|13262848|13262848|100.00|


* Hint
  * cell_offload_plan_display : (auto | always | never)
    * always : Non-Exadata 환경에서 Exadata Assessment를 위해 활용 가능
    * never  : Exadata 환경에서 Non-Exadata 환경의 (original) 실행 계획과의  비교를 위해 활용 가능
  * _Storage Index disabling: _kcfis_storageidx_disabled = false | true

* Wait Event
  * cell smart table scan
  * cell smart index scan
  * cell single block physical read
  * cell list of blocks physical read
  * cell multiblock physical read

* Smart Scan 제어를 위한 기본 방법
  * CELL_OFFLOAD_PROCESSING = TRUE | FALSE
    * alter system / alter session / opt_param 힌트

  * ASM Disk Group 속성 cell.smart_scan_capable = true | false
    * alter diskgroup … set attribute
 
### EHCC
* EHCC를 통한 공간 절감 예측 방법
```sql
dbms_compression.get_compression_ratio(
    scratchtbsname => '&&tbs',
    ownname => '&&owner’,
    tabname => '&&tab’,
    partname => null,
    comptype => dbms_compression.comp_for_query_low,
    blkcnt_cmp => l_blkcnt_cmp,
    blkcnt_uncmp => l_blkcnt_uncmp,
    row_cmp => l_row_cmp,			
    row_uncmp => l_row_uncmp,
    cmp_ratio => l_cmp_ratio,		
    comptype_str => l_comptype_str
);
```
* 압축 여부 확인 방법
```sql
Select dbms_compression.get_compression_type(‘&OWNER',‘&TAB‘, rowid) 
from &TAB;
```
* EHCC 압축은 Direct Path Insert / Loading에 의해서만 수행
  * Decompression은 어디에서 일어나는가
    * Smart Scan이 수행된다면 Cell에서 : 
      * _cell_offload_hybridcolumnar = ``true`` | false
      * cell IO uncompressed bytes > 0 (v$sysstat)

    * Smart Scan이 수행되지 않는다면 DB 서버에서
      * 전체 CU가 압축된 상태에서 버퍼 캐시로 전송됨
      * cell IO uncompressed bytes > 0 (v$sysstat)
* Query Mode
```sql
CREATE TABLE … COMPRESS FOR QUERY LOW
CREATE TABLE … COMPRESS FOR QUERY HIGH
CREATE TABLE … COMPRESS FOR ARCHIVE LOW
CREATE TABLE … COMPRESS FOR ARCHIVE HIGH
```
* COmpression 변경 방법
  * 테이블 전체의 정의만 변경하는 경우
```sql
    alter table ORDERS compress for query high;
```  
  * 테이블 전체의 정의와 데이터까지 변경하는 경우
```sql
     alter table ORDERS move compress for query high parallel 32;
```  
### Smart Flash Cache
* 네가지 활용 방법
  * Smart Flash Cache
  * Smart Flash Logging
  * Smart Write-Back Cache
  * Exadata Flash Cache 압축 
* 압축 명령어
```sql
   alter cell flashCompression=TRUE
```
* Cache 현황의 확인 방법
```sql
CellCLI> list flashcachecontent
…
    cachedKeepSize:    	 0
    cachedSize:        	 598016
    dbID:              	 2825298339
    dbUniqueName:      	 KRX3BA
    hitCount:          	 0
    missCount:         	 291
    objectNumber:      	 4294967294  -- dba_ojbects.data_object_id
    tableSpaceNumber:  	 1

CellCLI>

```
  * CELL_FLASH_CACHE = KEEP
* 성능 효과 확인 방법
  * “physical read total bytes optimized / physical read total bytes”

### IORM 
* Exadata 위에 단일 데이터베이스 : 
  * Intradatabase: by Consumer Group
  * DB 단 설정 (DBMS_RESOURCE_MANAGER)
* 복수의 데이터베이스들을 운영   : 
  * Interdatabase: by Database : Cell 단 설정 (IORMPLAN)
  * Category: by Category
    * Category by Consumer Group
* IORM objective 설정
  * basic | low_latency | high_throughput | balanced | auto
* IORM 모니터링 방법
  * Tool for Gathering I/O Resource Manager Metrics: metric_iorm.pl [ID 1337265.1]
* IORM의 자원 분배 알고리즘
  * ① catPlan
  * ② dbPlan
  * ③ DBRM Plan
  * 최종 할당
###  기타 성능 관련 Topic들
* DOP의 수동 지정
  * Default DOP = parallel_threads_per_cpu x cpu_count x instance_count
  * alter session force parallel query | dml | ddl parallel N;
  * parallel 힌트
  * Database Resource Manager
* Inter-Node Parallelism
  * Local DB 서버만을 사용  parallel_force_local = true | false
* 병렬 DML 관련 고려 사항
  * 세션에 병렬 DML 모드를 설정해야 함
    * alter session enable parallel dml;
  * SQL 변환
    * Direct Path, Nologging 방식의 Insert가 최상의 성능 
* 병렬 처리의 모니터링 :     Real-Time SQL Monitoring vs v$pq_tqstat
* Partition Granule 사용 시 DOP는 Partition 개수로 제한
* 병렬 조인과 데이터 재분배
  * Parallel Join
  * PQ_DISTRIBUTE 힌트
* Exadata 시스템 통계
  * execute dbms_stats.gather_system_stats('EXADATA');
  * execute DBMS_STATS.GATHER_FIXED_OBJECTS_STATS;    -- X$...
* ``HugePage 설정``
  * HugePage 설정의 필요성
    * HugePage는 swap되지 않음
    * Page Table 사이즈 축소
    * TLB(Translation Lookaside Buffer) Hit 증가, Page Walk 감소
  * 설정 방법
    * Shell Script to Calculate Values Recommended Linux HugePages / HugeTLB Configuration ``[ID 401749.1]``
    *  USE_LARGE_PAGES = TRUE | ONLY | FALSE | AUTO
### Automatic Storage Management
* ASM 데이터 보호 수준
  * Normal Redundancy: 2 개의 Cell에 걸쳐 “Double Mirroring” : 1 개 Cell의 장애까지 커버
  * High Redundancy: 3 개의 Cell에 걸쳐 “Triple Mirroring”   : 2 개 Cell의 장애까지 커버
* Rebalancing Power
  * ``alter diskgroup data_dg rebalance power 16;``
  * 0 ~ asm_power_limit (최대 값 1,024) / Default 4
  * 모니터링 : ``V$ASM_OPERATION``
* Fast Mirror Resync
  * ``alter diskgroup data_dg set attribute 'disk_repair_time'='7.2h‘;`` 
  * ASM은 offline 상태가 된 디스크를 영구히 drop하기 전에 disk_repair_time으로 명시된 시간 동안 대기
    * ASM이 자동으로 Rebalance를 수행하기 전까지의 대기 시간을 의미
  * 문제의 디스크가 다시 Online 상태가 되면 ASM은 오직 변경이 가해진 Extent에 대해서만 Rebalance를 수행
    * 따라서 두 번째 Rebalance 작업을 훨씬 더 빠르게 마칠 수 있도록 함
  * Default 3.6 시간
### Backup & Recovery
* Base Tool은 RMAN
  * ASM 환경에서 유일한 방안
* Output 파일 공간 할당량 조절
  * _file_size_increase_increment=2143289344
* Exadata 백업 권고 사항
  * RMAN Recovery Catalog 이용
    * Repository DB는 별도의 서버에 구성
  * Backup 용 데이터베이스 서비스 이용
  * 운영 영향도 최소화
    * DBRM / IORM을 이용 
    * ADG를 이용하여 Standby DB에 백업 작업을 Offload

### Exadata 모니터링 / 진단 / 유지 보수 관련 Tool

* OSWatcher Black Box (Includes: [Video]) [ID 301137.1]
  * OS 레벨의 모니터링 도구
    *vmstat, netstat, iostat, etc.
  *두 가지 구성 요소
    * oswbb: 데이터 수집 & 저장을 위한 shell scripts
    * oswbba: Graphical한 분석을 위한 java utility

* sar.sh
  * sar 등의 OS 명령
  * CellCli list metriccurrent
  * Oracle Wait Interface 조회
* Exachk.sh
  * Exadata 진단 및 Health Check을 위한 Tool
  * Oracle Exadata Database Machine exachk or HealthCheck [ID 1070954.1]
* Exa_Health_Check
  * 간소화된 Health Check
* ADR (arcli)
  * Trace, Dump, Log 등 “진단 데이터”를 위한 파일 기반 통합 Repository
  * Exadata DB 서버 및 Cell 서버 모두
```sql
adrci> show alert

Choose the alert log from the following homes to view:

1: diag/clients/user_oracle/host_3824420761_80
2: diag/tnslsnr/krx3b01/krx3b-scan
3: diag/tnslsnr/krx3b01/listener_scan1
4: diag/tnslsnr/krx3b01/listener
5: diag/asm/+asm/+ASM1
6: diag/asm/user_oracle/host_3824420761_80
7: diag/diagtool/user_oracle/host_3824420761_11
8: diag/rdbms/krx3ba/krx3ba1
9: diag/rdbms/add1/ADD11
10: diag/asmtool/user_oracle/host_3824420761_80
Q: to quit

Please select option: 8
Output the results to file: /tmp/alert_6617_13992_krx3ba1_1.ado

2013-04-09 17:17:01.197000 +09:00
Starting ORACLE instance (normal)
****************** Large Pages Information *****************

Total Shared Global Region in Large Pages = 16 GB (100%)

Large Pages used by this instance: 8193 (16 GB)
…

```
* DiagTools
  * Exadata Storage Server Diagnostic Collection Guide [ID 735323.1]
  * DbmCheck.sh : Cell 관련 구성 정보
  * diagget.sh  : DB 서버 관련 구성 정보, 각종 Oracle S/W 로그
* OPLAN
  * Oracle Software Patching with OPLAN [ID 1306814.1]
  * Patch 작업을 도와 주는 Tool
    * Patch Apply 및 Rollback에 대한 step-by-step 가이드 제공

 




