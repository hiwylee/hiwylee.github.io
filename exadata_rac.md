## RAC
* 
* grid process 그조 (from http://haisins.epac.to/wordpress/?p=3854)
  * ![](http://haisins.epac.to/wordpress/wp-content/uploads/2018/04/042318_0432_Oracle12cDB2.png)
## Info

```bash
[oracle@rac1 ~]$ srvctl config database -v
DB0902_yny19m   /u01/app/oracle/product/19.0.0.0/dbhome_1       19.0.0.0.0
[oracle@rac1 ~]$ srvctl config database -d DB0902_yny19m
Database unique name: DB0902_yny19m
Database name: DB0902
Oracle home: /u01/app/oracle/product/19.0.0.0/dbhome_1
Oracle user: oracle
Spfile: +DATA/DB0902_YNY19M/PARAMETERFILE/spfile.269.1050064405
Password file: +DATA/DB0902_YNY19M/PASSWORD/pwddb0902_yny19m.259.1050063751
Domain: subnet1.labvcn.oraclevcn.com
Start options: open
Stop options: immediate
Database role: PRIMARY
Management policy: AUTOMATIC
Server pools:
Disk Groups: RECO,DATA
Mount point paths:
Services:
Type: RAC
Start concurrency:
Stop concurrency:
OSDBA group: dba
OSOPER group: dbaoper
Database instances: DB09021,DB09022
Configured nodes: rac1,rac2
CSS critical: no
CPU count: 0
Memory target: 0
Maximum memory: 0
Default network number for database services:
Database is administrator managed
[oracle@rac1 ~]$

```
