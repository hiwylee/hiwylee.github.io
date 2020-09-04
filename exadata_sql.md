## Exadata 관련 유틸리티 SQL
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






