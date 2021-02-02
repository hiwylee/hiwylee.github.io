## Real-time Migration with Oracle Goldengate Replication
#### 사용 환경
* OGG source : primary db /  Target DB : ADG  snapshot standby 활용
* OGG : Goldengate Microservice 

### 사전 준비:  ADG  snapshot standby 설정
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

### 환경 설정.
* primary database : ** CREATE RESTORE POINT** (테스트 후 primy 로 원래 상태로)
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
