## GoldenGate Capture from a DataGuard with Cascaded Redo Logs
### Downstream Mining Server Configuration Steps

---
* source    : rac1.sh    (DB09021, db0902_yny19m, rac-scan.subnet1.labvcn.oraclevcn.com) 
* mining db : db19c.sh   (ORCL,ORCL)
* target    : primary.sh (ORCL) 
---

###  순서
* paramter

```sql
SQL> alter system set enable_goldengate_replication=true;

System altered.

SQL>  show parameter enable_goldengate_replication


NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
enable_goldengate_replication        boolean     TRUE
SQL> 
```
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

```sql
[oracle@db19c ~]$ ggsci

Oracle GoldenGate Command Interpreter for Oracle
Version 19.1.0.0.4 OGGCORE_19.1.0.0.0_PLATFORMS_191017.1054_FBO
Linux, x64, 64bit (optimized), Oracle 19c on Oct 17 2019 21:16:29
Operating system character set identified as UTF-8.

Copyright (C) 1995, 2019, Oracle and/or its affiliates. All rights reserved.
GGSCI (db19c) 2>  DBLOGIN USERID c##ggadmin@src PASSWORD ggadmin
Successfully logged into database CDB$ROOT.


GGSCI (db19c as c##ggadmin@DB09021/CDB$ROOT) 5>  ADD SCHEMATRANDATA DB0902_PDB1.HR PREPARECSN

2021-04-06 12:42:59  INFO    OGG-01788  SCHEMATRANDATA has been added on schema "HR".

2021-04-06 12:42:59  INFO    OGG-01976  SCHEMATRANDATA for scheduling columns has been added on schema "HR".

2021-04-06 12:43:00  INFO    OGG-10154  Schema level PREPARECSN set to mode NOWAIT on schema "HR".

2021-04-06 12:43:03  INFO    OGG-10471  ***** Oracle Goldengate support information on table HR.COUNTRIES *****
Oracle Goldengate support native capture on table HR.COUNTRIES.
Oracle Goldengate marked following column as key columns on table HR.COUNTRIES: COUNTRY_ID.

2021-04-06 12:43:03  INFO    OGG-10471  ***** Oracle Goldengate support information on table HR.DEPARTMENTS *****
Oracle Goldengate support native capture on table HR.DEPARTMENTS.
Oracle Goldengate marked following column as key columns on table HR.DEPARTMENTS: DEPARTMENT_ID.

2021-04-06 12:43:03  INFO    OGG-10471  ***** Oracle Goldengate support information on table HR.EMPLOYEES *****
Oracle Goldengate support native capture on table HR.EMPLOYEES.
Oracle Goldengate marked following column as key columns on table HR.EMPLOYEES: EMPLOYEE_ID.

2021-04-06 12:43:03  INFO    OGG-10471  ***** Oracle Goldengate support information on table HR.JOBS *****
Oracle Goldengate support native capture on table HR.JOBS.
Oracle Goldengate marked following column as key columns on table HR.JOBS: JOB_ID.

2021-04-06 12:43:03  INFO    OGG-10471  ***** Oracle Goldengate support information on table HR.JOB_HISTORY *****
Oracle Goldengate support native capture on table HR.JOB_HISTORY.
Oracle Goldengate marked following column as key columns on table HR.JOB_HISTORY: EMPLOYEE_ID, START_DATE.

2021-04-06 12:43:03  INFO    OGG-10471  ***** Oracle Goldengate support information on table HR.LOCATIONS *****
Oracle Goldengate support native capture on table HR.LOCATIONS.
Oracle Goldengate marked following column as key columns on table HR.LOCATIONS: LOCATION_ID.

2021-04-06 12:43:03  INFO    OGG-10471  ***** Oracle Goldengate support information on table HR.REGIONS *****
Oracle Goldengate support native capture on table HR.REGIONS.
Oracle Goldengate marked following column as key columns on table HR.REGIONS: REGION_ID.
```

```sql
GGSCI (db19c as c##ggadmin@DB09021/CDB$ROOT) 7> INFO SCHEMATRANDATA  DB0902_PDB1.HR
GGSCI (db19c as c##ggadmin@DB09021/CDB$ROOT) 9>  info trandata DB0902_PDB1.HR.*
```
  * A query against the “SOURCE” or “STANDBY” databases can also verify if individual tables have been prepared for instantiation.
  * Note:. The scn is the smallest system change number (SCN) for which the table can be instantiated. It is not the export SCN.
```sql
SYS@DB09021>  select table_name, scn from dba_capture_prepared_tables where table_owner = 'HR';


TABLE_NAME                            SCN
------------------------------ ----------
JOB_HISTORY                      46570629
COUNTRIES                        46570606
LOCATIONS                        46570635
JOBS                             46570624
EMPLOYEES                        46570618
REGIONS                          46570640
DEPARTMENTS                      46570613
```

* Create & Start Downstream Extract Process
  * SRC DB login via GGSCI on the mining server
```
GGSCI (db19c) 1>  DBLOGIN USERID c##ggadmin@src PASSWORD ggadmin
Successfully logged into mining database.

```

  * Mining DB login
```
GGSCI (db19c as c##ggadmin@DB09021/CDB$ROOT) 4>  MININGDBLOGIN USERID c##min@mining PASSWORD ogg
Successfully logged into mining database.

GGSCI (db19c as c##ggadmin@DB09021/CDB$ROOT) 5> register extract eapps database container (DB0902_PDB1)
2021-04-06 12:59:49  INFO    OGG-02003  Extract EAPPS successfully registered with database at SCN 46574593.

GGSCI (db19c as c##ggadmin@DB09021/CDB$ROOT) 8> CREATE SUBDIRS

Creating subdirectories under current directory /home/oracle

Parameter file                 /u01/app/oracle/ogg/dirprm: created.
Report file                    /u01/app/oracle/ogg/dirrpt: created.
Checkpoint file                /u01/app/oracle/ogg/dirchk: created.
Process status files           /u01/app/oracle/ogg/dirpcs: created.
SQL script files               /u01/app/oracle/ogg/dirsql: created.
Database definitions files     /u01/app/oracle/ogg/dirdef: created.
Extract data files             /u01/app/oracle/ogg/dirdat: created.
Temporary files                /u01/app/oracle/ogg/dirtmp: created.
Credential store files         /u01/app/oracle/ogg/dircrd: created.
Masterkey wallet files         /u01/app/oracle/ogg/dirwlt: created.
Dump files                     /u01/app/oracle/ogg/dirdmp: created.


GGSCI (db19c as c##ggadmin@DB09021/CDB$ROOT) 9> ADD EXTRACT eapps INTEGRATED TRANLOG BEGIN NOW
EXTRACT (Integrated) added.
GGSCI (db19c as c##ggadmin@DB09021/CDB$ROOT) 10> ADD EXTTRAIL ./dirdat/lt, EXTRACT eapps
EXTTRAIL added.

GGSCI (db19c as c##ggadmin@DB09021/CDB$ROOT) 11> info all

Program     Status      Group       Lag at Chkpt  Time Since Chkpt

MANAGER     STOPPED
EXTRACT     STOPPED     EAPPS       00:00:00      00:01:01



```

```
[oracle@db19c ogg]$
[oracle@db19c ogg]$ cat /u01/app/oracle/ogg/dirprm/mgr.prm
PORT 7809
```

```
[oracle@db19c ogg]$ vi /u01/app/oracle/ogg/dirprm/eapps.prm
[oracle@db19c ogg]$ cat /u01/app/oracle/ogg/dirprm/eapps.prm
EXTRACT EAPPS
-- Not logging into Source Database. Must use NOUSERID
NOUSERID
-- When using NOUSERID, FETCHUSERID of standby must be specified
FETCHUSERID c##ggadmin@to_stby, password ggadmin
-- Force Extract to Abend after the default of 30 seconds if the ADG is
-- behind the mining extract on a Fetch.
DBOPTIONS FETCHTIMEOUT
-- Extract will wait the default of 3 seconds between each check while
-- waiting for ADG to catch up
DBOPTIONS FETCHCHECKFREQ
-- Mining Database Login
TRANLOGOPTIONS MININGUSER c##min@orcl, MININGPASSWORD ogg
-- Specify Real-Time Mode not Archive Log Only mode
TRANLOGOPTIONS INTEGRATEDPARAMS (DOWNSTREAM_REAL_TIME_MINE Y)
EXTTRAIL ./dirdat/lt
TABLE DB0902_PDB1.APPS.*;
```

```sql
GGSCI (db19c) 2> start eapps

Sending START request to MANAGER ...
EXTRACT EAPPS starting
```
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



