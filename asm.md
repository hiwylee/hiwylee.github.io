## ASM - study
* Automatic Storage Manager (ASM) Enhancements in Oracle Database 11g Release 1 
  * https://oracle-base.com/articles/11g/asm-enhancements-11gr1
* Basic  from https://hayleyfish.tistory.com/
  * [ASM](https://hayleyfish.tistory.com/113?category=540223)
  * [ASM 관리](https://hayleyfish.tistory.com/114_)
  * [ASM 기반에서는 RMAN으로 복구](https://hayleyfish.tistory.com/115?category=540223)
  
### DBCS ASM
* ASM DIskgroup 사용량 

```sql
SQL> ed free_dg.sql

col gname form a15
col dbname form a15
col file_type form a14

SELECT
    gname,
    dbname,
    file_type,
    round(SUM(space)/1024/1024) mb,
    round(SUM(space)/1024/1024/1024) gb,
    COUNT(*) "#FILES"
FROM
    (
        SELECT
            gname,
            regexp_substr(full_alias_path, '[[:alnum:]_]*',1,4) dbname,
            file_type,
            space,
            aname,
            system_created,
            alias_directory
        FROM
            (
                SELECT
                    concat('+'||gname, sys_connect_by_path(aname, '/')) full_alias_path,
                    system_created,
                    alias_directory,
                    file_type,
                    space,
                    level,
                    gname,
                    aname
                FROM
                    (
                        SELECT
                            b.name            gname,
                            a.parent_index    pindex,
                            a.name            aname,
                            a.reference_index rindex ,
                            a.system_created,
                            a.alias_directory,
                            c.type file_type,
                            c.space
                        FROM
                            v$asm_alias a,
                            v$asm_diskgroup b,
                            v$asm_file c
                        WHERE
                            a.group_number = b.group_number
                        AND a.group_number = c.group_number(+)
                        AND a.file_number = c.file_number(+)
                        AND a.file_incarnation = c.incarnation(+) ) START WITH (mod(pindex, power(2, 24))) = 0
                AND rindex IN
                    (
                        SELECT
                            a.reference_index
                        FROM
                            v$asm_alias a,
                            v$asm_diskgroup b
                        WHERE
                            a.group_number = b.group_number
                        AND (
                                mod(a.parent_index, power(2, 24))) = 0
--                            and a.name like '&&db_name'
                    ) CONNECT BY prior rindex = pindex )
        WHERE
            NOT file_type IS NULL
            and system_created = 'Y' )
WHERE 1=1
--    and dbname like '&db_name'
GROUP BY
    gname,
    dbname,
    file_type
ORDER BY
    gname,
    dbname,
    file_type
/
SQL> @free
old  60: --                            and a.name like '&&db_name'
new  60: --                            and a.name like 'DB0902'
old  66: --    and dbname like '&db_name'
new  66: --    and dbname like 'DB0902'

GNAME           DBNAME          FILE_TYPE              MB         GB     #FILES
--------------- --------------- -------------- ---------- ---------- ----------
DATA            DB0902_YNY19M   CHANGETRACKING         12          0          1
DATA            DB0902_YNY19M   DATAFILE             4852          5         13
DATA            DB0902_YNY19M   PARAMETERFILE           4          0          1
DATA            DB0902_YNY19M   PASSWORD                0          0          1
DATA            DB0902_YNY19M   TEMPFILE              132          0          3
RECO            DB0902_YNY19M   ARCHIVELOG          37232         36         55
RECO            DB0902_YNY19M   AUTOBACKUP             20          0          1
RECO            DB0902_YNY19M   CONTROLFILE            96          0          3
RECO            DB0902_YNY19M   ONLINELOG            4128          4          4

9 rows selected.
SQL> SELECT name, free_mb, total_mb, free_mb/total_mb*100 as percentage
     FROM v$asm_diskgroup;  2

NAME                              FREE_MB   TOTAL_MB PERCENTAGE
------------------------------ ---------- ---------- ----------
DATA                              1038048    1048576 98.9959717
RECO                               220528     262144 84.1247559

```
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
