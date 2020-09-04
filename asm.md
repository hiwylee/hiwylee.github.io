## ASM - study
* Automatic Storage Manager (ASM) Enhancements in Oracle Database 11g Release 1 
  * https://oracle-base.com/articles/11g/asm-enhancements-11gr1
* Basic  from https://hayleyfish.tistory.com/
  * [ASM](https://hayleyfish.tistory.com/113?category=540223)
  * [ASM 관리](https://hayleyfish.tistory.com/114_)
  * [ASM 기반에서는 RMAN으로 복구](https://hayleyfish.tistory.com/115?category=540223)
  
### DBCS ASM
* ASM VIEWS

| VIEW | 설명 | 
|---|---|
| V$ASM_DISKGROUP| 디스크 그룹에 관련된 정보|
| V$ASM_DISK|디스크에 대한 정보|
| V$ASM_FILE|ASM 내부에 생성된 파일에 대한 정보|
| V$ASM_TEMPLATE|ASM 내 모든 디스크 그룹에 설정된 템플릿 정보|
| V$ASM_ALIAS| ASM 디스크 그룹의 ALIAS 정보|
| V$ASM_OPERATION| ASM 인스턴스상에서 실행되는 작업들 현황 정보|
| V$ASM_CLIENT|ASM을 사용하는 DB 인스턴스 현황|

```bash
[opc@orcl ~]$ sudo su - grid
Last login: Fri Sep  4 14:20:15 UTC 2020 on pts/0
[grid@orcl ~]$ asmcmd
ASMCMD> lsdg
State    Type    Rebal  Sector  Logical_Sector  Block       AU  Total_MB  Free_MB  Req_mir_free_MB  Usable_file_MB  Offline_disks  Voting_files  Name
MOUNTED  EXTERN  N         512             512   4096  4194304   1048576  1009856                0         1009856              0             Y  DATA/
MOUNTED  EXTERN  N         512             512   4096  4194304    262144   219000                0          219000              0             N  RECO/
ASMCMD>
```
```sql
SQL>
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

NAME                              TOTAL_R     FREE_R  REQ_FEE_R  RECOM_USE RECOM_FREE    TOT_USE   FREE_USE       USED
------------------------------ ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
DATA                              1048576    1009856          0     524288    1009856     524288     504928      19360
RECO                               262144     219000          0     131072     219000     131072     109500      21572

SQL>
SQL>  SELECT group_number, disk_number, name, mount_status, path, total_mb
    FROM v$asm_disk
SQL> /

GROUP_NUMBER DISK_NUMBER NAME                           MOUNT_S PATH                             TOTAL_MB
------------ ----------- ------------------------------ ------- ------------------------------ ----------
           2           0 RECODISK1                      CACHED  /dev/RECODISK1                      65536
           2           1 RECODISK2                      CACHED  /dev/RECODISK2                      65536
           2           2 RECODISK3                      CACHED  /dev/RECODISK3                      65536
           1           2 DATA_0002                      CACHED  /dev/DATADISK1                     262144
           1           1 DATA_0001                      CACHED  /dev/DATADISK2                     262144
           1           0 DATA_0000                      CACHED  /dev/DATADISK3                     262144
           1           3 DATA_0003                      CACHED  /dev/DATADISK4                     262144
           2           3 RECODISK4                      CACHED  /dev/RECODISK4                      65536


```
