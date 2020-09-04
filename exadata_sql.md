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
SQL> alter session set cell_offload_processing=true;
SQL> select /*+ parallel(s_on, 2) */ count(*) from sales where amount_sold >= 1500;

SQL> alter session set cell_offload_processing=false;
SQL> select /*+ parallel(s_off, 2) */ count(*) from sales where amount_sold >= 1500;
SQL> select substr(SQL_TEXT, 20, 10) SQL_TEXT, IO_INTERCONNECT_BYTES, PHYSICAL_READ_BYTES,
round(IO_INTERCONNECT_BYTES/PHYSICAL_READ_BYTES*100, 2) "TRANS(%)"
from v$sql where sql_text like 'select /*+ parallel(s_%';

```
