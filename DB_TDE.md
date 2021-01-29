## oracle TDE 구성

* [Samples Usage ](https://semode.tistory.com/260)
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
