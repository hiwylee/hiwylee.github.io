## Oracle Database Hybrid Active Data Guard Workshop

* [Samples Usage ](https://semode.tistory.com/260)
* [Oracle Database Hybrid Active Data Guard Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=609&p210_type=3&session=12913666657648)
### STEP 1 : Primary DB
---
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
### [STEP 2 : Stnady DB - ASM](oci_labs_adg-asm.md)
### STEP 2 : Stanby DB - LVM
---
### Provision DBCS on OCI
* DBCS 프로비전한 후에 DB 삭제하고 standby 다시 생성
### Set connectivity between on-premise host and cloud host
* DB 노드간 Name Resolution Configure

```bash
## primay db
[opc@primary ~]$  sudo vi /etc/hosts
xxx.xxx.xxx.xxx dbstby.sub01291310280.standbyvcn.oraclevcn.com  dbstby
sudo yum -y install telnet
[opc@primary ~]$ telnet dbstby 1521
  Trying 158.101.136.61...
  Connected to 158.101.136.61.
  Escape character is '^]'.
  ^]

 telnet> q
  Connection closed.
[opc@primary ~]$  
## stdby db
sudo vi /etc/hosts
xxx.xxx.xxx.xxx primary.subnet1.primaryvcn.oraclevcn.com primary
[opc@dbsty ~]$ telnet primary 1521
Trying 152.67.197.86...
Connected to primary.
Escape character is '^]'.
^C^]
telnet>
q
Connection closed by foreign host.
[opc@dbsty ~]$

```

* primary :  oracle 계정에 ssh key pair 설정 (primary -> stdnby)
  * primay db 에서 key pair 생성후 pub key를 standby db 에 복사
```
oracle@primary ~]$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/oracle/.ssh/id_rsa):
Created directory '/home/oracle/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/oracle/.ssh/id_rsa.
Your public key has been saved in /home/oracle/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:sHuktidyWkix6EkAdUV8i26VPrvq081N3wKDkkbo+Cg oracle@primary
The key's randomart image is:
+---[RSA 2048]----+
|... .+o          |
|.  .  . .        |
|.   . .+ o       |
| . . ooo=        |
|  o o+.+S. .     |
| o o..++* . +    |
|  o .+=o.* o + . |
|  E oo=o+ o . o .|
|   ..=+=..     . |
+----[SHA256]-----+
[oracle@primary ~]$ cat .ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGvDLo5kRbFdRH8bji5wVRxBwv3i/0BjA39QvhPtPU KyYGBsO4lTeUifnk0F3D5lQI4V3ji+RCMIjkEifiqJsRagHN+Cf3qI9rz1liQZwo3Rqhh+ifxIJ+mu3G mHgDQALefesF8A4slCsN9DmwIhMA3obPPKyZLp3deZuKhSkKF6dTt1R3k/aTGMlx/Qq8O7RgNjvST8wA bPA74rb+eMqM1jin5rIuViq+Ld+h9HeQlSnS/6jmTmDsCusAmhM2H3V2f6+z1ssfWdf4FOvSS3yABZFl B+8h5roesTYU8pUwinaq+25OEinuhDtmc8Pi8OE+XkFe3xArtf4w+vmu3Hlh oracle@primary

```
* standby db 에 pubkey 내용 복사

```
vi .ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGvDLo5kRbFdRH8bji5wVRxBwv3i/0BjA39QvhPtPU KyYGBsO4lTeUifnk0F3D5lQI4V3ji+RCMIjkEifiqJsRagHN+Cf3qI9rz1liQZwo3Rqhh+ifxIJ+mu3G mHgDQALefesF8A4slCsN9DmwIhMA3obPPKyZLp3deZuKhSkKF6dTt1R3k/aTGMlx/Qq8O7RgNjvST8wA bPA74rb+eMqM1jin5rIuViq+Ld+h9HeQlSnS/6jmTmDsCusAmhM2H3V2f6+z1ssfWdf4FOvSS3yABZFl B+8h5roesTYU8pUwinaq+25OEinuhDtmc8Pi8OE+XkFe3xArtf4w+vmu3Hlh oracle@primary

chmod 600 .ssh/authorized_keys
```

* primay -> standby 로 바로 로그인이 되는 지 확인

```bash
[oracle@primary ~]$  ssh oracle@dbstby echo Test
The authenticity of host 'dbstby (152.67.196.89)' can't be established.
ECDSA key fingerprint is SHA256:Fvg5p58/+P8Z/ifDONK49WGzbf2J4Pj5MBg17XePkJU.
ECDSA key fingerprint is MD5:43:92:21:a4:e8:6d:05:0c:d7:f9:c0:26:3d:bd:a4:8d.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'dbstby,152.67.196.89' (ECDSA) to the list of known hosts.
Test

```
*  **stdnby에서도 똑같이  oracle 계정에 ssh key pair 설정 (stdnby -> primary ) **

### STEP 3 : Deploy Active Data Guard (with LVM)
---
### Manually Delete the standby Database Created by Tooling
* list datafile to delete and create pfile

```sql
SQL> set heading off linesize 999 pagesize 0 feedback off trimspool on
SQL> select 'rm '||name from v$datafile union all select 'rm '||name from v$tempfile union all select 'rm '||member from v$logfile;
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_system_j1848fgx_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_sysaux_j1848fg5_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_undotbs1_j1848fgs_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19ACD479CCF0662E0530804F40A7CBF/datafile/o1_mf_system_j1849fmg_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19ACD479CCF0662E0530804F40A7CBF/datafile/o1_mf_sysaux_j1848fg5_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_users_j184fpfz_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19ACD479CCF0662E0530804F40A7CBF/datafile/o1_mf_undotbs1_j1849y5n_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_system_j1849omv_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_sysaux_j1849x39_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_undotbs1_j18496kc_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_users_j184frt2_.dbf
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_temp_j184d5kp_.tmp
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19ACD479CCF0662E0530804F40A7CBF/datafile/o1_mf_temp_j184d8op_.tmp
rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_temp_j184do22_.tmp
rm /u03/app/oracle/redo/ORCL_YNY166/onlinelog/o1_mf_3_j184c2qk_.log
rm /u03/app/oracle/redo/ORCL_YNY166/onlinelog/o1_mf_2_j184c2o1_.log
rm /u03/app/oracle/redo/ORCL_YNY166/onlinelog/o1_mf_1_j184c2ln_.log
SQL> create pfile='/tmp/ORCL_yny166.pfile' from spfile;

```
*  shutdown db and delete datafile

```sql
SQL> shutdown immediate;
Database closed.
Database dismounted.
ORACLE instance shut down.
SQL>

```

```
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_system_j1848fgx_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_sysaux_j1848fg5_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_undotbs1_j1848fgs_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19ACD479CCF0662E0530804F40A7CBF/datafile/o1_mf_system_j1849fmg_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19ACD479CCF0662E0530804F40A7CBF/datafile/o1_mf_sysaux_j1848fg5_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_users_j184fpfz_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19ACD479CCF0662E0530804F40A7CBF/datafile/o1_mf_undotbs1_j1849y5n_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_system_j1849omv_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_sysaux_j1849x39_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_undotbs1_j18496kc_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_users_j184frt2_.dbf
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/datafile/o1_mf_temp_j184d5kp_.tmp
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19ACD479CCF0662E0530804F40A7CBF/datafile/o1_mf_temp_j184d8op_.tmp
[oracle@dbsty .ssh]$ rm /u02/app/oracle/oradata/ORCL_yny166/ORCL_YNY166/A19AF823ADF20D72E0530804F40A73FA/datafile/o1_mf_temp_j184do22_.tmp
[oracle@dbsty .ssh]$ rm /u03/app/oracle/redo/ORCL_YNY166/onlinelog/o1_mf_3_j184c2qk_.log
[oracle@dbsty .ssh]$ rm /u03/app/oracle/redo/ORCL_YNY166/onlinelog/o1_mf_2_j184c2o1_.log
[oracle@dbsty .ssh]$ rm /u03/app/oracle/redo/ORCL_YNY166/onlinelog/o1_mf_1_j184c2ln_.log

```


```
```
### Copy the Password File and wallet file to the standby
* Copy the Password File

```
[oracle@dbsty .ssh]$ scp oracle@primary:/u01/app/oracle/product/19c/dbhome_1/dbs/orapwORCL $ORACLE_HOME/dbs/
orapwORCL                                                       100% 2048     3.4MB/s   00:00
[oracle@dbsty .ssh]$

```
* copy wallet file from primary (/u01/app/oracle/admin/ORCL/wallet) to DIRECTORY=/opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny166

```
[oracle@dbsty .ssh]$ cat $ORACLE_HOME/network/admin/sqlnet.ora
# sqlnet.ora Network Configuration File: /u01/app/oracle/product/19.0.0/dbhome_1/network/admin/sqlnet.ora
# Generated by Oracle configuration tools.

NAMES.DIRECTORY_PATH= (TNSNAMES, ONAMES, HOSTNAME)

ENCRYPTION_WALLET_LOCATION=
 (SOURCE=
  (METHOD=FILE)
   (METHOD_DATA=
    (DIRECTORY=/opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny166)
   )
 )
SQLNET.ENCRYPTION_SERVER=REQUIRED
SQLNET.CRYPTO_CHECKSUM_SERVER=REQUIRED
SQLNET.ENCRYPTION_TYPES_SERVER=(AES256,AES192,AES128)
SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER=(SHA1)
SQLNET.ENCRYPTION_CLIENT=REQUIRED
SQLNET.CRYPTO_CHECKSUM_CLIENT=REQUIRED
SQLNET.ENCRYPTION_TYPES_CLIENT=(AES256,AES192,AES128)
SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT=(SHA1)
```
* copy file and correct file permission

```
[oracle@dbsty .ssh]$ scp oracle@primary:/u01/app/oracle/admin/ORCL/wallet/ewallet.p12 /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny166/
ewallet.p12                                                                                             100% 5467     8.1MB/s   00:00
[oracle@dbsty .ssh]$ scp oracle@primary:/u01/app/oracle/admin/ORCL/wallet/cwallet.sso /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny166/
cwallet.sso                                                                                             100% 5512     8.0MB/s   00:00
[oracle@dbsty .ssh]$ chmod 600 /opt/oracle/dcs/commonstore/wallets/tde/ORCL_yny166/*wallet*

```

### Configure Static Listeners
* primary db :; add listner

```
vi $ORACLE_HOME/network/admin/listener.ora
```


```
[oracle@primary ~]$ cat $ORACLE_HOME/network/admin/listener.ora
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

```

* 리스너 재기동
```
[oracle@primary ~]$ lsnrctl reload

LSNRCTL for Linux: Version 19.0.0.0.0 - Production on 29-JAN-2021 15:25:06

Copyright (c) 1991, 2019, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=primary.subnet1.primaryvcn.oraclevcn.com)(PORT=1521)))
The command completed successfully

```
* standby db


```
[oracle@dbsty .ssh]$ vi $ORACLE_HOME/network/admin/listener.ora
[oracle@dbsty .ssh]$ cat  $ORACLE_HOME/network/admin/listener.ora
# listener.ora Network Configuration File: /u01/app/oracle/product/19.0.0/dbhome_1/network/admin/listener.ora
# Generated by Oracle configuration tools.

LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = dbsty.sub01291310280.standbyvcn.oraclevcn.com)(PORT = 1521))
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )
## ADDED
SID_LIST_LISTENER=
  (SID_LIST=
     (SID_DESC=
     (GLOBAL_DBNAME=ORCL_yny166)
     (ORACLE_HOME=/u01/app/oracle/product/19.0.0/dbhome_1)
     (SID_NAME=ORCL)
     )
     (SID_DESC=
     (GLOBAL_DBNAME=ORCL_yny166_DGMGRL)
     (ORACLE_HOME=/u01/app/oracle/product/19.0.0/dbhome_1)
     (SID_NAME=ORCL)
     )
  )

```
* 리스너 재기동

```
[oracle@dbsty .ssh]$ lsnrctl reload

LSNRCTL for Linux: Version 19.0.0.0.0 - Production on 29-JAN-2021 15:26:28

Copyright (c) 1991, 2019, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=dbsty.sub01291310280.standbyvcn.oraclevcn.com)(PORT=1521)))
The command completed successfully
[oracle@dbsty .ssh]$

```
### TNS Entries for Redo Transport

* standby DB 마운트

```sql
[oracle@dbsty .ssh]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Fri Jan 29 15:29:11 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

Connected to an idle instance.

SQL> startup mount;
ORACLE instance started.

Total System Global Area 6442449472 bytes
Fixed Size                  9148992 bytes
Variable Size            1090519040 bytes
Database Buffers         5318377472 bytes
Redo Buffers               24403968 bytes
Database mounted.
SQL>

```

* primary  db

``` 
[oracle@primary ~]$ cat  $ORACLE_HOME/network/admin/tnsnames.ora
# tnsnames.ora Network Configuration File: /u01/app/oracle/product/19c/dbhome_1/network/admin/tnsnames.ora
# Generated by Oracle configuration tools.

LISTENER_ORCL =
  (ADDRESS = (PROTOCOL = TCP)(HOST = primary.subnet1.primaryvcn.oraclevcn.com)(PORT = 1521))


ORCL =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = primary.subnet1.primaryvcn.oraclevcn.com)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = ORCL)
    )
  )

orclpdb =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = primary)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = orclpdb)
    )
  )

## ADDED
ORCL_yny166 =
 (DESCRIPTION =
     (SDU=65536)
     (RECV_BUF_SIZE=134217728)
     (SEND_BUF_SIZE=134217728)
     (ADDRESS_LIST =
     (ADDRESS = (PROTOCOL = TCP)(HOST = dbsty.sub01291310280.standbyvcn.oraclevcn.com)(PORT = 1521))
     )
     (CONNECT_DATA =
        (SERVER = DEDICATED)
        (SERVICE_NAME = ORCL_yny166)
        (UR=A)
     )
  )

[oracle@primary ~]$

```
* standby db 
  * primary 용  tnsname 등록 : **두 DB 가 domain 이름이 다르면 DML Redirection시  에러가 발생하므로 사용하지 않는다**

``` 
[oracle@dbsty .ssh]$ cat $ORACLE_HOME/network/admin/tnsnames.ora
# tnsnames.ora Network Configuration File: /u01/app/oracle/product/19.0.0/dbhome_1/network/admin/tnsnames.ora
# Generated by Oracle configuration tools.

ORCL_YNY166 =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = dbsty)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = ORCL_yny166)
    )
  )

 LISTENER_ORCL =
  (ADDRESS = (PROTOCOL = TCP)(HOST = dbstby)(PORT = 1521))

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

* Set TCP socket size, (opc user) and reload

```
[opc@dbsty .ssh]$ sudo vi /etc/sysctl.conf
net.core.rmem_max = 134217728 
net.core.wmem_max = 134217728
```

```
[opc@dbsty .ssh]$ sudo /sbin/sysctl -p
fs.file-max = 6815744
kernel.sem = 250 32000 100 128
kernel.shmmni = 4096
kernel.shmall = 1073741824
kernel.shmmax = 4398046511104
kernel.panic_on_oops = 1
net.core.rmem_default = 262144
net.core.wmem_default = 262144
net.ipv4.conf.all.rp_filter = 2
net.ipv4.conf.default.rp_filter = 2
fs.aio-max-nr = 1048576
net.ipv4.ip_local_port_range = 9000 65500
fs.suid_dumpable = 1
kernel.core_pattern = core.%e.%p
net.ipv4.conf.all.arp_announce = 2
net.ipv4.conf.all.arp_ignore = 1
net.ipv4.conf.all.arp_filter = 1
net.core.rmem_max = 134217728
net.core.wmem_max = 134217728
net.ipv4.tcp_rmem = 4096 87380 134217728
net.ipv4.tcp_wmem = 4096 65536 134217728
net.core.netdev_max_backlog = 300000
net.ipv4.tcp_moderate_rcvbuf = 1
sysctl: cannot stat /proc/sys/net/ipv6/conf/all/disable_ipv6: No such file or directory
sysctl: cannot stat /proc/sys/net/ipv6/conf/default/disable_ipv6: No such file or directory
vm.min_free_kbytes = 524288
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
kernel.pid_max = 99999
vm.nr_hugepages = 3226

```

### Instantiate the Standby Database

* 폴더생성

```
[oracle@dbsty ~]$ mkdir -p /u02/app/oracle/oradata/ORCL_yny166/pdbseed
[oracle@dbsty ~]$ mkdir -p /u02/app/oracle/oradata/ORCL_yny166/orclpdb
[oracle@dbsty ~]$ mkdir -p /u03/app/oracle/redo/ORCL_yny166/onlinelog

```

*  The different database domain name of the on-premise and cloud will cause DML Redirection error, in this lab, we **don't use the database domain**.

```sql
alter system set db_file_name_convert='/u01/app/oracle/oradata/ORCL','/u02/app/oracle/oradata/ORCL_yny166' scope=spfile;
alter system set db_create_online_log_dest_1='/u03/app/oracle/redo/ORCL_yny166/onlinelog' scope=spfile;
alter system set log_file_name_convert='/u01/app/oracle/oradata/ORCL','/u03/app/oracle/redo/ORCL_yny166/onlinelog' scope=spfile;
alter system set db_domain='' scope=spfile;
alter system set db_file_name_convert='/u01/app/oracle/oradata/ORCL','/u02/app/oracle/oradata/ORCL_yny166' scope=spfile;
alter system set db_create_online_log_dest_1='/u03/app/oracle/redo/ORCL_yny166/onlinelog' scope=spfile;
alter system set db_domain='' scope=spfile;
```

* Shutdown the database, connect with RMAN. Then startup database nomount.

```sql
SQL> shutdown immediate;
exit
ORA-01109: database not open


Database dismounted.
ORACLE instance shut down.
SQL> Disconnected from Oracle Database 19c EE High Perf Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

```

```sql
[oracle@dbsty ~]$ rman target /

Recovery Manager: Release 19.0.0.0.0 - Production on Fri Jan 29 16:05:23 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

connected to target database (not started)

RMAN> startup nomount;

Oracle instance started

Total System Global Area    6442449472 bytes

Fixed Size                     9148992 bytes
Variable Size               1090519040 bytes
Database Buffers            5318377472 bytes
Redo Buffers                  24403968 bytes
RMAN>
```

* Restore control file from on-premise database and mount the cloud database.

```sql
RMAN> restore standby controlfile from service 'ORCL';

Starting restore at 29-JAN-21
using target database control file instead of recovery catalog
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=181 device type=DISK

channel ORA_DISK_1: starting datafile backup set restore
channel ORA_DISK_1: using network backup set from service ORCL
channel ORA_DISK_1: restoring control file
channel ORA_DISK_1: restore complete, elapsed time: 00:00:02
output file name=/u02/app/oracle/oradata/ORCL_yny166/control01.ctl
output file name=/u03/app/oracle/fast_recovery_area/ORCL_YNY166/control02.ctl
Finished restore at 29-JAN-21
```

```
RMAN> alter database mount;

released channel: ORA_DISK_1
Statement processed

RMAN>
``` 

* restore database from on-premise database.

```sql

RMAN> restore database from service 'ORCL' section size 5G;

Starting restore at 29-JAN-21
Starting implicit crosscheck backup at 29-JAN-21
allocated channel: ORA_DISK_1
channel ORA_DISK_1: SID=181 device type=DISK
Crosschecked 1 objects
Finished implicit crosscheck backup at 29-JAN-21

Starting implicit crosscheck copy at 29-JAN-21
using channel ORA_DISK_1
Finished implicit crosscheck copy at 29-JAN-21

searching for all files in the recovery area
cataloging files...
cataloging done

List of Cataloged Files
=======================
File Name: /u03/app/oracle/fast_recovery_area/ORCL_YNY166/archivelog/2021_01_29/o1_mf_1_2_j184fn1w_.arc
File Name: /u03/app/oracle/fast_recovery_area/ORCL_YNY166/archivelog/2021_01_29/o1_mf_1_1_j184f1k6_.arc
File Name: /u03/app/oracle/fast_recovery_area/ORCL_YNY166/archivelog/2021_01_29/o1_mf_1_3_j184lf9l_.arc

using channel ORA_DISK_1

channel ORA_DISK_1: starting datafile backup set restore
channel ORA_DISK_1: using network backup set from service ORCL
channel ORA_DISK_1: specifying datafile(s) to restore from backup set
channel ORA_DISK_1: restoring datafile 00001 to /u02/app/oracle/oradata/ORCL_yny166/system01.dbf
channel ORA_DISK_1: restoring section 1 of 1
channel ORA_DISK_1: restore complete, elapsed time: 00:00:16
channel ORA_DISK_1: starting datafile backup set restore
channel ORA_DISK_1: using network backup set from service ORCL
channel ORA_DISK_1: specifying datafile(s) to restore from backup set
channel ORA_DISK_1: restoring datafile 00003 to /u02/app/oracle/oradata/ORCL_yny166/sysaux01.dbf
channel ORA_DISK_1: restoring section 1 of 1
...
...
...
channel ORA_DISK_1: restoring datafile 00012 to /u02/app/oracle/oradata/ORCL_yny166/orclpdb/users01.dbf
channel ORA_DISK_1: restoring section 1 of 1
channel ORA_DISK_1: restore complete, elapsed time: 00:00:01
Finished restore at 29-JAN-21

RMAN>

```

* Shutdown the database, connect to sqlplus as sysdba and mount the database again.

```sql

SQL> shutdown immediate;

database dismounted
Oracle instance shut down

```

```sql

[oracle@dbsty ~]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Fri Jan 29 16:13:17 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

Connected to an idle instance.

SQL> startup mount;
ORACLE instance started.

Total System Global Area 6442449472 bytes
Fixed Size                  9148992 bytes
Variable Size            1090519040 bytes
Database Buffers         5318377472 bytes
Redo Buffers               24403968 bytes
Database mounted.
SQL>

```
### Clear all online and standby redo logs
* 

```sql
SQL>   set pagesize 0 feedback off linesize 120 trimspool on
SQL>
SQL>   select distinct 'alter database clear logfile group '||group#||';' from v$logfile;
alter database clear logfile group 1;
alter database clear logfile group 2;
alter database clear logfile group 3;
alter database clear logfile group 4;
alter database clear logfile group 5;
alter database clear logfile group 6;
alter database clear logfile group 7;

```
### Configure Data Guard broker* 
* 아래 명령어를 primay/standby 양쪽에서 실행할 것

```sql
show parameter dg_broker_config_file;
show parameter dg_broker_start;
alter system set dg_broker_start=true;
select pname from v$process where pname like 'DMON%';
```
```sql
[oracle@primary ~]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Fri Jan 29 16:22:14 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

SQL> show parameter dg_broker_config_file;

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
dg_broker_config_file1               string      /u01/app/oracle/product/19c/db
                                                 home_1/dbs/dr1ORCL.dat
dg_broker_config_file2               string      /u01/app/oracle/product/19c/db
                                                 home_1/dbs/dr2ORCL.dat
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

* Register the database via DGMGRL. Replace ORCL_yny166 with your standby db unique name.' '

```
dgmgrl sys/Ora_DB4U@ORCL
CREATE CONFIGURATION adgconfig AS PRIMARY DATABASE IS ORCL CONNECT IDENTIFIER IS ORCL;
ADD DATABASE ORCL_yny166 AS CONNECT IDENTIFIER IS ORCL_yny166 MAINTAINED AS PHYSICAL;
enable configuration;
SHOW CONFIGURATION;
```

```sql
[oracle@dbsty ~]$ dgmgrl sys/Ora_DB4U@ORCL
DGMGRL for Linux: Release 19.0.0.0.0 - Production on Fri Jan 29 16:24:21 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

Welcome to DGMGRL, type "help" for information.
Connected to "ORCL"
Connected as SYSDBA.
DGMGRL> create configuration adgconfig as primary database is ORCL connect identifier is ORCL;
Configuration "adgconfig" created with primary database "orcl"
DGMGRL> ADD DATABASE ORCL_yny166 AS CONNECT IDENTIFIER IS ORCL_yny166 maintained as physical;
Database "orcl_yny166" added
DGMGRL> enable configuration;
Enabled.
DGMGRL> show configuration;

Configuration - adgconfig

  Protection Mode: MaxPerformance
  Members:
  orcl        - Primary database
    orcl_yny166 - Physical standby database
      Warning: ORA-16854: apply lag could not be determined

Fast-Start Failover:  Disabled

Configuration Status:
WARNING   (status updated 7 seconds ago)

DGMGRL>

```

* stadby remove 방법

```sql
DGMGRL> SHOW CONFIGURATION;

Configuration - adgconfig

  Protection Mode: MaxPerformance
  Members:
  orcl        - Primary database
    orcl_yny166 - Physical standby database (disabled)
      ORA-16795: the standby database needs to be re-created

Fast-Start Failover:  Disabled

Configuration Status:
SUCCESS   (status updated 56 seconds ago)

DGMGRL> disable database orcl_yny166;
Disabled.
DGMGRL> remove database orcl_yny166;
Removed database "orcl_yny166" from the configuration
DGMGRL> show configuration ;

Configuration - adgconfig

  Protection Mode: MaxPerformance
  Members:
  orcl - Primary database

Fast-Start Failover:  Disabled

Configuration Status:

```
----
### lag check

```sql

SQL> alter database recover managed standby database cancel;

Database altered.

SQL> alter database recover managed standby database using current logfile disconnect;

Database altered.

SQL> select open_mode,database_role from v$database;

OPEN_MODE         DATABASE_ROLE
-------------------- ----------------
READ ONLY WITH APPLY PHYSICAL STANDBY

SQL> ed dgstat.sql
set linesize 120;
column name format a25;
column value format a20;
column time_computed format a20;
column datum_time format a20;
select name, value, time_computed, datum_time from v$dataguard_stats;

SQL> @dgstat

NAME                      VALUE                TIME_COMPUTED        DATUM_TIME
------------------------- -------------------- -------------------- --------------------
transport lag             +00 00:00:00         01/29/2021 17:08:27  01/29/2021 17:08:27
apply lag                 +00 00:00:00         01/29/2021 17:08:27  01/29/2021 17:08:27
apply finish time         +00 00:00:00.000     01/29/2021 17:08:27
estimated startup time    15                   01/29/2021 17:08:27

SQL>

```

```sql
[oracle@dbstby ~]$ dgmgrl sys/Ora_DB4U@orcl
DGMGRL for Linux: Release 19.0.0.0.0 - Production on Sat Sep 5 07:25:52 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

Welcome to DGMGRL, type "help" for information.
Connected to "ORCL"
Connected as SYSDBA.
DGMGRL> show database orcl_yny166

Database - orcl_yny166

  Role:               PHYSICAL STANDBY
  Intended State:     APPLY-ON
  Transport Lag:      0 seconds (computed 1 second ago)
  Apply Lag:          0 seconds (computed 1 second ago)
  Average Apply Rate: 20.00 KByte/s
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
