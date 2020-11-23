## [Oracle Database 12c Backup and Recovery Survival Guide](https://resources.oreilly.com/examples/9781782171201)
* [침조](https://resources.oreilly.com/examples/9781782171201/blob/master/Appendix_code/appendix_examples.sql)
* learning.oreilly.com : oracle SSO
### --- Setup of environment

```bash
[opc@odi2 ~]$ sudo mkdir /u01/pdb
[opc@odi2 ~]$ sudo chown oracle:oinstall /u01/pdb

[opc@odi2 ~]$ sudo mkdir /u01/pdb/backups
[opc@odi2 ~]$ sudo chown oracle:oinstall /u01/pdb/backups

```

```sql
ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE;

ALTER PROFILE DEFAULT LIMIT PASSWORD_VERIFY_FUNCTION NULL;

```

```sql
SYS@odidb2>  alter session set container=pdb;

Session altered.

SYS@odidb2> 
SYS@odidb2>CREATE TABLESPACE test DATAFILE '+DATA';
  
Tablespace created.


SYS@odidb2> ALTER PROFILE DEFAULT LIMIT PASSWORD_VERIFY_FUNCTION NULL;

Profile altered.

SYS@odidb2> create user test identified by test default tablespace TEST quota unlimited on test;

User created.

SYS@odidb2> CREATE TABLE TEST.EMPLOYEE
( EMP_ID   NUMBER(10) NOT NULL,
  EMP_NAME VARCHAR2(30),
  EMP_SSN  VARCHAR2(9),
  EMP_DOB  DATE
);

Table created.
SYS@odidb2> ed
Wrote file /home/oracle/coet/sql/afiedt.buf

  1* INSERT INTO test.employee VALUES (101,'Francisco Munoz',123456789,to_date('30-JUN-73','DD-MON-YY'))
SYS@odidb2> /
SYS@odidb2> INSERT INTO test.employee VALUES (102,'Gonzalo Munoz',234567890,to_date('02-OCT-96','DD-MON-YY'));

1 row created.

SYS@odidb2> INSERT INTO test.employee VALUES (103,'Evelyn Aghemio',659812831,to_date('02-OCT-79','DD-MON-YY'));

1 row created.
SYS@odidb2> commit;

Commit complete.

SYS@odidb2>


```

### --- Configure Database

```sql

SYS@odidb2> SYS@odidb2> CREATE USER backup_admin IDENTIFIED BY bckpwd DEFAULT TABLESPACE users;


User created.

Elapsed: 00:00:00.05
SYS@odidb2> SYS@odidb2>
SYS@odidb2>
SYS@odidb2> GRANT sysbackup TO backup_admin;

Grant succeeded.

Elapsed: 00:00:00.52

SYS@odidb2> GRANT dba TO backup_admin;

Grant succeeded.

Elapsed: 00:00:00.52
```

```bash

[oracle@odi2 ~]$ rman catalog backup_admin/bckpwd@//10.0.0.8:1521/pdb.dbsecsubnet.dbsecvcn.oraclevcn.com

Recovery Manager: Release 19.0.0.0.0 - Production on Mon Nov 23 18:01:44 2020
Version 19.8.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

connected to recovery catalog database

RMAN>create catalog tablespace catalog_ts; 
/* recovery catalog 생성  */

```

```bash
[oracle@odi2 ~]$ rman target=/ catalog backup_admin/bckpwd@//10.0.0.8:1521/pdb.dbsecsubnet.dbsecvcn.oraclevcn.com

Recovery Manager: Release 19.0.0.0.0 - Production on Mon Nov 23 18:02:37 2020
Version 19.8.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

connected to target database: ODIDB (DBID=944821679)
connected to recovery catalog database

RMAN>  register database;

database registered in recovery catalog
starting full resync of recovery catalog
full resync complete

RMAN>
RMAN>  CONFIGURE BACKUP OPTIMIZATION ON;

new RMAN configuration parameters:
CONFIGURE BACKUP OPTIMIZATION ON;
new RMAN configuration parameters are successfully stored
starting full resync of recovery catalog
full resync complete

RMAN> CONFIGURE CONTROLFILE AUTOBACKUP ON;

new RMAN configuration parameters:
CONFIGURE CONTROLFILE AUTOBACKUP ON;
new RMAN configuration parameters are successfully stored
starting full resync of recovery catalog
full resync complete

RMAN> CONFIGURE CHANNEL 1 DEVICE TYPE DISK FORMAT '/u01/pdb/backups /bck_orcl_%U';

new RMAN configuration parameters:
CONFIGURE CHANNEL 1 DEVICE TYPE DISK FORMAT   '/u01/pdb/backups /bck_orcl_%U';
new RMAN configuration parameters are successfully stored
starting full resync of recovery catalog
full resync complete

RMAN> CONFIGURE CHANNEL 1 DEVICE TYPE DISK MAXPIECESIZE 200m MAXOPENFILES 8 RATE 150m;

old RMAN configuration parameters:
CONFIGURE CHANNEL 1 DEVICE TYPE DISK FORMAT   '/u01/pdb/backups /bck_orcl_%U';
new RMAN configuration parameters:
CONFIGURE CHANNEL 1 DEVICE TYPE DISK MAXPIECESIZE 200 M MAXOPENFILES 8 RATE 150 M;
new RMAN configuration parameters are successfully stored
starting full resync of recovery catalog
full resync complete

RMAN>

RMAN> CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '/u01/pdb/backups/controlfile/ctl_pdb_%F';


new RMAN configuration parameters:
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '/u01/pdb/backups/controlfile/ctl_pdb_%F';
new RMAN configuration parameters are successfully stored
starting full resync of recovery catalog
full resync complete


RMAN>
RMAN> CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 1 DAYS;

new RMAN configuration parameters:
CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 1 DAYS;
new RMAN configuration parameters are successfully stored
starting full resync of recovery catalog
full resync complete

RMAN> CONFIGURE ARCHIVELOG DELETION POLICY TO BACKED UP 1 TIMES TO DISK;


new RMAN configuration parameters:
CONFIGURE ARCHIVELOG DELETION POLICY TO BACKED UP 1 TIMES TO DISK;
new RMAN configuration parameters are successfully stored
starting full resync of recovery catalog
full resync complete

RMAN>
RMAN> BACKUP DATABASE PLUS ARCHIVELOG;



Starting backup at 2020-11-23 18:19:51
current log archived
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=30 instance=odidb2 device type=DISK
channel ORA_DISK_1: starting archived log backup set
channel ORA_DISK_1: specifying archived log(s) in backup set
input archived log thread=2 sequence=46 RECID=65 STAMP=1054459459
input archived log thread=2 sequence=47 RECID=66 STAMP=1054459794
input archived log thread=1 sequence=20 RECID=68 STAMP=1054460343
input archived log thread=2 sequence=48 RECID=67 STAMP=1054460141
input archived log thread=2 sequence=49 RECID=69 STAMP=1054460355
input archived log thread=2 sequence=50 RECID=70 STAMP=1054466973
input archived log thread=1 sequence=21 RECID=72 STAMP=1054469752
input archived log thread=2 sequence=51 RECID=71 STAMP=1054468618
input archived log thread=2 sequence=52 RECID=73 STAMP=1054469758
input archived log thread=2 sequence=53 RECID=74 STAMP=1054471072
input archived log thread=1 sequence=22 RECID=76 STAMP=1054472336
input archived log thread=2 sequence=54 RECID=75 STAMP=1054471726
input archived log thread=2 sequence=55 RECID=77 STAMP=1054472348
input archived log thread=2 sequence=56 RECID=78 STAMP=1054472937
input archived log thread=1 sequence=23 RECID=80 STAMP=1054474206
input archived log thread=2 sequence=57 RECID=79 STAMP=1054473596
input archived log thread=2 sequence=58 RECID=81 STAMP=1054474218
input archived log thread=2 sequence=59 RECID=82 STAMP=1054474869
input archived log thread=1 sequence=24 RECID=84 STAMP=1054476144
input archived log thread=2 sequence=60 RECID=83 STAMP=1054475527
input archived log thread=2 sequence=61 RECID=85 STAMP=1054476158
input archived log thread=2 sequence=62 RECID=86 STAMP=1054476798
input archived log thread=1 sequence=25 RECID=88 STAMP=1054478178
input archived log thread=2 sequence=63 RECID=87 STAMP=1054477496
input archived log thread=2 sequence=64 RECID=89 STAMP=1054478190
input archived log thread=2 sequence=65 RECID=90 STAMP=1054479038
input archived log thread=1 sequence=26 RECID=92 STAMP=1054480521
input archived log thread=2 sequence=66 RECID=91 STAMP=1054479784
input archived log thread=2 sequence=67 RECID=93 STAMP=1054480549
input archived log thread=2 sequence=68 RECID=94 STAMP=1054481292
input archived log thread=1 sequence=27 RECID=96 STAMP=1054666833
input archived log thread=2 sequence=69 RECID=95 STAMP=1054482045
...

```

### --- Backup Database

### --- Check for Obsolete

### --- Creating RMAN user

### --- Creating Catalog

### --- Create a virtual Private Catalog

### --- Enabling Block TRacking

### --- Monitoring a Backup

### --- Incremental Backups

### --- Multisection Backups

### --- FRA -Checking times of redo switches

### --- Check FRA usage

### --- See Archivelog Generated

### --- See Control file backups

