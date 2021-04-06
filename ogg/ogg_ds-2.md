## GoldenGate Capture from a DataGuard with Cascaded Redo Logs
### Source RDBMS Configuration Steps

---
* source    : rac1.sh    (DB09021, db0902_yny19m, rac-scan.subnet1.labvcn.oraclevcn.com) 
* mining db : db19c.sh   (ORCL,ORCL)
* target    : primary.sh (ORCL) 
---

### 
* Enable Cascading Redo Log Shipping
* Create OGG Extract User
* Open SQL*Net Port
* Set LOG_ARCHIVE_CONFIG
  SQL> Alter system set LOG_ARCHIVE_CONFIG=’DG_CONFIG=(< Primary database DB_UNQUE_NAME>, <Standby database DB_UNIQUE_NAME>, <Mining database DB_UNIQUE_NAME>)’;
  
  ```sql
  SQL> Alter system set LOG_ARCHIVE_CONFIG=’DG_CONFIG=(SRC_01, STBY_02, MINING)’;
  ```
* Set LOG_ARCHIVE_DEST_3
  * SQL> Alter system set LOG_ARCHIVE_DEST_2=’SERVICE=<connect string for the mining database> ASYNC NOREGISTER VALID_FOR=(STANDBY_LOGFILES, STANDBY_ROLE) REOPEN=10 DB_UNIQUE_NAME=<db unique name of the mining server>’;

    ```sql
  * SQL> Alter system set LOG_ARCHIVE_DEST_3=’SERVICE=to_mining ASYNC NOREGISTER VALID_FOR=(STANDBY_LOGFILES, STANDBY_ROLE) REOPEN=10 DB_UNIQUE_NAME=mining’;
    ```

```sql
[opc@rac1 ~]$ sudo su - oracle
Last login: Tue Apr  6 09:44:35 UTC 2021 on pts/0
[oracle@rac1 ~]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Tue Apr 6 09:59:06 2021
Version 19.8.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c EE Extreme Perf Release 19.0.0.0.0 - Production
Version 19.8.0.0.0

SYS@DB09021> @param LOG_ARCH

no rows selected

Elapsed: 00:00:00.06
SYS@DB09021> show parameter LOG_ARCHIVE_CONFIG

NAME                                 TYPE                   VALUE
------------------------------------ ---------------------- ------------------------------
log_archive_config                   string

SYS@DB09021> alter system set log_archive_config='DG_CONFIG=(ORCL)';

System altered.

Elapsed: 00:00:00.52
SYS@DB09021> alter system set LOG_ARCHIVE_DEST_3='SERVICE=mining async NOREGISTER VALID_FOR=(STANDBY_LOGFILES, STANDBY_ROLE) REOPEN=10 DB_UNIQUE_NAME=ORCL';
System altered.

SYS@DB09021> alter database add supplemental log data;

Database altered.

Elapsed: 00:00:00.22
SYS@DB09021> create user c##ggadmin identified by ggadmin;

User created.

Elapsed: 00:00:00.37
SYS@DB09021> exec dbms_goldengate_auth.grant_admin_privilege('C##GGADMIN',container=>'ALL');

PL/SQL procedure successfully completed.

Elapsed: 00:00:08.60
SYS@DB09021> grant dba to c##ggadmin container=all;

Grant succeeded.

Elapsed: 00:00:00.03
SYS@DB09021> connect c##ggadmin/ggadmin;
Connected.
C##GGADMIN@DB09021>

```

* source tnsnames.ora

  ```bash
 mining =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = mining)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = ORCL)
    )
  )
 
  ```
  
