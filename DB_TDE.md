## oracle TDE 구성

* [Samples Usage ](https://semode.tistory.com/260)
### Enable TDE

* 
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

### Enable the Network Encryption

