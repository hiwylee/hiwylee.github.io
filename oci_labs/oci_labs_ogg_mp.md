## Real-time Migration with Oracle Goldengate Replication
#### 사용 환경
* OGG source : primary db /  Target DB : ADG  snapshot standby 활용
* OGG : Goldengate Microservice 

### 사전 준비:  ADG  snapshot standby 설정

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
