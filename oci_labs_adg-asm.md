###  Oracle Database Hybrid Active Data Guard Workshop

### STEP 2 : Stnady DB - ASM
---
### Manually Delete the standby Database Created by Tooling
* list datafile to delete and create pfile

```sql
SQL> set heading off linesize 999 pagesize 0 feedback off trimspool on
SQL> select 'asmcmd rm '||name from v$datafile union all select 'asmcmd rm '||name from v$tempfile union all select 'asmcmd rm '||member from v$logfile;
asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/system.261.1063135085
asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/sysaux.262.1063135139
asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/undotbs1.263.1063135165
asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/system.265.1063135303
asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/sysaux.266.1063135303
asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/undotbs1.267.1063135303
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/system.276.1063136557
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/sysaux.271.1063136571
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/undotbs1.272.1063136583
asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/users.274.1063136535
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/users.275.1063136537
asmcmd rm +DATA/ORCL_YNY1ZH/TEMPFILE/temp.264.1063135255
asmcmd rm +DATA/ORCL_YNY1ZH/BA0FEC6E998B2498E0530300000A0303/TEMPFILE/temp.268.1063135343
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/TEMPFILE/temp.270.1063136605
asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_3.259.1063135221
asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_2.258.1063135221
asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_1.257.1063135221
SQL>
SQL> create pfile='/tmp/ORCL_yny1zh.pfile' from spfile;
SQL> exit;
Disconnected from Oracle Database 19c EE High Perf Release 19.0.0.0.0 - Production
Version 19.7.0.0.0
[oracle@dbstby .ssh]$
```
* collect the configuration of the database for future reference

``` sql
[oracle@dbstby ~]$ srvctl config database -d ORCL_yny1zh > /tmp/ORCL_yny1zh.config
[oracle@dbstby ~]$ cat /tmp/ORCL_yny1zh.config
Database unique name: ORCL_yny1zh
Database name: ORCL
Oracle home: /u01/app/oracle/product/19.0.0.0/dbhome_1
Oracle user: oracle
Spfile: +DATA/ORCL_YNY1ZH/PARAMETERFILE/spfile.269.1063135725
Password file:
Domain: sub01291310280.standbyvcn.oraclevcn.com
Start options: open
Stop options: immediate
Database role: PRIMARY
Management policy: AUTOMATIC
Server pools:
Disk Groups: RECO,DATA
Mount point paths:
Services:
Type: SINGLE
OSDBA group: dba
OSOPER group: dbaoper
Database instance: ORCL
Configured nodes: dbstby
CSS critical: no
CPU count: 0
Memory target: 0
Maximum memory: 0
Default network number for database services:
Database is administrator managed
```

* shutdown db 

```bash
[oracle@dbstby ~]$ srvctl stop database -d ORCL_yny1zh -o immediate
PRCC-1016 : ORCL_yny1zh was already stopped
[oracle@dbstby ~]$

```

* delete datafile

``` bash
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/system.261.1063135085
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/sysaux.262.1063135139
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/undotbs1.263.1063135165
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/system.265.1063135303
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/sysaux.266.1063135303
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/undotbs1.267.1063135303
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/system.276.1063136557
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/sysaux.271.1063136571
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/undotbs1.272.1063136583
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/users.274.1063136535
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/users.275.1063136537
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/TEMPFILE/temp.264.1063135255
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA0FEC6E998B2498E0530300000A0303/TEMPFILE/temp.268.1063135343
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/TEMPFILE/temp.270.1063136605
[oracle@dbstby .ssh]$ asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_3.259.1063135221
[oracle@dbstby .ssh]$ asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_2.258.1063135221
[oracle@dbstby .ssh]$ asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_1.257.1063135221

```

### Copy the Password File and wallet file to the standby
* Copy the Password File

```bash

[oracle@dbstby .ssh]$ scp oracle@primary:/u01/app/oracle/product/19c/dbhome_1/dbs/orapwORCL /tmp
orapwORCL   
```


```
```
* Switch to **grid** user, use asmcmd, replace ORCL_nrt1d4 with your standby db unique name, using capital letters in the directory names

```
[oracle@dbstby .ssh]$ exit
logout
[opc@dbstby .ssh]$ sudo su - grid
Last login: Sat Jan 30 07:02:15 UTC 2021
[grid@dbstby ~]$
[grid@dbstby ~]$ asmcmd
ASMCMD> pwcopy --dbuniquename ORCL_yny1zh -f /tmp/orapwORCL +DATA/ORCL_YNY1ZH/orapwORCL_yny1zh
copying /tmp/orapwORCL -> +DATA/ORCL_YNY1ZH/ORCL_YNY1ZH
ASMCMD-9453: failed to register password file as a CRS resource
ASMCMD>

```

* ASMCMD-9453: failed to register password file as a CRS resource then as the **oracle** user execute the following

```
[oracle@dbstby ~]$ id
uid=101(oracle) gid=1001(oinstall) groups=1001(oinstall),1002(dbaoper),1003(dba),1006(asmdba)
[oracle@dbstby ~]$ srvctl modify database -db ORCL_yny1zh -pwfile '+DATA/ORCL_yny1zh/orapwORCL_yny1zh'
[oracle@dbstby ~]$

```

* Verify the password file is registered correctly (as **oracle** user)

```
[oracle@dbstby ~]$ id
uid=101(oracle) gid=1001(oinstall) groups=1001(oinstall),1002(dbaoper),1003(dba),1006(asmdba)
[oracle@dbstby ~]$ srvctl config  database -db ORCL_yny1zh
Database unique name: ORCL_yny1zh
Database name: ORCL
Oracle home: /u01/app/oracle/product/19.0.0.0/dbhome_1
Oracle user: oracle
Spfile: +DATA/ORCL_YNY1ZH/PARAMETERFILE/spfile.269.1063135725
Password file: +DATA/ORCL_yny1zh/orapwORCL_yny1zh
Domain: sub01291310280.standbyvcn.oraclevcn.com
Start options: open
Stop options: immediate
Database role: PRIMARY
Management policy: AUTOMATIC
Server pools:
Disk Groups: RECO,DATA
Mount point paths:
Services:
Type: SINGLE
OSDBA group: dba
OSOPER group: dbaoper
Database instance: ORCL
Configured nodes: dbstby
CSS critical: no
CPU count: 0
Memory target: 0
Maximum memory: 0
Default network number for database services:
Database is administrator managed
[oracle@dbstby ~]$

```
### Copying the Wallet File  
* wallet localtion : $ORACLE_HOME/network/admin/sqlnet.ora 
```sql
## primary
  ENCRYPTION_WALLET_LOCATION =
    (SOURCE = (METHOD = FILE)
      (METHOD_DATA =
        (DIRECTORY = /u01/app/oracle/admin/ORCL/wallet)
      )
    )
 ```
  * primary : /u01/app/oracle/admin/ORCL/wallet
  * dbstby  : /opt/oracle/dcs/commonstore/wallets/tde/$ORACLE_UNQNAME

```bash
[oracle@dbstby ~]$ scp primary:/u01/app/oracle/admin/ORCL/wallet/ewallet.p12 /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny1zh/
ewallet.p12                                                                       100% 5467     1.6MB/s   00:00
[oracle@dbstby ~]$ scp primary:/u01/app/oracle/admin/ORCL/wallet/cwallet.sso  /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny1zh/
cwallet.sso                                                                        100% 5512     2.3MB/s   00:00
[oracle@dbstby ~]$ chmod 600 /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny1zh/*wallet*
[oracle@dbstby ~]$ ls -l  /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny1zh/*wallet*
-rw------- 1 oracle asmadmin 5512 Jan 30 07:27 /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny1zh/cwallet.sso
-rw------- 1 oracle asmadmin 5467 Jan 30 07:26 /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny1zh/ewallet.p12
-rw------- 1 oracle asmadmin 2555 Jan 29 19:40 /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny1zh/ewallet_2021012919401289_defaultTag.p12

```
### Configure Static Listeners

* primary 
```bash
[oracle@primary .ssh]$ cat $ORACLE_HOME/network/admin/listener.ora
# listener.ora Network Configuration File: /u01/app/oracle/product/19c/dbhome_1/network/admin/listener.ora
# Generated by Oracle configuration tools.

LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = primary.subnet1.primaryvcn.oraclevcn.com)(PORT = 1521))
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )

## ADDED
SID_LIST_LISTENER=
  (SID_LIST=
     (SID_DESC=
     (GLOBAL_DBNAME=ORCL)
     (ORACLE_HOME=/u01/app/oracle/product/19c/dbhome_1)
     (SID_NAME=ORCL)
     )
     (SID_DESC=
     (GLOBAL_DBNAME=ORCL_DGMGRL)
     (ORACLE_HOME=/u01/app/oracle/product/19c/dbhome_1)
     (SID_NAME=ORCL)
     )
  )
[oracle@primary .ssh]$ lsnrctl reload

LSNRCTL for Linux: Version 19.0.0.0.0 - Production on 30-JAN-2021 07:33:18

Copyright (c) 1991, 2019, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=primary.subnet1.primaryvcn.oraclevcn.com)(PORT=1521)))
The command completed successfully
[oracle@primary .ssh]$

```

* standby 
  * add following lines into $ORACLE_HOME/network/admin/listener.ora (**grid** user)

```
[oracle@dbstby ~]$ exit
logout
[opc@dbstby .ssh]$ sudo su - grid
Last login: Sat Jan 30 07:32:16 UTC 2021
[grid@dbstby ~]$ vi $ORACLE_HOME/network/admin/listener.ora

SID_LIST_LISTENER=
  (SID_LIST=
    (SID_DESC=
    (GLOBAL_DBNAME=ORCL_yny1zh)
    (ORACLE_HOME=/u01/app/19.0.0.0/grid)
    (SID_NAME=ORCL)
    )
    (SID_DESC=
    (GLOBAL_DBNAME=ORCL_yny1zh_DGMGRL)
    (ORACLE_HOME=/u01/app/19.0.0.0/grid)
    (SID_NAME=ORCL)
    )
 )
```
  * realod listener
```
[grid@dbstby ~]$ lsnrctl reload

LSNRCTL for Linux: Version 19.0.0.0.0 - Production on 30-JAN-2021 07:37:40

Copyright (c) 1991, 2019, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=IPC)(KEY=LISTENER)))
The command completed successfully
[grid@dbstby ~]$

```
  * Start the Standby database in mount state

```
[grid@dbstby ~]$ srvctl start database -db ORCL_yny1zh -startoption mount
[grid@dbstby ~]$
```
### TNS Entries for Redo Transport 
* vi $ORACLE_HOME/network/admin/tnsnames.ora
  * primary(**oracle** user)

```
[opc@primary .ssh]$ sudo su - oracle
Last login: Sat Jan 30 07:32:16 UTC 2021
[oracle@primary .ssh]$ vi $ORACLE_HOME/network/admin/tnsnames.ora

ORCL_yny1zh =
 (DESCRIPTION =
     (SDU=65536)
     (RECV_BUF_SIZE=134217728)
     (SEND_BUF_SIZE=134217728)
     (ADDRESS_LIST =
     (ADDRESS = (PROTOCOL = TCP)(HOST = dbstby)(PORT = 1521))
     )
     (CONNECT_DATA =
        (SERVER = DEDICATED)
        (SERVICE_NAME = ORCL_yny1zh)
        (UR=A)
     )
  )

```

  * standby(**oracle** user) 

``` 
[opc@dbstby .ssh]$ sudo su - oracle
Last login: Sat Jan 30 07:32:16 UTC 2021
[oracle@dbstby ~]$ vi $ORACLE_HOME/network/admin/tnsnames.ora

ORCL =
  (DESCRIPTION =
  (SDU=65536)
  (RECV_BUF_SIZE=134217728)
  (SEND_BUF_SIZE=134217728)
  (ADDRESS_LIST =
    (ADDRESS = (PROTOCOL = TCP)(HOST = primary)(PORT = 1521))
  )
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = ORCL)
      (UR=A)
    )
  )

```

* Set TCP socket size : /etc/sysctl.conf

```
net.core.rmem_max = 134217728 
net.core.wmem_max = 134217728
```
```
[opc@primary ~]$ sudo /sbin/sysctl -p
```

### Instantiate the Standby Database
* create pdb directory in ASM (os user : **grid**)

```
[grid@dbstby ~]$ id
uid=102(grid) gid=1001(oinstall) groups=1001(oinstall),1002(dbaoper),1004(asmadmin),1005(asmoper),1006(asmdba)
[grid@dbstby ~]$
[grid@dbstby ~]$ asmcmd
ASMCMD> ls
DATA/
RECO/
ASMCMD> mkdir DATA/ORCL_YNY1ZH/pdbseed
ASMCMD>  mkdir DATA/ORCL_YNY1ZH/orclpdb
ASMCMD>  mkdir DATA/ORCL_YNY1ZH/ONLINELOG
ASMCMD> exit
[grid@dbstby ~]$

```
* modify the db and log file name convert parameter (os user : **oracle **)

  * param.sql
```
ALTER SYSTEM SET db_file_name_convert='/u01/app/oracle/oradata/ORCL','+DATA/ORCL_YNY1ZH' scope=spfile;
ALTER SYSTEM SET db_create_online_log_dest_1='+RECO' scope=spfile;
ALTER SYSTEM SET log_file_name_convert='/u01/app/oracle/oradata/ORCL','+RECO/ORCL_YNY1ZH/ONLINELOG' scope=spfile;
ALTER SYSTEM SET db_domain='' scope=spfile;
```
  * set params
```
[opc@dbstby .ssh]$ sudo su - oracle
Last login: Sat Jan 30 08:02:18 UTC 2021
[oracle@dbstby ~]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Sat Jan 30 08:04:14 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c EE High Perf Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

SQL> @param

System altered.

System altered.

System altered.

System altered.

SQL> exit
Disconnected from Oracle Database 19c EE High Perf Release 19.0.0.0.0 - Production
Version 19.7.0.0.0
[oracle@dbstby ~]$
```

* Shutdown and connect RMAN / startup database nomount

```
[oracle@dbstby ~]$ srvctl stop database -d ORCL_yny1zh -o immediate;

```

```sql
[oracle@dbstby ~]$ rman target /

Recovery Manager: Release 19.0.0.0.0 - Production on Sat Jan 30 08:12:05 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

connected to target database (not started)

RMAN> startup nomount;

Oracle instance started

Total System Global Area    6442449472 bytes

Fixed Size                     9148992 bytes
Variable Size               1140850688 bytes
Database Buffers            5268045824 bytes
Redo Buffers                  24403968 bytes

RMAN>

```


* Restore control file from primary database

```
[oracle@dbstby ~]$ rman target /

Recovery Manager: Release 19.0.0.0.0 - Production on Sat Jan 30 08:25:35 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

connected to target database: ORCL (not mounted)

RMAN> restore standby controlfile from service 'ORCL';

Starting restore at 30-JAN-21
using target database control file instead of recovery catalog
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=29 device type=DISK

channel ORA_DISK_1: starting datafile backup set restore
channel ORA_DISK_1: using network backup set from service ORCL
channel ORA_DISK_1: restoring control file
channel ORA_DISK_1: restore complete, elapsed time: 00:00:04
output file name=+RECO/ORCL_YNY1ZH/CONTROLFILE/current.256.1063135219
Finished restore at 30-JAN-21

RMAN>

```

* startup mount

```
RMAN> alter database mount;

released channel: ORA_DISK_1
Statement processed

RMAN>

```

* restore database from primary database

```
RMAN> restore database from service 'ORCL' section size 5G;

Starting restore at 30-JAN-21
Starting implicit crosscheck backup at 30-JAN-21
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=186 device type=DISK
Crosschecked 1 objects
Finished implicit crosscheck backup at 30-JAN-21

Starting implicit crosscheck copy at 30-JAN-21
using channel ORA_DISK_1
Finished implicit crosscheck copy at 30-JAN-21

searching for all files in the recovery area
cataloging files...
cataloging done

List of Cataloged Files
=======================
File Name: +RECO/ORCL_YNY1ZH/ARCHIVELOG/2021_01_29/thread_1_seq_1.260.1063136415

using channel ORA_DISK_1

channel ORA_DISK_1: starting datafile backup set restore
channel ORA_DISK_1: using network backup set from service ORCL
channel ORA_DISK_1: specifying datafile(s) to restore from backup set
channel ORA_DISK_1: restoring datafile 00001 to +DATA/ORCL_YNY1ZH/system01.dbf
channel ORA_DISK_1: restoring section 1 of 1
channel ORA_DISK_1: restore complete, elapsed time: 00:00:17
channel ORA_DISK_1: starting datafile backup set restore
channel ORA_DISK_1: using network backup set from service ORCL
channel ORA_DISK_1: specifying datafile(s) to restore from backup set
channel ORA_DISK_1: restoring datafile 00003 to +DATA/ORCL_YNY1ZH/sysaux01.dbf
channel ORA_DISK_1: restoring section 1 of 1
...
...
channel ORA_DISK_1: restoring datafile 00012 to +DATA/ORCL_YNY1ZH/orclpdb/users01.dbf
channel ORA_DISK_1: restoring section 1 of 1
channel ORA_DISK_1: restore complete, elapsed time: 00:00:56
Finished restore at 30-JAN-21

RMAN>

```

* Shutdown   

```

RMAN> shutdown immediate;

database dismounted
Oracle instance shut down

RMAN>

```

* startup mount the database again

```
[oracle@dbstby ~]$ srvctl start database -d ORCL_yny1zh -o mount

```

* Clear all online and standby redo logs

```sql

SQL> set pagesize 0 feedback off linesize 120 trimspool on
SQL> select distinct 'alter database clear logfile group '||group#||';' from v$logfile;
alter database clear logfile group 1;
alter database clear logfile group 2;
alter database clear logfile group 3;
alter database clear logfile group 4;
alter database clear logfile group 5;
alter database clear logfile group 6;
alter database clear logfile group 7;
SQL>
SQL> alter database clear logfile group 1;
alter database clear logfile group 2;
alter database clear logfile group 3;
alter database clear logfile group 4;
alter database clear logfile group 5;
alter database clear logfile group 6;
alter database clear logfile group 7;

SQL>

```

### Configure Data Guard broker

* Configure Data Guard broker From primay side

```
show parameter dg_broker_config_file;
show parameter dg_broker_start;
alter system set dg_broker_start=true;
select pname from v$process where pname like 'DMON%';
```

* Configure Data Guard broker From standby side

```

SQL> show parameter dg_broker_config_file;

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
dg_broker_config_file1               string      /u01/app/oracle/product/19.0.0
                                                 .0/dbhome_1/dbs/dr1ORCL_yny1zh
                                                 .dat
dg_broker_config_file2               string      /u01/app/oracle/product/19.0.0
                                                 .0/dbhome_1/dbs/dr2ORCL_yny1zh
                                                 .dat
SQL> show parameter dg_broker_start;

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
dg_broker_start                      boolean     FALSE
SQL> alter system set dg_broker_start=true;

System altered.

SQL> select pname from v$process where pname like 'DMON%';

PNAME
-----
DMON
```

* Register the database via DGMGRL

```
DGMGRL> show configuration;

Configuration - adgconfig

  Protection Mode: MaxPerformance
  Members:
  orcl        - Primary database
    orcl_yny166 - Physical standby database

Fast-Start Failover:  Disabled

Configuration Status:
SUCCESS   (status updated 42 seconds ago)

Database "orcl_yny1zh" added
DGMGRL>

```

```
DGMGRL> show configuration;

Configuration - adgconfig

  Protection Mode: MaxPerformance
  Members:
  orcl        - Primary database
    orcl_yny166 - Physical standby database
    orcl_yny1zh - Physical standby database (disabled)
      ORA-16905: The member was not enabled yet.

Fast-Start Failover:  Disabled

Configuration Status:
SUCCESS   (status updated 44 seconds ago)

DGMGRL> enable database orcl_yny1zh;
Enabled.
DGMGRL>  show configuration;


Configuration - adgconfig

  Protection Mode: MaxPerformance
  Members:
  orcl        - Primary database
    orcl_yny166 - Physical standby database
    orcl_yny1zh - Physical standby database
      Error: ORA-16810: multiple errors or warnings detected for the member

Fast-Start Failover:  Disabled

Configuration Status:
ERROR   (status updated 35 seconds ago)

DGMGRL> DGMGRL>

```
* From cloud side, open the standby database as read only.

```sql
[oracle@dbstby ~]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Sat Jan 30 08:53:46 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c EE High Perf Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

SQL> select open_mode,database_role from v$database;

OPEN_MODE            DATABASE_ROLE
-------------------- ----------------
MOUNTED              PHYSICAL STANDBY

SQL> alter database open;

Database altered.

SQL> alter pluggable database orclpdb open;

Pluggable database altered.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 ORCLPDB                        READ ONLY  NO
SQL> select open_mode,database_role from v$database;

OPEN_MODE            DATABASE_ROLE
-------------------- ----------------
READ ONLY WITH APPLY PHYSICAL STANDBY

SQL>

```

* OPEN_MODE is READ ONLY, do following sql to chagnge  OPEN_MODE to  READ ONLY WITH APPLY  

```sql
SQL> alter database recover managed standby database cancel;

Database altered.

SQL> alter database recover managed standby database using current logfile disconnect;

Database altered.

SQL> select open_mode,database_role from v$database;

OPEN_MODE         DATABASE_ROLE
-------------------- ----------------
READ ONLY WITH APPLY PHYSICAL STANDBY
```

* check DGMGR Configuration Status:

```
DGMGRL> show configuration;

Configuration - adgconfig

  Protection Mode: MaxPerformance
  Members:
  orcl        - Primary database
    orcl_yny166 - Physical standby database
    orcl_yny1zh - Physical standby database

Fast-Start Failover:  Disabled

Configuration Status:
SUCCESS   (status updated 27 seconds ago)

DGMGRL>
```

* Check Lag

```
DGMGRL> show database ORCL_yny1zh;

Database - orcl_yny1zh

  Role:               PHYSICAL STANDBY
  Intended State:     APPLY-ON
  Transport Lag:      0 seconds (computed 7 seconds ago)
  Apply Lag:          0 seconds (computed 7 seconds ago)
  Average Apply Rate: 0 Byte/s
  Real Time Query:    ON
  Instance(s):
    ORCL

Database Status:
SUCCESS

DGMGRL>
```

### Test DML Redirection
* From the standby side : 
  * enable DML Redirection 
```
alter session enable adg_redirect_dml;
```

```
[oracle@dbstby ~]$  sqlplus testuser/testuser@dbstby:1521/orclpdb

SQL*Plus: Release 19.0.0.0.0 - Production on Sat Jan 30 09:04:29 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

Last Successful login time: Fri Jan 29 2021 17:18:12 +00:00

Connected to:
Oracle Database 19c EE High Perf Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

SQL> set timing on
SQL> insert into test values(2,'line2');
insert into test values(2,'line2')
            *
ERROR at line 1:
ORA-16000: database or pluggable database open for read-only access

Elapsed: 00:00:00.02

SQL> alter session enable adg_redirect_dml;

Session altered.

Elapsed: 00:00:00.00
```

* (속도가 엄청 느리다 : 기본 설정이 ASYNC/MaxPerformance 임.
```
SQL> insert into test values(2,'line2');

1 row created.

Elapsed: 00:00:18.74
SQL> commit;

Commit complete.

Elapsed: 00:00:09.85
SQL>

```
* Switch the redo transport mode and protection mode : redirect 성능향상을 위해서

* Before : ASYNC, MaxPerformance (INSERT 18초)

```
DGMGRL>  show database orcl_yny1zh LogXptMode;
  LogXptMode = 'ASYNC'
DGMGRL> show database orcl  LogXptMode;
  LogXptMode = 'ASYNC'
DGMGRL>
DGMGRL> show configuration;

Configuration - adgconfig

  Protection Mode: MaxPerformance
  Members:
  orcl        - Primary database
    orcl_yny166 - Physical standby database
    orcl_yny1zh - Physical standby database

Fast-Start Failover:  Disabled

Configuration Status:
SUCCESS   (status updated 30 seconds ago)

```
* Change : ASYNC, MaxPerformance (INSERT 18초) -> SYNC, MaxAvailability
```

DGMGRL> EDIT DATABASE orcl SET PROPERTY LogXptMode='SYNC';
Property "logxptmode" updated
DGMGRL> EDIT DATABASE orcl_yny1zh  SET PROPERTY LogXptMode='SYNC';
Property "logxptmode" updated
DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MAXAVAILABILITY;
Succeeded.
DGMGRL>

```
* AFTER :  SYNC/MaxAvailability

```DGMGRL> show database orcl_yny1zh LogXptMode;
  LogXptMode = 'SYNC'
DGMGRL>  show database orcl  LogXptMode;
  LogXptMode = 'ASYNC'  LogXptMode = 'SYNC'

DGMGRL>  show configuration;

Configuration - adgconfig

  Protection Mode: MaxAvailability
  Members:
  orcl        - Primary database
    orcl_yny166 - Physical standby database
    orcl_yny1zh - Physical standby database

Fast-Start Failover:  Disabled

Configuration Status:
SUCCESS   (status updated 15 seconds ago)

DGMGRL>
```
#### 속도 비교


*  ASYNC, MaxPerformance (INSERT 18초)

```sql

```
*  SYNC, MaxAvailability

```sql
SQL> insert into test values(3,'line3');

1 row created.

Elapsed: 00:00:00.87
SQL> commit;

Commit complete.

Elapsed: 00:00:01.04
SQL>
```
### Switchover to the standby

* validate the standby database to see if Ready For **Switchover is Yes**
```

DGMGRL> validate database orcl;

  Database Role:    Primary database

  Ready for Switchover:  Yes

  Managed by Clusterware:
    orcl:  NO
    Validating static connect identifier for the primary database orcl...
    The static connect identifier allows for a connection to database "orcl".

DGMGRL>  validate database orcl_yny1zh;

  Database Role:     Physical standby database
  Primary Database:  orcl

  Ready for Switchover:  Yes
  Ready for Failover:    Yes (Primary Running)

  Flashback Database Status:
    orcl       :  On
    orcl_yny1zh:  Off

  Managed by Clusterware:
    orcl       :  NO
    orcl_yny1zh:  YES
    Validating static connect identifier for the primary database orcl...
    The static connect identifier allows for a connection to database "orcl".

  Standby Apply-Related Information:
    Apply State:      Running
    Apply Lag:        9 seconds (computed 5 seconds ago)
    Apply Delay:      0 minutes


```
* Switch over to  standby : orcl_yny1zh

```
DGMGRL> switchover to orcl_yny1zh
Performing switchover NOW, please wait...
Operation requires a connection to database "orcl_yny1zh"
Connecting ...
Connected to "ORCL_yny1zh"
Connected as SYSDBA.
New primary database "orcl_yny1zh" is opening...
Operation requires start up of instance "ORCL" on database "orcl"
Starting instance "ORCL"...
Connected to an idle instance.
ORACLE instance started.
Connected to "ORCL"
Database mounted.
Database opened.
Connected to "ORCL"
Switchover succeeded, new primary is "orcl_yny1zh"
DGMGRL>


```

