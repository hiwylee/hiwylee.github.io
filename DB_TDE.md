## Oracle Database Hybrid Active Data Guard Workshop

* [Samples Usage ](https://semode.tistory.com/260)
* [Oracle Database Hybrid Active Data Guard Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=609&p210_type=3&session=12913666657648)
### Enable TDE

* wallet directory
```bash

sudo su - oracle

mkdir -p /u01/app/oracle/admin/ORCL/wallet
```
* sqlnet.ora
```
vi $ORACLE_HOME/network/admin/sqlnet.ora
...
 ENCRYPTION_WALLET_LOCATION =
    (SOURCE = (METHOD = FILE)
      (METHOD_DATA =
       (DIRECTORY = /u01/app/oracle/admin/ORCL/wallet)
      )
    )
```

* Connect to sqlplus as sysdba, create keystore.

```sql
[oracle@primary ~]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Fri Jan 29 12:13:57 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

SQL>  administer key management create keystore '/u01/app/oracle/admin/ORCL/wallet' identified by "Ora_DB4U"
SQL> /

keystore altered.

-- Open the keystore.
SQL>
SQL> administer key management set keystore open  identified by "Ora_DB4U" container=all
SQL> /

keystore altered.

-- Create master key.

SQL> administer key management set key identified by "Ora_DB4U" with backup using 'backup' container=all
SQL> /

keystore altered.

SQL>
-- Verify the keystore, 

SQL> select * from v$encryption_wallet
SQL> /

WRL_TYPE             WRL_PARAMETER                            STATUS                         WALLET_TYPE          WALLET_OR KEYSTORE FULLY_BAC     CON_ID
-------------------- ---------------------------------------- ------------------------------ -------------------- --------- -------- --------- ----------
FILE                 /u01/app/oracle/admin/ORCL/wallet/       OPEN                           PASSWORD             SINGLE    NONE     NO                 1
FILE                                                          OPEN                           PASSWORD             SINGLE    UNITED   NO                 2
FILE                                                          OPEN                           PASSWORD             SINGLE    UNITED   NO                 3

-- Make keystore autologin.
SQL> ed
Wrote file afiedt.buf

  1* administer key management create auto_login keystore from keystore '/u01/app/oracle/admin/ORCL/wallet/' identified by "Ora_DB4U"
SQL> /

keystore altered.

-- Reset wallet from PASSWORD to AUTOLOGIN mode.

SQL> administer key management set keystore close identified by "Ora_DB4U"
  2  /

keystore altered.

SQL>

-- Verify the keystore , the wallet is configure to autologin.
SQL> select * from v$encryption_wallet;

WRL_TYPE             WRL_PARAMETER                            STATUS                         WALLET_TYPE          WALLET_OR KEYSTORE FULLY_BAC     CON_ID
-------------------- ---------------------------------------- ------------------------------ -------------------- --------- -------- --------- ----------
FILE                 /u01/app/oracle/admin/ORCL/wallet/       OPEN                           AUTOLOGIN            SINGLE    NONE     NO                 1
FILE                                                          OPEN                           AUTOLOGIN            SINGLE    UNITED   NO                 2
FILE                                                          OPEN                           AUTOLOGIN            SINGLE    UNITED   NO                 3


```
### Encrypt the Data Files
#### encrypt the USERS tablespace in the pdb.
* Connect to the orclpdb, check the encrypt status of the tablespace.

```sql
SQL> alter session set container=orclpdb;

Session altered.

SQL>
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         3 ORCLPDB                        READ WRITE NO

```
*  encrypt the USERS tablespace online

```sql

SQL> select tablespace_name, encrypted from dba_tablespaces;

TABLESPACE_NAME                ENC
------------------------------ ---
SYSTEM                         NO
SYSAUX                         NO
UNDOTBS1                       NO
TEMP                           NO
USERS                          NO

SQL>


SQL> alter tablespace users encryption online encrypt;

Tablespace altered.


SQL> select tablespace_name, encrypted from dba_tablespaces;

TABLESPACE_NAME                ENC
------------------------------ ---
SYSTEM                         NO
SYSAUX                         NO
UNDOTBS1                       NO
TEMP                           NO
USERS                          YES

```


### Enable the Network Encryption

*

```sql

SQL>
SQL> connect / as sysdba
Connected.
SQL>  set linesize 120
SQL> col network_service_banner for a85
SQL> select i.network_service_banner from v$session_connect_info i, v$session s where s.sid=i.sid and s.serial# = i.serial# and s.username = 'SYS';

NETWORK_SERVICE_BANNER
-------------------------------------------------------------------------------------
Oracle Bequeath NT Protocol Adapter for Linux: Version 19.0.0.0.0 - Production
Authentication service for Linux: Version 19.0.0.0.0 - Production
Encryption service for Linux: Version 19.0.0.0.0 - Production
Crypto-checksumming service for Linux: Version 19.0.0.0.0 - Production


```
* Edit the sqlnet.ora file.

```
NAMES.DIRECTORY_PATH= (TNSNAMES, EZCONNECT)
## TDE
ENCRYPTION_WALLET_LOCATION =
    (SOURCE = (METHOD = FILE)
      (METHOD_DATA =
       (DIRECTORY = /u01/app/oracle/admin/ORCL/wallet)
      )
    )
## in-fligh encryption
SQLNET.ENCRYPTION_SERVER=REQUIRED
SQLNET.CRYPTO_CHECKSUM_SERVER=REQUIRED
SQLNET.ENCRYPTION_TYPES_SERVER=(AES256,AES192,AES128)
SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER=(SHA1)
SQLNET.ENCRYPTION_CLIENT=REQUIRED
SQLNET.CRYPTO_CHECKSUM_CLIENT=REQUIRED
SQLNET.ENCRYPTION_TYPES_CLIENT=(AES256,AES192,AES128)
SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT=(SHA1)

```

*  network service banner again, the network encryption is enable now

```sql
SQL>  select i.network_service_banner from v$session_connect_info i, v$session s where s.sid=i.sid and s.serial# = i.serial# and s.username = 'SYS';

NETWORK_SERVICE_BANNER
--------------------------------------------------------------------------------
Oracle Bequeath NT Protocol Adapter for Linux: Version 19.0.0.0.0 - Production
Authentication service for Linux: Version 19.0.0.0.0 - Production
Encryption service for Linux: Version 19.0.0.0.0 - Production
AES256 Encryption service adapter for Linux: Version 19.0.0.0.0 - Production
Crypto-checksumming service for Linux: Version 19.0.0.0.0 - Production
SHA1 Crypto-checksumming service adapter for Linux: Version 19.0.0.0.0 - Production

SQL>

```

### Enable Achivelog and Flashback

* Enable Achivelog

```sql
SQL>
SQL> archive log list;
Database log mode              No Archive Mode
Automatic archival             Disabled
Archive destination            /u01/app/oracle/product/19c/dbhome_1/dbs/arch
Oldest online log sequence     11
Current log sequence           13
SQL>
SQL> shutdown immediate;
Database closed.
Database dismounted.
ORACLE instance shut down.

SQL>
SQL> startup mount;
ORACLE instance started.

Total System Global Area 4647286504 bytes
Fixed Size                  9144040 bytes
Variable Size             855638016 bytes
Database Buffers         3774873600 bytes
Redo Buffers                7630848 bytes
Database mounted.
SQL> alter database archivelog;

Database altered.

SQL> !mkdir -p /u01/app/oracle/fra/ORCL

SQL> alter system set db_recovery_file_dest_size=10G scope=both sid='*';

System altered.

SQL> alter system set db_recovery_file_dest='/u01/app/oracle/fra/ORCL' scope=both sid='*';

System altered.

SQL>

```

* Enable Flashback

```sql

SQL>
SQL> alter database flashback on;

Database altered.

SQL> alter database open;
```

* Check  Achivelog and Flashback


```sql

SQL> archive log list;
Database log mode              Archive Mode
Automatic archival             Enabled
Archive destination            USE_DB_RECOVERY_FILE_DEST
Oldest online log sequence     11
Next log sequence to archive   13
Current log sequence           13
SQL>

```
* Enable force logging.

```sql

SQL> alter database force logging;

Database altered.

```

### Change Redo Log Size and Create Standby Log
* Check the status of the redo log

```sql

SQL> select group#, bytes, status from v$log;

    GROUP#      BYTES STATUS
---------- ---------- ----------------
         1  209715200 CURRENT
         2  209715200 INACTIVE
         3  209715200 INACTIVE
```
* Add 3 new redo log group.

```sql
SQL>  alter database add logfile group 4 '/u01/app/oracle/oradata/ORCL/redo04.log' size 1024M;

Database altered.

SQL> alter database add logfile group 5 '/u01/app/oracle/oradata/ORCL/redo05.log' size 1024M;

Database altered.

SQL> alter database add logfile group 6 '/u01/app/oracle/oradata/ORCL/redo06.log' size 1024M;

Database altered.

SQL> alter system switch logfile;

System altered.

SQL> alter system checkpoint;

System altered.

SQL> select group#, bytes, status from v$log;

    GROUP#      BYTES STATUS
---------- ---------- ----------------
         1  209715200 INACTIVE
         2  209715200 INACTIVE
         3  209715200 INACTIVE
         4 1073741824 CURRENT
         5 1073741824 UNUSED
         6 1073741824 UNUSED

6 rows selected.

SQL> alter database drop logfile group 1;

Database altered.

SQL>  alter database drop logfile group 2;

Database altered.

SQL>  alter database drop logfile group 3;

Database altered.

```
* Create 4 standby log group.

```sql

SQL> alter database add standby logfile thread 1 '/u01/app/oracle/oradata/ORCL/srl_redo01.log' size 1024M;

Database altered.

SQL> alter database add standby logfile thread 1 '/u01/app/oracle/oradata/ORCL/srl_redo02.log' size 1024M;

Database altered.

SQL> alter database add standby logfile thread 1 '/u01/app/oracle/oradata/ORCL/srl_redo03.log' size 1024M;

Database altered.

SQL> alter database add standby logfile thread 1 '/u01/app/oracle/oradata/ORCL/srl_redo04.log' size 1024M;

Database altered.

SQL> select group#,thread#,bytes from v$standby_log;

    GROUP#    THREAD#      BYTES
---------- ---------- ----------
         1          1 1073741824
         2          1 1073741824
         3          1 1073741824
         7          1 1073741824

SQL>
```
### Modify the Init Parameters for Best Practice
*

```sql
SQL>
SQL> alter system set standby_file_management=auto scope=both;

System altered.

SQL> alter system set db_lost_write_protect=typical scope=both;

System altered.

SQL>  alter system set fast_start_mttr_target=300 scope=both;

System altered.

```

