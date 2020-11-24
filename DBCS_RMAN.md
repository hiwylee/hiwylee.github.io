## DBCS Backup & Restore with RMAN
### 참조 
* [ Backup Oracle database to OCI Object storage.](https://www.oraclecloudadmin.com/2020/08/backup-oracle-database-to-oci-object.html)
* [Backing Up a Database to Object Storage Using RMAN(https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Tasks/backingupOSrman.htm#prerequisites)
* oci authentication changed .

#### Installing the Backup Module on the DB System

```bash
[oracle@rat odbcs]$ cat install.sh
java -jar opc_install.jar -opcId 'oracleidentitycloudservice/wonyong.lee@oracle.com' -opcPass 'pPB7jSBHz(:D4HvzyWb}' -container DB_BACKUP -walletDir ~/wallet/ -libDir ~/lib/ -configfile ~/config -host https://swiftobjectstorage.ap-chuncheon-1.oraclecloud.com/v1/idx9wbxtnehn

[oracle@rat odbcs]$ sh install.sh
Oracle Database Cloud Backup Module Install Tool, build 12.2.0.1.0DBBKPCSBP_2018-06-12
Backups would be sent to container DB_BACKUP.
Oracle Database Cloud Backup Module wallet created in directory /home/oracle/wallet.
Oracle Database Cloud Backup Module initialization file /home/oracle/config created.
Downloading Oracle Database Cloud Backup Module Software Library from file opc_linux64.zip.
Download complete.
[oracle@rat odbcs]$

```

#### Configuring RMAN


```sql
[oracle@rat ~]$ rman target=/

Recovery Manager: Release 19.0.0.0.0 - Production on Tue Nov 24 18:32:15 2020
Version 19.9.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

connected to target database: PROD (DBID=468584496)

RMAN> show all
2> ;

using target database control file instead of recovery catalog
RMAN configuration parameters for database with db_unique_name PROD_YNY1HG are:
CONFIGURE RETENTION POLICY TO REDUNDANCY 1; # default
CONFIGURE BACKUP OPTIMIZATION OFF; # default
CONFIGURE DEFAULT DEVICE TYPE TO DISK;
CONFIGURE CONTROLFILE AUTOBACKUP ON;
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '%F'; # default
CONFIGURE DEVICE TYPE DISK PARALLELISM 1 BACKUP TYPE TO BACKUPSET; # default
CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE DISK TO 1; # default
CONFIGURE ARCHIVELOG BACKUP COPIES FOR DEVICE TYPE DISK TO 1; # default
CONFIGURE CHANNEL DEVICE TYPE DISK FORMAT   '/u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/rat_%U';
CONFIGURE MAXSETSIZE TO UNLIMITED; # default
CONFIGURE ENCRYPTION FOR DATABASE OFF; # default
CONFIGURE ENCRYPTION ALGORITHM 'AES128'; # default
CONFIGURE COMPRESSION ALGORITHM 'BASIC' AS OF RELEASE 'DEFAULT' OPTIMIZE FOR LOAD TRUE ; # default
CONFIGURE RMAN OUTPUT TO KEEP FOR 7 DAYS; # default
CONFIGURE ARCHIVELOG DELETION POLICY TO NONE; # default
CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/u01/app/oracle/product/19.0.0/dbhome_1/dbs/snapcf_prod.f'; # default

RMAN> 

RMAN> CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS 'SBT_LIBRARY=/home/oracle/lib/libopc.so, SBT_PARMS=(OPC_PFILE=/home/oracle/config)';

using target database control file instead of recovery catalog
new RMAN configuration parameters:
CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS  'SBT_LIBRARY=/home/oracle/lib/libopc.so, SBT_PARMS=(OPC_PFILE=/home/oracle/config)';
new RMAN configuration parameters are successfully stored

RMAN>

RMAN> configure default device type to SBT_TYPE;

old RMAN configuration parameters:
CONFIGURE DEFAULT DEVICE TYPE TO DISK;
new RMAN configuration parameters:
CONFIGURE DEFAULT DEVICE TYPE TO 'SBT_TYPE';
new RMAN configuration parameters are successfully stored

RMAN> configure backup optimization on;

new RMAN configuration parameters:
CONFIGURE BACKUP OPTIMIZATION ON;
new RMAN configuration parameters are successfully stored

RMAN>

RMAN> configure controlfile autobackup on;

old RMAN configuration parameters:
CONFIGURE CONTROLFILE AUTOBACKUP ON;
new RMAN configuration parameters:
CONFIGURE CONTROLFILE AUTOBACKUP ON;
new RMAN configuration parameters are successfully stored

RMAN> configure controlfile autobackup format for device type SBT_TYPE to '%F';

new RMAN configuration parameters:
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE 'SBT_TYPE' TO '%F';
new RMAN configuration parameters are successfully stored

RMAN> configure encryption for database on;

new RMAN configuration parameters:
CONFIGURE ENCRYPTION FOR DATABASE ON;
new RMAN configuration parameters are successfully stored

RMAN> show all
2> ;

RMAN configuration parameters for database with db_unique_name PROD_YNY1HG are:
CONFIGURE RETENTION POLICY TO REDUNDANCY 1; # default
CONFIGURE BACKUP OPTIMIZATION ON;
CONFIGURE DEFAULT DEVICE TYPE TO 'SBT_TYPE';
CONFIGURE CONTROLFILE AUTOBACKUP ON;
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE 'SBT_TYPE' TO '%F';
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '%F'; # default
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE SBT_TAPE TO '%F'; # default
CONFIGURE DEVICE TYPE SBT_TYPE PARALLELISM 1 BACKUP TYPE TO BACKUPSET; # default
CONFIGURE DEVICE TYPE DISK PARALLELISM 1 BACKUP TYPE TO BACKUPSET; # default
CONFIGURE DEVICE TYPE SBT_TAPE PARALLELISM 1 BACKUP TYPE TO BACKUPSET; # default
CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE SBT_TYPE TO 1; # default
CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE DISK TO 1; # default
CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE SBT_TAPE TO 1; # default
CONFIGURE ARCHIVELOG BACKUP COPIES FOR DEVICE TYPE SBT_TYPE TO 1; # default
CONFIGURE ARCHIVELOG BACKUP COPIES FOR DEVICE TYPE DISK TO 1; # default
CONFIGURE ARCHIVELOG BACKUP COPIES FOR DEVICE TYPE SBT_TAPE TO 1; # default
CONFIGURE CHANNEL DEVICE TYPE DISK FORMAT   '/u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/rat_%U';
CONFIGURE CHANNEL DEVICE TYPE 'SBT_TAPE' PARMS  'SBT_LIBRARY=/home/oracle/lib/libopc.so, SBT_PARMS=(OPC_PFILE=/home/oracle/config)';
CONFIGURE MAXSETSIZE TO UNLIMITED; # default
CONFIGURE ENCRYPTION FOR DATABASE ON;
CONFIGURE ENCRYPTION ALGORITHM 'AES128'; # default
CONFIGURE COMPRESSION ALGORITHM 'BASIC' AS OF RELEASE 'DEFAULT' OPTIMIZE FOR LOAD TRUE ; # default
CONFIGURE RMAN OUTPUT TO KEEP FOR 7 DAYS; # default
CONFIGURE ARCHIVELOG DELETION POLICY TO NONE; # default
CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/u01/app/oracle/product/19.0.0/dbhome_1/dbs/snapcf_prod.f'; # default

RMAN>


```
---
#### Backing up the Database

```sql

RMAN> SET ENCRYPTION IDENTIFIED BY "password" ONLY;

executing command: SET encryption

RMAN> BACKUP INCREMENTAL LEVEL 0 SECTION SIZE 512M DATABASE PLUS ARCHIVELOG;

Starting backup at 24-NOV-20
current log archived
RMAN-00571: ===========================================================
RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
RMAN-00571: ===========================================================
RMAN-03002: failure of backup plus archivelog command at 11/24/2020 20:03:51
ORA-19554: error allocating device, device type: SBT_TYPE, device name:
ORA-27001: unsupported device type

RMAN> CONFIGURE DEFAULT DEVICE TYPE TO SBT_TAPE;

old RMAN configuration parameters:
CONFIGURE DEFAULT DEVICE TYPE TO 'SBT_TYPE';
new RMAN configuration parameters:
CONFIGURE DEFAULT DEVICE TYPE TO 'SBT_TAPE';
new RMAN configuration parameters are successfully stored

RMAN> BACKUP INCREMENTAL LEVEL 0 SECTION SIZE 512M DATABASE PLUS ARCHIVELOG;


Starting backup at 24-NOV-20
current log archived
allocated channel: ORA_SBT_TAPE_1
channel ORA_SBT_TAPE_1: SID=12 device type=SBT_TAPE
channel ORA_SBT_TAPE_1: Oracle Database Backup Service Library VER=19.0.0.1
channel ORA_SBT_TAPE_1: starting archived log backup set
channel ORA_SBT_TAPE_1: specifying archived log(s) in backup set
input archived log thread=1 sequence=7 RECID=7 STAMP=1057324516
input archived log thread=1 sequence=8 RECID=8 STAMP=1057325676
input archived log thread=1 sequence=9 RECID=9 STAMP=1057326031
input archived log thread=1 sequence=10 RECID=10 STAMP=1057328844
input archived log thread=1 sequence=11 RECID=11 STAMP=1057349030
input archived log thread=1 sequence=12 RECID=12 STAMP=1057349121
channel ORA_SBT_TAPE_1: starting piece 1 at 24-NOV-20
channel ORA_SBT_TAPE_1: finished piece 1 at 24-NOV-20
piece handle=0hvgbng1_1_1 tag=TAG20201124T200521 comment=API Version 2.0,MMS Version 19.0.0.1
channel ORA_SBT_TAPE_1: backup set complete, elapsed time: 00:00:07
Finished backup at 24-NOV-20

.....

channel ORA_SBT_TAPE_1: starting piece 1 at 24-NOV-20
channel ORA_SBT_TAPE_1: finished piece 1 at 24-NOV-20
piece handle=2mvgbnm8_1_1 tag=TAG20201124T200529 comment=API Version 2.0,MMS Version 19.0.0.1
channel ORA_SBT_TAPE_1: backup set complete, elapsed time: 00:00:01
Finished backup at 24-NOV-20

Starting backup at 24-NOV-20
current log archived
using channel ORA_SBT_TAPE_1
channel ORA_SBT_TAPE_1: starting archived log backup set
channel ORA_SBT_TAPE_1: specifying archived log(s) in backup set
input archived log thread=1 sequence=13 RECID=13 STAMP=1057349321
channel ORA_SBT_TAPE_1: starting piece 1 at 24-NOV-20
channel ORA_SBT_TAPE_1: finished piece 1 at 24-NOV-20
piece handle=2nvgbnm9_1_1 tag=TAG20201124T200841 comment=API Version 2.0,MMS Version 19.0.0.1
channel ORA_SBT_TAPE_1: backup set complete, elapsed time: 00:00:01
Finished backup at 24-NOV-20

Starting Control File and SPFILE Autobackup at 24-NOV-20
piece handle=c-468584496-20201124-04 comment=API Version 2.0,MMS Version 19.0.0.1
Finished Control File and SPFILE Autobackup at 24-NOV-20

RMAN>


```

### make CHange to DB

```sql

SQL> create table test(i int);

Table created.

SQL> insert into test values(1);

1 row created.

SQL> /

1 row created.

SQL> /

1 row created.

SQL> commit;

Commit complete.

SQL> ed
Wrote file afiedt.buf

  1* alter system switch logfile
SQL> /

System altered.

SQL>

```
---

#### Recovering a Database from Object Storage.
* RMAN COMMAND

```sql
set decryption identified by "password";
set controlfile autobackup format for device type sbt to '%F';
run {
  allocate channel c2 device type sbt PARMS 'SBT_LIBRARY=/home/oracle/lib/libopc.so, SBT_PARMS=(OPC_PFILE=/home/oracle/config)';
  restore controlfile from autobackup;
  alter database mount;
  RESTORE DATABASE;
  RECOVER DATABASE;
    }
```	


* DBID

```sql
SQL> select DBID from v$database;

      DBID
----------
 468584496
```

```sql
[oracle@rat lib]$ rman target /

Recovery Manager: Release 19.0.0.0.0 - Production on Tue Nov 24 20:35:18 2020
Version 19.9.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

connected to target database (not started)

RMAN> set dbid 468584496

executing command: SET DBID

RMAN>  STARTUP NOMOUNT

Oracle instance started

Total System Global Area   30601641080 bytes

Fixed Size                    12692600 bytes
Variable Size               3556769792 bytes
Database Buffers           26977763328 bytes
Redo Buffers                  54415360 bytes

RMAN>

```

```sql

RMAN> set decryption identified by "password";

executing command: SET decryption

RMAN> set controlfile autobackup format for device type sbt to '%F';

executing command: SET CONTROLFILE AUTOBACKUP FORMAT

RMAN> run {
  allocate channel c1 device type sbt PARMS 'SBT_LIBRARY=/home/oracle/lib/libopc.so, SBT_PARMS=(OPC_PFILE=/home/oracle/config)';
2> 3>   restore controlfile from autobackup;
4>   alter database mount;
    }5>

allocated channel: c1
channel c1: SID=1 device type=SBT_TAPE
channel c1: Oracle Database Backup Service Library VER=19.0.0.1

Starting restore at 24-NOV-20

channel c1: looking for AUTOBACKUP on day: 20201124
channel c1: AUTOBACKUP found: c-468584496-20201124-05
channel c1: restoring control file from AUTOBACKUP c-468584496-20201124-05
channel c1: control file restore from AUTOBACKUP complete
output file name=/u02/app/oracle/oradata/prod_yny1hg/control01.ctl
output file name=/u03/app/oracle/fast_recovery_area/PROD_YNY1HG/control02.ctl
Finished restore at 24-NOV-20

Statement processed
released channel: c1

RMAN>


```

#### Restore & Recover Database
```sql
RMAN> RESTORE DATABASE;

Starting restore at 24-NOV-20
Starting implicit crosscheck backup at 24-NOV-20
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=1 device type=DISK
Crosschecked 11 objects
Finished implicit crosscheck backup at 24-NOV-20

Starting implicit crosscheck copy at 24-NOV-20
using channel ORA_DISK_1
Finished implicit crosscheck copy at 24-NOV-20

searching for all files in the recovery area
cataloging files...
cataloging done

List of Cataloged Files
=======================
File Name: /u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/o1_mf_s_1057325059_hvs2qmz1_.bkp
File Name: /u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/o1_mf_s_1057329072_hvs6o0xf_.bkp
File Name: /u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/o1_mf_s_1057326190_hvs3tykq_.bkp

using channel ORA_DISK_1

creating datafile file number=14 name=/u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/datafile/o1_mf_test_ts_hvs2g4g7_.dbf
skipping datafile 5; already restored to file /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/B21673D7363B1806E053C305F40A9423/datafile/o1_mf_system_hv7fd45o_.dbf
skipping datafile 6; already restored to file /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/B21673D7363B1806E053C305F40A9423/datafile/o1_mf_sysaux_hv7fcp1x_.dbf
skipping datafile 8; already restored to file /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/B21673D7363B1806E053C305F40A9423/datafile/o1_mf_undotbs1_hv7fdfg3_.dbf
channel ORA_DISK_1: starting datafile backup set restore
channel ORA_DISK_1: specifying datafile(s) to restore from backup set
channel ORA_DISK_1: restoring datafile 00001 to /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/datafile/o1_mf_system_hvs38m2q_.dbf
channel ORA_DISK_1: restoring datafile 00003 to /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/datafile/o1_mf_sysaux_hv7fcp1z_.dbf
channel ORA_DISK_1: restoring datafile 00004 to /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/datafile/o1_mf_undotbs1_hv7fcp28_.dbf
channel ORA_DISK_1: restoring datafile 00007 to /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/datafile/o1_mf_users_hv7fhg6b_.dbf
channel ORA_DISK_1: restoring datafile 00013 to /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/datafile/example.dbf
channel ORA_DISK_1: reading from backup piece /u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/PROD_05vgaqhd_1_1
channel ORA_DISK_1: piece handle=/u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/PROD_05vgaqhd_1_1 tag=TAG20201124T115108
channel ORA_DISK_1: restored backup piece 1
channel ORA_DISK_1: restore complete, elapsed time: 00:02:25
channel ORA_DISK_1: starting datafile backup set restore
channel ORA_DISK_1: specifying datafile(s) to restore from backup set
channel ORA_DISK_1: restoring datafile 00009 to /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/B2169F489B0C1E32E053C305F40A9E33/datafile/o1_mf_system_hv7flbbk_.dbf
channel ORA_DISK_1: restoring datafile 00010 to /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/B2169F489B0C1E32E053C305F40A9E33/datafile/o1_mf_sysaux_hv7fllgz_.dbf
channel ORA_DISK_1: restoring datafile 00011 to /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/B2169F489B0C1E32E053C305F40A9E33/datafile/o1_mf_undotbs1_hv7flsz7_.dbf
channel ORA_DISK_1: restoring datafile 00012 to /u02/app/oracle/oradata/prod_yny1hg/PROD_YNY1HG/B2169F489B0C1E32E053C305F40A9E33/datafile/o1_mf_users_hv7fhjfx_.dbf
channel ORA_DISK_1: reading from backup piece /u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/PROD_06vgaqht_1_1
channel ORA_DISK_1: piece handle=/u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/PROD_06vgaqht_1_1 tag=TAG20201124T115108
channel ORA_DISK_1: restored backup piece 1
channel ORA_DISK_1: restore complete, elapsed time: 00:00:07
Finished restore at 24-NOV-20

RMAN>




```