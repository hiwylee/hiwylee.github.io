## 대용량 처리
### 주요 파라미터* _parallel

```
NAME                                               VALUE
-------------------------------------------------- ------------------------------
_parallel_syspls_obey_force                        false
_parallel_broadcast_enabled                        false
_parallel_load_balancing                           falsesho

_optimizer_group_by_placement                      false       >> group by 
_px_groupby_pushdown                               off         >>

parallel_execution_message_size                    16384

-- pq slave 가 사용가능한 최대 메모리
_pga_max_size                                      2097152  

-- 한 퀴리가 사용할 수 있는  최대 작업 메모리 (pga의 1/2) ;  
_smm_px_max_size                                   50331648
_smm_px_max_size_static                            50331648

parallel_min_servers                               960


pga_aggregate_limit                                192G
pga_aggregate_target                                96G

```

```
MemTotal:       30615520 kB
MemFree:         1691076 kB
MemAvailable:   12384580 kB
Buffers:          377572 kB
Cached:         11184380 kB
SwapCached:         5528 kB
Active:         11390696 kB
Inactive:        5182164 kB
Active(anon):    6409480 kB
Inactive(anon):  1170732 kB
Active(file):    4981216 kB
Inactive(file):  4011432 kB
Unevictable:      623168 kB
Mlocked:          623168 kB
SwapTotal:      16777212 kB
SwapFree:       16181004 kB
Dirty:              1116 kB
Writeback:             0 kB
AnonPages:       5642952 kB
Mapped:           714752 kB
Shmem:           2413740 kB
Slab:            3898400 kB
SReclaimable:    3666888 kB
SUnreclaim:       231512 kB
KernelStack:       18816 kB
PageTables:       132428 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    28368876 kB
Committed_AS:   10245072 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      139660 kB
VmallocChunk:   34359531028 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
CmaTotal:              0 kB
CmaFree:               0 kB
HugePages_Total:    3629
HugePages_Free:      174
HugePages_Rsvd:        3
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:     2835216 kB
DirectMap2M:    22327296 kB
DirectMap1G:     8388608 kB

```


```
SYS@DB09021> show sga

Total System Global Area 7247754448 bytes
Fixed Size                  9151696 bytes
Variable Size            4445962240 bytes
Database Buffers         2768240640 bytes
Redo Buffers               24399872 bytes

SYS@DB09021> select * from v$pgastat;

NAME                                                          VALUE UNIT                         CON_ID
-------------------------------------------------- ---------------- ------------------------ ----------
aggregate PGA target parameter                     7,247,757,312    bytes                             0
aggregate PGA auto target                          5,425,007,616    bytes                             0
global memory bound                                724,766,720      bytes                             0
total PGA inuse                                    1,219,972,096    bytes                             0
total PGA allocated                                2,912,138,240    bytes                             0
maximum PGA allocated                              4,339,356,672    bytes                             0
total freeable PGA memory                          1,618,214,912    bytes                             0
MGA allocated (under PGA)                          268,435,456      bytes                             0
maximum MGA allocated                              268,435,456      bytes                             0
process count                                      108                                                0
max processes count                                122                                                0
PGA memory freed back to OS                        274,773,966,848  bytes                             0
total PGA used for auto workareas                  0                bytes                             0
maximum PGA used for auto workareas                410,598,400      bytes                             0
total PGA used for manual workareas                0                bytes                             0
maximum PGA used for manual workareas              40,321,024       bytes                             0
over allocation count                              0                                                  0
bytes processed                                    555,613,489,152  bytes                             0
extra bytes read/written                           0                bytes                             0
cache hit percentage                               100              percent                           0
recompute count (total)                            4,590,932                                          0

21 rows selected.


```
```
COLUMN username FORMAT A30
COLUMN osuser FORMAT A20
SYS@DB09021> SYS@DB09021> SYS@DB09021> COLUMN spid FORMAT A10
COLUMN service_name FORMAT A15
SYS@DB09021> SYS@DB09021> COLUMN module FORMAT A45
COLUMN machine FORMAT A30
COLUMN logon_time FORMAT A20
COLUMN pga_used_mem_mb FORMAT 99990.00
COLUMN pga_alloc_mem_mb FORMAT 99990.00
COLUMN pga_freeable_mem_mb FORMAT 99990.00
COLUMN pga_max_mem_mb FORMAT 99990.00

SELECT NVL(s.username, '(oracle)') AS username,
       s.osuser,
       s.sid,
       s.serial#,
       p.spid,
       ROUND(p.pga_used_mem/1024/1024,2) AS pga_used_mem_mb,
SYS@DB09021> SYS@DB09021> SYS@DB09021> SYS@DB09021> SYS@DB09021> SYS@DB09021> SYS@DB09021> SYS@DB09021>   2    3    4    5    6    7         ROUND(p.pg                                  a_alloc_mem/1024/1024,2) AS pga_alloc_mem_mb,
       ROUND(p.pga_freeable_mem/1024/1024,2) AS pga_freeable_mem_mb,
       ROUND(p.pga_max_mem/1024/1024,2) AS pga_max_mem_mb,
       s.lockwait,
       s.status,
       s.service_name,
       s.module,
       s.machine,
       s.program,
       TO_CHAR(s.logon_Time,'DD-MON-YYYY HH24:MI:SS') AS logon_time,
       s.last_call_et AS last_call_et_secs
FROM   v$session s,
       v$process p
WHERE  s.paddr = p.addr
ORDER BY s.username, s.osuser;
```

* [Oracle Database - Handy Scripts PGA and Temp](http://o-dba.blogspot.com/2017/01/oracle-database-handy-scripts-pga-and.html)
