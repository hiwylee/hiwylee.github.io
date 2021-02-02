## Real-time Migration with Oracle Goldengate Replication
#### 사용 환경
* OGG source : primary db /  Target DB : ADG  snapshot standby 활용
* OGG : Goldengate Microservice 
---
### 사전 준비 1:  ADG  snapshot standby 설정
* [참고문서](https://dbaclass.com/article/convert-physical-standby-to-snapshot-standby-database/)
* PHYSICAL STANDBY 확인

```sql
SQL> select database_role, open_mode from v$database;

DATABASE_ROLE    OPEN_MODE
---------------- --------------------
PHYSICAL STANDBY READ ONLY WITH APPLY

SQL>

```
* Cancel the recovery process:

```sql
SQL> alter database recover managed standby database cancel;

Database altered.
```

* **flashback mode enable** 설정 :

```sql
-- shutdown
SQL>
SQL> shutdown immediate;
Database closed.
Database dismounted.
ORACLE instance shut down.
SQL>

-- startup mount
SQL> startup mount;
ORACLE instance started.

Total System Global Area 6442449472 bytes
Fixed Size                  9148992 bytes
Variable Size            1090519040 bytes
Database Buffers         5318377472 bytes
Redo Buffers               24403968 bytes
SQL>
SQL> show parameter db_recovery_file_dest

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
db_recovery_file_dest                string      /u03/app/oracle/fast_recovery_area/
db_recovery_file_dest_size           big integer 251G
SQL>
SQL>  select flashback_on from v$database;

FLASHBACK_ON
------------------
NO


--  flashback on

SQL>  alter database recover managed standby database cancel;

Database altered.

SQL>
SQL>
SQL>
SQL>
SQL> alter database flashback on;

Database altered.

SQL>

```

* convert it to snapshot standby

```sql
SQL> select status from v$instance;

STATUS
------------
MOUNTED

SQL> alter database convert to snapshot standby;

Database altered.

SQL> alter database open;

Database altered.

SQL> select database_role, open_mode from v$database;

DATABASE_ROLE    OPEN_MODE
---------------- --------------------
SNAPSHOT STANDBY READ WRITE

SQL> select name, guarantee_flashback_database from v$restore_point;

NAME                                            GUA
----------------------------------------------- -------
SNAPSHOT_STANDBY_REQUIRED_02/02/2021 05:22:12   YES
```
* 접속정보 :

``` 
source (ORCL)         : 10.0.1.2  / 152.67.196.89   dbsty.sub01291310280.standbyvcn.oraclevcn.com  dbsty
target (ORCL_yny166)  : 10.0.0.2  / 152.67.197.86 primary.subnet1.primaryvcn.oraclevcn.com primary
```
---
### 사전 준비 2 :  SOurce DB RESTORE POINT
* primary database : **CREATE RESTORE POINT** (테스트 후 primy 로 원래 상태로)
 * [Guarantee Restore Point tips ](http://www.dba-oracle.com/t_flashback_guaranteed_restore_point.htm)
```sql
SQL> CREATE RESTORE POINT before_ogg GUARANTEE FLASHBACK DATABASE;

Restore point created.

SQL> col name format a20
SQL> col time format a33

SQL>
Wrote file afiedt.buf

  1  SELECT NAME, SCN, TIME, DATABASE_INCARNATION#,
  2         GUARANTEE_FLASHBACK_DATABASE,STORAGE_SIZE
  3*   FROM V$RESTORE_POINT
SQL> /
NAME                        SCN TIME                              DATABASE_INCARNATION# GUA STORAGE_SIZE
-------------------- ---------- --------------------------------- --------------------- --- ------------
BEFORE_OGG              3594066 02-FEB-21 05.40.25.000000000 AM                       4 YES   1073741824

SQL>

```
--- 
### Real-time Migration with Oracle Goldengate Replication
* source/target : nomarl DBCS  
  * [참조문서](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=756&p210_type=3&session=7583365448709)
  * ![](https://oracle.github.io/learning-library/solutions-library/exacs-mdw/golden-gate/images/gg_arch.png)
  
----
### STEP 1: Provision a Goldengate Microservice from OCI Marketplace

### STEP 2: Configure the Source Database

* source 설정 script - ogg amdin & 환경설정

```sql
create user C##user01 identified by WElcome_123#;
grant connect, resource, dba to c##user01;
alter database add supplemental log data;
exec dbms_goldengate_auth.grant_admin_privilege('C##user01', container=>'all');
alter system set ENABLE_GOLDENGATE_REPLICATION=true scope=both;
```

```sql
[oracle@primary ogg]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Tue Feb 2 07:57:20 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

SQL> create user C##user01 identified by WElcome_123#;

User created.

SQL> grant connect, resource , dba to c##user01;

Grant succeeded.

SQL> alter database add supplemental log data;

Database altered.

SQL> exec dbms_goldengate_auth.grant_admin_privilege('C##user01', container=>'all');

PL/SQL procedure successfully completed.

SQL> alter system set enable_goldengate_replication=true scope=both;

System altered.

SQL> show parameter ENABLE_GOLDENGATE_REPLICATION;

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
enable_goldengate_replication        boolean     TRUE
SQL>

```

*  create a schema user:  appschema in PDB 
   * scripts

```sql
alter session set container=orclpdb;
create user appschema identified by WElcome_123# default tablespace users;
grant connect, resource, dba to appschema;
CREATE TABLE appschema.COMMENTS
   (  "COMMENT_ID" NUMBER(10,0),
  "ITEM_ID" NUMBER(10,0),
  "COMMENT_BY" NUMBER(10,0),
  "COMMENT_CREATE_DATE" DATE DEFAULT sysdate,
  "COMMENT_TEXT" VARCHAR2(500)
   ) ;
alter user appschema quota unlimited on users;
```

### STEP 3: Configure the Target Database
* Target 설정 script - ogg amdin & 환경설정

```sql
-- cr_user.sql
create user C##user01 identified by WElcome_123#;
grant connect, resource, dba to c##user01;
alter database add supplemental log data;
exec dbms_goldengate_auth.grant_admin_privilege('C##user01', container=>'all');
alter system set ENABLE_GOLDENGATE_REPLICATION=true scope=both;
```

```sql
[oracle@dbsty ogg]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Tue Feb 2 08:22:33 2021
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 19c EE High Perf Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

SQL> @cr_user

User created.

Grant succeeded.

Database altered.

PL/SQL procedure successfully completed.

System altered.


NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
enable_goldengate_replication        boolean     TRUE
SQL>

```
*  create a schema user:  appschema in PDB 
  * scripts

```sql
-- cr_app.sql
alter session set container=orclpdb;
create user appschema identified by WElcome_123# default tablespace users;
grant connect, resource, dba to appschema;
CREATE TABLE appschema.COMMENTS
   (  "COMMENT_ID" NUMBER(10,0),
  "ITEM_ID" NUMBER(10,0),
  "COMMENT_BY" NUMBER(10,0),
  "COMMENT_CREATE_DATE" DATE DEFAULT sysdate,
  "COMMENT_TEXT" VARCHAR2(500)
   ) ;
alter user appschema quota unlimited on users;
```

```sql
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 ORCLPDB                        READ WRITE NO
SQL> @cr_app

Session altered.

User created.

Grant succeeded.

Table created.

User altered.
```

### STEP 4: Configure Goldengate Service
* OGG Deployment name : **Databases**

* /etc/hosts
```bash
# source DB
152.67.197.86 primary.subnet1.primaryvcn.oraclevcn.com         primary
# target DB
152.67.196.89   dbsty.sub01291310280.standbyvcn.oraclevcn.com  dbsty

```
* tnsmames.ora 설정 : /u02/deployments/[Deployment name]/etc

```
-bash-4.2$ cd /u02/deployments/Databases/etc
-bash-4.2$ cat tnsnames.ora

cdb_source =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = primary)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = ORCL)
    )
  )

pdb_source =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = primary)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = orclpdb)
    )
  )

cdb_target =
 (DESCRIPTION =
     (SDU=65536)
     (RECV_BUF_SIZE=134217728)
     (SEND_BUF_SIZE=134217728)
     (ADDRESS_LIST =
     (ADDRESS = (PROTOCOL = TCP)(HOST = dbsty)(PORT = 1521))
     )
     (CONNECT_DATA =
        (SERVER = DEDICATED)
        (SERVICE_NAME = ORCL_yny166)
        (UR=A)
     )
  )


pdb_target =
 (DESCRIPTION =
     (SDU=65536)
     (RECV_BUF_SIZE=134217728)
     (SEND_BUF_SIZE=134217728)
     (ADDRESS_LIST =
     (ADDRESS = (PROTOCOL = TCP)(HOST = dbsty)(PORT = 1521))
     )
     (CONNECT_DATA =
        (SERVER = DEDICATED)
        (SERVICE_NAME = orclpdb)
        (UR=A)
     )
  )

```
* sqlnet.ora

```
WALLET_LOCATION = (SOURCE=(METHOD=FILE)(METHOD_DATA=(DIRECTORY="/u02/deployments/Databases/etc")))
```

* OGG 설정 
  * url :  [https://<ip_address_of_goldengate_image> ex) https://152.67.192.10](https://152.67.192.10)
  * id/password : opc home 아래 ogg-credentials.json 참조 
```
-bash-4.2$ cd
-bash-4.2$ cat ogg-credentials.json
{"username": "oggadmin", "credential": "EDJT7Hpk.Q2qNrN1"}
-
```
* **Administration Server	** Stop 후 Start 해야 위에서 변경한 내용(tnsnames.ora/sqlnet.ora)이 반영됨

#### OGG : Extract, Pump, Repica 설정
* stream pool size : [참고](https://www.oracle-scn.com/memory-requirement-for-oracle-goldengate-integrated-extract/)
```
 alter system set streams_pool_size=1G scope=both;

```
---
### 데이터베이스 원상 복구
* OGG Micro Service 종료.
  * stop extract/replica
---
#### 소스 원상 복구
* Source DB - flashback database to a restore point (**before_ogg**)
   * [Guarantee Restore Point tips ](http://www.dba-oracle.com/t_flashback_guaranteed_restore_point.htm)
 
 ```sql
 
 ```
 
#### 타겟 원상 복구

* [참고문서](https://dbaclass.com/article/convert-physical-standby-to-snapshot-standby-database/)

 ```sql
 
 ```
 
