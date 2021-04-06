## GoldenGate Capture from a DataGuard with Cascaded Redo Logs
### Downstream Mining Server Configuration Steps

---
* source    : rac1.sh    (DB09021, db0902_yny19m, rac-scan.subnet1.labvcn.oraclevcn.com) 
* mining db : db19c.sh   (ORCL,ORCL)
* target    : primary.sh (ORCL) 
---

###  순서
* Set LOG_ARCHIVE_CONFIG
* Set LOG_ARCHIVE_DEST_1 : location for local archives
* Set LOG_ARCHIVE_DEST_2 : for foreign archives

```sql
SQL> alter system set log_archive_config='DG_CONFIG=(DB0902_YNY19M, ORCL)';

System altered.

SQL> alter system set LOG_ARCHIVE_DEST_1='LOCATION=/u01/app/oracle/fra/ORCL/ORCL/archivelog VALID_FOR=(ONLINE_LOGFILE, PRIMARY_ROLE)';

System altered.

SQL> alter system set LOG_ARCHIVE_DEST_2='LOCATION=/u01/app/oracle/foreign_archives VALID_FOR=(STANDBY_LOGFILES, ALL_ROLES)';

System altered.

```
* Set Standby Logfile Groups

```sql

SQL> ALTER DATABASE ADD STANDBY LOGFILE GROUP 4 ('/u01/app/oracle/oradata/ORCL/slog4a.rdo', '/u01/app/oracle/oradata/ORCL/slog4b.rdo') SIZE 1024M;

Database altered.

SQL> ALTER DATABASE ADD STANDBY LOGFILE GROUP 5 ('/u01/app/oracle/oradata/ORCL/slog5a.rdo', '/u01/app/oracle/oradata/ORCL/slog5b.rdo') SIZE 1024M;

Database altered.

SQL> ALTER DATABASE ADD STANDBY LOGFILE GROUP 6 ('/u01/app/oracle/oradata/ORCL/slog6a.rdo', '/u01/app/oracle/oradata/ORCL/slog6b.rdo') SIZE 1024M;

Database altered.

SQL> ALTER DATABASE ADD STANDBY LOGFILE GROUP 7 ('/u01/app/oracle/oradata/ORCL/slog7a.rdo', '/u01/app/oracle/oradata/ORCL/slog7b.rdo') SIZE 1024M;

Database altered.

SQL> ALTER DATABASE ADD STANDBY LOGFILE GROUP 4 ('/u01/app/oracle/oradata/ORCL/slog4a.rdo', '/u01/app/oracle/oradata/ORCL/slog4b.rdo') SIZE 1024M;

```
* Copy password file from Source to Downstream
* Open SQL*Net Port
  * Create TNSNAMES entry for Source System
* Create Mining Database Capture User 

```sql
[oracle@db19c ~]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Tue Apr 6 10:26:40 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

SQL> alter user sys identified by WElcome123##;

User altered.

SQL> create user c##min identified by ogg;

User created.

SQL> exec dbms_goldengate_auth.grant_admin_privilege('C##MIN',container=>'ALL');

PL/SQL procedure successfully completed.

SQL> grant dba to c##min container=all;

Grant succeeded.

SQL> connect c##min/ogg
Connected.
SQL>
```
* Enable Supplemental Logging
* Create & Start Downstream Extract Process



### tips

* rac password file 

```sql
[grid@rac1 ~]$ srvctl config database -d db0902_yny19m
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
Services: fan,svctest,TAF,unisrv
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
```

```bash
[oracle@db19c ~]$ cp /tmp/pwddb0902_yny19m $ORACLE_HOME/dbs/pwddb0902_yny19m
[oracle@db19c dbs]$ cp orapwORCL orapwORCL.org
[oracle@db19c dbs]$ cp pwddb0902_yny19m orapwORCL

```

```
[grid@rac1 ~]$ asmcmd
ASMCMD> pwcopy
usage: pwcopy [ --dbuniquename <string> | --asm ][-f]
        <source_path> <destination_path>
help:  help pwcopy
ASMCMD> pwcopy +DATA/DB0902_YNY19M/PASSWORD/pwddb0902_yny19m.259.1050063751 /tmp/pwddb0902_yny19m
copying +DATA/DB0902_YNY19M/PASSWORD/pwddb0902_yny19m.259.1050063751 -> /tmp/pwddb0902_yny19m
ASMCMD>
```

