## Active Data Guard using Data Guard Broker
* sys password
```sql
alter user sys identified by WelCome123##;

```
* firewall-cmd
```bash
[opc@workshop ~]$ sudo firewall-cmd --permanent --zone=public --add-port=1521/tcp
success
[opc@workshop ~]$ sudo firewall-cmd --reload
success
[opc@workshop ~]$ sudo firewall-cmd --permanent --zone=public --list-ports
1521/tcp


```
* https://oracle-base.com/articles/19c/data-guard-setup-using-broker-19c
```sh
"/tmp/initcdb1_stby.ora"

*.db_name='cdb1'
mkdir -p /u01/app/oracle/oradata/ORCL/pdbseed
mkdir -p /u01/app/oracle/oradata/ORCL/pdb1
mkdir -p /u01/app/oracle/fast_recovery_area/ORCL
mkdir -p /u01/app/oracle/admin/ORCL/adumpquit

orapwd file=/u01/app/oracle/product/19c/dbhome_1/dbs/orapwORCL password=WelCome123## entries=10

export ORACLE_SID=ORCL
[oracle@workshop2 admin]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Tue Sep 1 13:55:32 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

Connected to an idle instance.

SQL> startup nomount pfile='/tmp/initORCL_STBY.ora';
ORACLE instance started.

Total System Global Area  381677696 bytes
Fixed Size                  8896640 bytes
Variable Size             314572800 bytes
Database Buffers           50331648 bytes
Redo Buffers                7876608 bytes
SQL>

```
* Duplicate Database 
```bash
$ rman TARGET sys/WelCome123##@ORCL AUXILIARY sys/WelCome123##@ORCL_stby
```
```sql
RMAN> DUPLICATE TARGET DATABASE
  FOR STANDBY
  FROM ACTIVE DATABASE
  DORECOVER
  SPFILE
    SET db_unique_name='ORCL_STBY' COMMENT 'Is standby'
  NOFILENAMECHECK; 

Starting Duplicate Db at 01-SEP-20
using target database control file instead of recovery catalog
allocated channel: ORA_AUX_DISK_1
channel ORA_AUX_DISK_1: SID=528 device type=DISK
current log archived

contents of Memory Script:
{
   backup as copy reuse
   passwordfile auxiliary format  '/u01/app/oracle/product/19c/dbhome_1/dbs/orapwORCL'   ;
   restore clone from service  'ORCL' spfile to
 '/u01/app/oracle/product/19c/dbhome_1/dbs/spfileORCL.ora';
   sql clone "alter system set spfile= ''/u01/app/oracle/product/19c/dbhome_1/dbs/spfileORCL.ora''";
}
executing Memory Script

Starting backup at 01-SEP-20
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=11 device type=DISK
Finished backup at 01-SEP-20

Starting restore at 01-SEP-20
using channel ORA_AUX_DISK_1

channel ORA_AUX_DISK_1: starting datafile backup set restore
channel ORA_AUX_DISK_1: using network backup set from service ORCL
channel ORA_AUX_DISK_1: restoring SPFILE
output file name=/u01/app/oracle/product/19c/dbhome_1/dbs/spfileORCL.ora
channel ORA_AUX_DISK_1: restore complete, elapsed time: 00:00:01
Finished restore at 01-SEP-20

sql statement: alter system set spfile= ''/u01/app/oracle/product/19c/dbhome_1/dbs/spfileORCL.ora''

contents of Memory Script:
{
   sql clone "alter system set  db_unique_name =
 ''ORCL_STBY'' comment=
 ''Is standby'' scope=spfile";
   shutdown clone immediate;
   startup clone nomount;
}
executing Memory Script

sql statement: alter system set  db_unique_name =  ''ORCL_STBY'' comment= ''Is standby'' scope=spfile
Oracle instance shut down

connected to auxiliary database (not started)
Oracle instance started

Total System Global Area   10032774576 bytes

Fixed Size                    12684720 bytes
Variable Size               1543503872 bytes
Database Buffers            8455716864 bytes
Redo Buffers                  20869120 bytes
duplicating Online logs to Oracle Managed File (OMF) location

contents of Memory Script:
{
   restore clone from service  'ORCL' standby controlfile;
}
executing Memory Script

Starting restore at 01-SEP-20
allocated channel: ORA_AUX_DISK_1
channel ORA_AUX_DISK_1: SID=743 device type=DISK

channel ORA_AUX_DISK_1: starting datafile backup set restore
channel ORA_AUX_DISK_1: using network backup set from service ORCL
channel ORA_AUX_DISK_1: restoring control file
channel ORA_AUX_DISK_1: restore complete, elapsed time: 00:00:02
output file name=/u01/app/oracle/oradata/ORCL/control01.ctl
output file name=/u01/app/oracle/oradata/ORCL/control02.ctl
Finished restore at 01-SEP-20

contents of Memory Script:
{
   sql clone 'alter database mount standby database';
}
executing Memory Script

sql statement: alter database mount standby database
RMAN-05538: warning: implicitly using DB_FILE_NAME_CONVERT
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/system01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/sysaux01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/undotbs01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/pdbseed/system01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/pdbseed/sysaux01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/users01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/pdbseed/undotbs01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/orclpdb/system01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/orclpdb/sysaux01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/orclpdb/undotbs01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/orclpdb/users01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/orclpdb/tbs_auto_idx01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/pdb2/system01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/pdb2/sysaux01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/pdb2/undotbs01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/pdb3/system01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/pdb3/sysaux01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (datafile) file name /u01/app/oracle/oradata/ORCL/pdb3/undotbs01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (tempfile) file name /u01/app/oracle/oradata/ORCL/temp01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (tempfile) file name /u01/app/oracle/oradata/ORCL/pdbseed/temp012020-08-31_10-51-15-810-AM.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (tempfile) file name /u01/app/oracle/oradata/ORCL/orclpdb/temp01.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (tempfile) file name /u01/app/oracle/oradata/ORCL/pdb2/temp012020-08-31_10-51-15-810-AM.dbf conflicts with a file used by the target database
RMAN-05158: WARNING: auxiliary (tempfile) file name /u01/app/oracle/oradata/ORCL/pdb3/temp012020-08-31_10-51-15-810-AM.dbf conflicts with a file used by the target database

contents of Memory Script:
{
   set newname for tempfile  1 to
 "/u01/app/oracle/oradata/ORCL/temp01.dbf";
   set newname for tempfile  2 to
 "/u01/app/oracle/oradata/ORCL/pdbseed/temp012020-08-31_10-51-15-810-AM.dbf";
   set newname for tempfile  3 to
 "/u01/app/oracle/oradata/ORCL/orclpdb/temp01.dbf";
   set newname for tempfile  4 to
 "/u01/app/oracle/oradata/ORCL/pdb2/temp012020-08-31_10-51-15-810-AM.dbf";
   set newname for tempfile  5 to
 "/u01/app/oracle/oradata/ORCL/pdb3/temp012020-08-31_10-51-15-810-AM.dbf";
   switch clone tempfile all;
   set newname for datafile  1 to
 "/u01/app/oracle/oradata/ORCL/system01.dbf";
   set newname for datafile  3 to
 "/u01/app/oracle/oradata/ORCL/sysaux01.dbf";
   set newname for datafile  4 to
 "/u01/app/oracle/oradata/ORCL/undotbs01.dbf";
   set newname for datafile  5 to
 "/u01/app/oracle/oradata/ORCL/pdbseed/system01.dbf";
   set newname for datafile  6 to
 "/u01/app/oracle/oradata/ORCL/pdbseed/sysaux01.dbf";
   set newname for datafile  7 to
 "/u01/app/oracle/oradata/ORCL/users01.dbf";
   set newname for datafile  8 to
 "/u01/app/oracle/oradata/ORCL/pdbseed/undotbs01.dbf";
   set newname for datafile  9 to
 "/u01/app/oracle/oradata/ORCL/orclpdb/system01.dbf";
   set newname for datafile  10 to
 "/u01/app/oracle/oradata/ORCL/orclpdb/sysaux01.dbf";
   set newname for datafile  11 to
 "/u01/app/oracle/oradata/ORCL/orclpdb/undotbs01.dbf";
   set newname for datafile  12 to
 "/u01/app/oracle/oradata/ORCL/orclpdb/users01.dbf";
   set newname for datafile  13 to
 "/u01/app/oracle/oradata/ORCL/orclpdb/tbs_auto_idx01.dbf";
   set newname for datafile  14 to
 "/u01/app/oracle/oradata/ORCL/pdb2/system01.dbf";
   set newname for datafile  15 to
 "/u01/app/oracle/oradata/ORCL/pdb2/sysaux01.dbf";
   set newname for datafile  16 to
 "/u01/app/oracle/oradata/ORCL/pdb2/undotbs01.dbf";
   set newname for datafile  17 to
 "/u01/app/oracle/oradata/ORCL/pdb3/system01.dbf";
   set newname for datafile  18 to
 "/u01/app/oracle/oradata/ORCL/pdb3/sysaux01.dbf";
   set newname for datafile  19 to
 "/u01/app/oracle/oradata/ORCL/pdb3/undotbs01.dbf";
   restore
   from  nonsparse   from service
 'ORCL'   clone database
   ;
   sql 'alter system archive log current';
}
executing Memory Script

executing command: SET NEWNAME
...
executing command: SET NEWNAME

renamed tempfile 1 to /u01/app/oracle/oradata/ORCL/temp01.dbf in control file
renamed tempfile 2 to /u01/app/oracle/oradata/ORCL/pdbseed/temp012020-08-31_10-51-15-810-AM.dbf in control file
renamed tempfile 3 to /u01/app/oracle/oradata/ORCL/orclpdb/temp01.dbf in control file
renamed tempfile 4 to /u01/app/oracle/oradata/ORCL/pdb2/temp012020-08-31_10-51-15-810-AM.dbf in control file
renamed tempfile 5 to /u01/app/oracle/oradata/ORCL/pdb3/temp012020-08-31_10-51-15-810-AM.dbf in control file

executing command: SET NEWNAME
...
executing command: SET NEWNAME

Starting restore at 01-SEP-20
using channel ORA_AUX_DISK_1

channel ORA_AUX_DISK_1: starting archived log restore to default destination
channel ORA_AUX_DISK_1: using network backup set from service ORCL
channel ORA_AUX_DISK_1: restoring archived log
archived log thread=1 sequence=20
channel ORA_AUX_DISK_1: restore complete, elapsed time: 00:00:01
channel ORA_AUX_DISK_1: starting archived log restore to default destination
channel ORA_AUX_DISK_1: using network backup set from service ORCL
channel ORA_AUX_DISK_1: restoring archived log
archived log thread=1 sequence=21
channel ORA_AUX_DISK_1: restore complete, elapsed time: 00:00:02
Finished restore at 01-SEP-20

datafile 1 switched to datafile copy
input datafile copy RECID=4 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/system01.dbf
datafile 3 switched to datafile copy
input datafile copy RECID=5 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/sysaux01.dbf
datafile 4 switched to datafile copy
input datafile copy RECID=6 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/undotbs01.dbf
datafile 5 switched to datafile copy
input datafile copy RECID=7 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/pdbseed/system01.dbf
datafile 6 switched to datafile copy
input datafile copy RECID=8 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/pdbseed/sysaux01.dbf
datafile 7 switched to datafile copy
input datafile copy RECID=9 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/users01.dbf
datafile 8 switched to datafile copy
input datafile copy RECID=10 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/pdbseed/undotbs01.dbf
datafile 9 switched to datafile copy
input datafile copy RECID=11 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/orclpdb/system01.dbf
datafile 10 switched to datafile copy
input datafile copy RECID=12 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/orclpdb/sysaux01.dbf
datafile 11 switched to datafile copy
input datafile copy RECID=13 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/orclpdb/undotbs01.dbf
datafile 12 switched to datafile copy
input datafile copy RECID=14 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/orclpdb/users01.dbf
datafile 13 switched to datafile copy
input datafile copy RECID=15 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/orclpdb/tbs_auto_idx01.dbf
datafile 14 switched to datafile copy
input datafile copy RECID=16 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/pdb2/system01.dbf
datafile 15 switched to datafile copy
input datafile copy RECID=17 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/pdb2/sysaux01.dbf
datafile 16 switched to datafile copy
input datafile copy RECID=18 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/pdb2/undotbs01.dbf
datafile 17 switched to datafile copy
input datafile copy RECID=19 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/pdb3/system01.dbf
datafile 18 switched to datafile copy
input datafile copy RECID=20 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/pdb3/sysaux01.dbf
datafile 19 switched to datafile copy
input datafile copy RECID=21 STAMP=1049988207 file name=/u01/app/oracle/oradata/ORCL/pdb3/undotbs01.dbf

contents of Memory Script:
{
   set until scn  2672823;
   recover
   standby
   clone database
    delete archivelog
   ;
}
executing Memory Script

executing command: SET until clause

Starting recover at 01-SEP-20
using channel ORA_AUX_DISK_1

starting media recovery

archived log for thread 1 with sequence 20 is already on disk as file /u01/app/oracle/oradata/ORCL/ORCL_STBY/archivelog/2020_09_01/o1_mf_1_20_hnwsvdyb_.arc
archived log for thread 1 with sequence 21 is already on disk as file /u01/app/oracle/oradata/ORCL/ORCL_STBY/archivelog/2020_09_01/o1_mf_1_21_hnwsvg1p_.arc
archived log file name=/u01/app/oracle/oradata/ORCL/ORCL_STBY/archivelog/2020_09_01/o1_mf_1_20_hnwsvdyb_.arc thread=1 sequence=20
archived log file name=/u01/app/oracle/oradata/ORCL/ORCL_STBY/archivelog/2020_09_01/o1_mf_1_21_hnwsvg1p_.arc thread=1 sequence=21
media recovery complete, elapsed time: 00:00:01
Finished recover at 01-SEP-20

contents of Memory Script:
{
   delete clone force archivelog all;
}
executing Memory Script

released channel: ORA_DISK_1
released channel: ORA_AUX_DISK_1
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=873 device type=DISK
deleted archived log
archived log file name=/u01/app/oracle/oradata/ORCL/ORCL_STBY/archivelog/2020_09_01/o1_mf_1_20_hnwsvdyb_.arc RECID=1 STAMP=1049988204
deleted archived log
archived log file name=/u01/app/oracle/oradata/ORCL/ORCL_STBY/archivelog/2020_09_01/o1_mf_1_21_hnwsvg1p_.arc RECID=2 STAMP=1049988206
Deleted 2 objects

Finished Duplicate Db at 01-SEP-20


```
### Standby db open
```sql


SQL> startup nomount
ORACLE instance started.

Total System Global Area 1.0033E+10 bytes
Fixed Size                 12684720 bytes
Variable Size            1543503872 bytes
Database Buffers         8455716864 bytes
Redo Buffers               20869120 bytes
SQL> ALTER DATABASE MOUNT STANDBY DATABASE;

Database altered.

SQL> ALTER DATABASE OPEN READ ONLY;

Database altered.

SQL>

```
### ``Enable Broker``
* ``Enable Broker`` : primary / standby db
```sql

SQL> ALTER SYSTEM SET dg_broker_start=true;

System altered.

SQL>
```
*  register the primary server with the broker
```sql
SQL> ALTER SYSTEM SET dg_broker_start=true;

System altered.

SQL> Disconnected from Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.7.0.0.0
[oracle@workshop ~]$ dgmgrl sys/WelCome123##@ORCL
DGMGRL for Linux: Release 19.0.0.0.0 - Production on Tue Sep 1 15:30:05 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

Welcome to DGMGRL, type "help" for information.
Connected to "ORCL"
Connected as SYSDBA.
DGMGRL> CREATE CONFIGURATION my_dg_config AS PRIMARY DATABASE IS  ORCL  CONNECT IDENTIFIER IS ORCL;
Configuration "my_dg_config" created with primary database "orcl"
DGMGRL>
Configuration "my_dg_config" created with primary database "orcl"
```
* Now add the standby database.
```sql
DGMGRL> ADD DATABASE ORCL_STBY AS CONNECT IDENTIFIER IS ORCL_STBY  MAINTAINED AS PHYSICAL;
Database "orcl_stby" added


```
* we enable the new configuration.
```sql
DGMGRL> ENABLE CONFIGURATION;
Enabled.
DGMGRL>

```
*  check the configuration and status of the databases from the broker.
```sql

DGMGRL> SHOW CONFIGURATION;

Configuration - my_dg_config

  Protection Mode: MaxPerformance
  Members:
  orcl      - Primary database
    orcl_stby - Physical standby database
      Error: ORA-16810: multiple errors or warnings detected for the member

Fast-Start Failover:  Disabled

Configuration Status:
ERROR   (status updated 10 seconds ago)

DGMGRL>
DGMGRL> show database orcl

Database - orcl

  Role:               PRIMARY
  Intended State:     TRANSPORT-ON
  Instance(s):
    ORCL

Database Status:
SUCCESS

DGMGRL> show database orcl_stby

Database - orcl_stby

  Role:               PHYSICAL STANDBY
  Intended State:     APPLY-ON
  Transport Lag:      0 seconds (computed 0 seconds ago)
  Apply Lag:          0 seconds (computed 0 seconds ago)
  Average Apply Rate: 99.00 KByte/s
  Real Time Query:    ON
  Instance(s):
    ORCL

Database Status:
SUCCESS

DGMGRL>

```
* FAST_START FAILOVER : https://oracledbwr.com/oracle-19c-disable-fast-start-failover-in-dataguard-broker/
```sql
DGMGRL> SHOW FAST_START FAILOVER

Fast-Start Failover:  Disabled

  Protection Mode:    MaxPerformance
  Lag Limit:          30 seconds

  Threshold:          30 seconds
  Active Target:      (none)
  Potential Targets:  (none)
  Observer:           (none)
  Shutdown Primary:   TRUE
  Auto-reinstate:     TRUE
  Observer Reconnect: (none)
  Observer Override:  FALSE

Configurable Failover Conditions
  Health Conditions:
    Corrupted Controlfile          YES
    Corrupted Dictionary           YES
    Inaccessible Logfile            NO
    Stuck Archiver                  NO
    Datafile Write Errors          YES

  Oracle Error Conditions:
    (none)

DGMGRL>

```

### Database Switchover
* Switchover
```sql

```
* switch back to the original primary

```sql

```
* Reinstating a Failed Primary Database
  * Step 1   Restart the Old Primary Database.
```sql
SQL> startup nomount;
ORACLE instance started.

Total System Global Area 1.0033E+10 bytes
Fixed Size                 12684720 bytes
Variable Size            1543503872 bytes
Database Buffers         8455716864 bytes
Redo Buffers               20869120 bytes
SQL>

```
  * Step 2   Reinstate the old primary database.
```sql

DGMGRL> rsinstate database 'ORCL_STBY';
Unrecognized command "rsinstate", try "help"
DGMGRL> reinstate database 'ORCL_STBY';
Reinstating database "ORCL_STBY", please wait...

```  
  * Step 3   Show the Configuration and Databases.
```sql

```
* ``Check the CDB DATABASE ROLE``
```sql
 

select name, db_unique_name, database_role, open_mode from v$database;
```
### Flashback Database
### Read-Only Standby and Active Data Guard
### Snapshot Standby

