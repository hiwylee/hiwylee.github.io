## Real Application Testing (RAT) - SPA
* [Where to Find Information About Performance Related Features (Doc ID 1361401.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=370702162634348&parent=DOCUMENT&sourceId=1600574.1&id=1361401.1&_afrWindowMode=0&_adf.ctrl-state=62i5lkkl6_210#aref_section257)


#### SPA 

* [SQL Performance Analyzer in Oracle Database 11g Release 1](https://oracle-base.com/articles/11g/sql-performance-analyzer-11gr1)
---
#### SPA 주의 사항 
* Compares the performance of the statements in a tuning set before and after a database change
  * Database, operating system, or hardware upgrades.
  * Database, operating system, or hardware configuration changes.
  * Database initialization parameter changes.
  * Schema changes, such as adding indexes or materialized views.
  * Refreshing optimizer statistics.
  * Creating or changing SQL profiles.
* Unlike Database Replay, the SQL Performance Analyzer ***does not try and replicate the workload*** on the system. It just **plugs through each statement gathering performance statistics**.
---

## SQL Performance Analyzer Test
###  Steps
* Setting Up the Test
* Creating SQL Tuning Sets using the DBMS_SQLTUNE Package
* Running the SQL Performance Analyzer using the DBMS_SQLPA Package
* Creating SQL Tuning Sets using Enterprise Manager
* Running the SQL Performance Analyzer using Enterprise Manager
* Optimizer Upgrade Simulation
* Parameter Change
* Transferring SQL Tuning Sets

### Setting Up the Test

```sql
SQL> CREATE USER spa_test_user IDENTIFIED BY spa_test_user
  QUOTA UNLIMITED ON users;

SQL> GRANT CONNECT, CREATE TABLE TO spa_test_user;


SQL>  grant administer sql tuning set to spa_test_user;

Grant succeeded.

SQL> grant administer sql management object to spa_test_user;

Grant succeeded.

SQL>
SQL> grant advisor to spa_test_user;

Grant succeeded.



```
*  create a test table called MY_OBJECTS
```sql
SQL> CONN spa_test_user/spa_test_user@pdb
Connected.
SQL> CREATE TABLE my_objects AS
  SELECT * FROM all_objects;
Table created.

SQL> EXEC DBMS_STATS.gather_table_stats(USER, 'MY_OBJECTS', cascade => TRUE);  
PL/SQL procedure successfully completed.

SQL>
```
* "before" state

```sql
SQL> SELECT COUNT(*) FROM my_objects WHERE object_id <= 100;

  COUNT(*)
----------
         0

SQL> SELECT object_name FROM my_objects WHERE object_id = 100;

no rows selected

SQL> SELECT COUNT(*) FROM my_objects WHERE object_id <= 1000;

  COUNT(*)
----------
        17

SQL> SELECT object_name FROM my_objects WHERE object_id = 1000;

no rows selected

SQL> SELECT COUNT(*) FROM my_objects WHERE object_id BETWEEN 100 AND 1000;

  COUNT(*)
----------
        17

SQL>
```
### Creating SQL Tuning Sets using the DBMS_SQLTUNE Package
* 1). Create a SQL tuning set called spa_test_sqlset using the CREATE_SQLSET procedure

```sql
SQL> exec dbms_sqltune.create_sqlset(sqlset_name => 'spa_test_sqlset');

PL/SQL procedure successfully completed.

```
* 2). Retrieve a cursor and load into running set sing the LOAD_SQLSET procedure.

```sql
/*
GRANT SELECT ON V_$SQL TO SPA_TEST_USER;
GRANT SELECT ON V_$SQLAREA TO SPA_TEST_USER;
GRANT SELECT ON V_$SQLAREA_PLAN_HASH TO SPA_TEST_USER;
GRANT SELECT ON V_$SQLSTATS TO SPA_TEST_USER;
GRANT SELECT ON V_$SQL_BIND_CAPTURE TO SPA_TEST_USER;

GRANT SELECT ON GV_$SQL TO SPA_TEST_USER;
GRANT SELECT ON GV_$SQLAREA TO SPA_TEST_USER;
GRANT SELECT ON GV_$SQLAREA_PLAN_HASH TO SPA_TEST_USER;
GRANT SELECT ON GV_$SQLSTATS TO SPA_TEST_USER;
GRANT SELECT ON GV_$SQL_BIND_CAPTURE TO SPA_TEST_USER;
 
grant select any table to spa_test_user;

grant execute on dbms_sqlpa  to spa_test_user;
*/
--
-- ld_crs.sql
DECLARE
  l_cursor  DBMS_SQLTUNE.sqlset_cursor;
BEGIN
  OPEN l_cursor FOR
     SELECT VALUE(a)
     FROM   TABLE(
              DBMS_SQLTUNE.select_cursor_cache(
                basic_filter   => 'sql_text LIKE ''%my_objects%'' and parsing_schema_name = ''SPA_TEST_USER''',
                attribute_list => 'ALL')
            ) a;
                                               
 
  DBMS_SQLTUNE.load_sqlset(sqlset_name     => 'spa_test_sqlset',
                           populate_cursor => l_cursor);
END;
/
--
SQL> @ld_crs
DECLARE
*
ERROR at line 1:
ORA-13773: insufficient privileges to select data from the cursor cache
ORA-06512: at "SYS.DBMS_SQLTUNE", line 7467
ORA-06512: at "SYS.DBMS_SQLTUNE", line 5836
ORA-06512: at "SYS.DBMS_SQLTUNE_INTERNAL", line 16762
ORA-06512: at "SYS.DBMS_SQLTUNE", line 9109
ORA-06512: at "SYS.DBMS_SYS_ERROR", line 79
ORA-06512: at "SYS.DBMS_SQLTUNE", line 8508
ORA-06512: at line 1
ORA-06512: at "SYS.DBMS_SQLTUNE", line 9039
ORA-06512: at "SYS.DBMS_SQLTUNE_INTERNAL", line 16538
ORA-06512: at "SYS.DBMS_SQLTUNE_INTERNAL", line 16674
ORA-06512: at "SYS.DBMS_SQLTUNE", line 5801
ORA-06512: at "SYS.DBMS_SQLTUNE", line 7442
ORA-06512: at line 11


-- grant dba privilege to user to avoid errors
-- grant dba to spa_test_user;

SQL> @ld_crs

PL/SQL procedure successfully completed.

SQL>
 
```
* DBA_SQLSET_STATEMENTS view allows us to see which statements have been associated with the tuning set.

```sql
SQL> ed
Wrote file afiedt.buf

  1  select sql_text
  2    from dba_sqlset_statements
  3*  where sqlset_name = 'spa_test_sqlset'
SQL> /

SQL_TEXT
--------------------------------------------------------------------------------
DECLARE
  l_cursor  DBMS_SQLTUNE.sqlset_cursor;
BEGIN
  OPEN l_cursor FOR
     S

CREATE TABLE my_objects AS
  SELECT * FROM all_objects

SELECT object_name FROM my_objects WHERE object_id = 100
DECLARE

SQL_TEXT
--------------------------------------------------------------------------------
  l_cursor DBMS_SQLTUNE.sqlset_cursor;
begin
  OPEN l_cursor FOR


declare
  l_cursor DBMS_SQLTUNE.sqlset_cursor;
begin
  OPEN l_cursor FOR



SQL_TEXT
--------------------------------------------------------------------------------
 SELECT /*+ first_rows(1) */ sql_id, force_matching_signature, sql_text, cast(NU
SELECT object_name FROM my_objects WHERE object_id = 1000
SELECT COUNT(*) FROM my_objects WHERE object_id <= 1000
SELECT VALUE(A) FROM TABLE( DBMS_SQLTUNE.SELECT_CURSOR_CACHE( BASIC_FILTER => 's
SELECT COUNT(*) FROM my_objects WHERE object_id <= 100
SELECT VALUE(A) FROM TABLE ( DBMS_SQLTUNE.SELECT_CURSOR_CACHE( BASIC_FILTER => '
SELECT COUNT(*) FROM my_objects WHERE object_id BETWEEN 100 AND 1000

12 rows selected.

SQL>

```
### Running the SQL Performance Analyzer using the DBMS_SQLPA Package
* 1). Create an analysis task using the CREATE_ANALYSIS_TASK

```sql
SQL> VARIABLE v_task VARCHAR2(64);
EXEC :v_task :=  DBMS_SQLPA.create_analysis_task(sqlset_name => 'spa_test_sqlset');
SQL>
PL/SQL procedure successfully completed.

SQL>
SQL> print :v_task

V_TASK
--------------------------------------------------------------------------------
TASK_18

```
* use the EXECUTE_ANALYSIS_TASK procedure to execute the contents of the SQL tuning set against the current state of the database to gather information about the performance before any modifications are made

```sql
BEGIN
  DBMS_SQLPA.execute_analysis_task(
    task_name       => :v_task,
    execution_type  => 'test execute',
    execution_name  => 'before_change');
END;
/
```

* make a change

```sql
SQL> CREATE INDEX my_objects_index_01 ON my_objects(object_id);

Index created.
SQL> EXEC DBMS_STATS.gather_table_stats(USER, 'MY_OBJECTS', cascade => TRUE);

PL/SQL procedure successfully completed.

SQL>

```

* test the performance after the database change

```sql
BEGIN
  DBMS_SQLPA.execute_analysis_task(
    task_name       => :v_task,
    execution_type  => 'test execute',
    execution_name  => 'after_change');
END;
/
```

* run a comparison analysis task

```sql
BEGIN
  DBMS_SQLPA.execute_analysis_task(
    task_name        => :v_task,
    execution_type   => 'compare performance', 
    execution_params => dbms_advisor.arglist(
                          'execution_name1', 
                          'before_change', 
                          'execution_name2', 
                          'after_change')
    );
END;
/
```
* check out the comparison report using the REPORT_ANALYSIS_TASK function
```sql
SET PAGESIZE 0
SET LINESIZE 1000
SET LONG 1000000
SET LONGCHUNKSIZE 1000000
SET TRIMSPOOL ON
SET TRIM ON

SPOOL /tmp/execute_comparison_report.htm

SELECT DBMS_SQLPA.report_analysis_task(:v_task, 'HTML', 'ALL')
FROM   dual;

SPOOL OFF
```

### Optimizer Upgrade Simulation

```sql
```
### Transferring SQL Tuning Sets

* create the staging table using the CREATE_STGTAB_SQLSET procedure.

```sql
CONN sys/password@prod AS SYSDBA

BEGIN
  DBMS_SQLTUNE.create_stgtab_sqlset(table_name      => 'SQLSET_TAB',
                                    schema_name     => 'SPA_TEST_USER',
                                    tablespace_name => 'USERS');
END;
/

```
* use the PACK_STGTAB_SQLSET procedure to export SQL tuning set into the staging table

```sql

BEGIN
  DBMS_SQLTUNE.pack_stgtab_sqlset(sqlset_name          => 'SPA_TEST_SQLSET',
                                  sqlset_owner         => 'SPA_TEST_USER',
                                  staging_table_name   => 'SQLSET_TAB',
                                  staging_schema_owner => 'SPA_TEST_USER');
END;
/
```

* transferred to the test system using Datapump, Export/Import or via a database link

* SQL tuning set can be imported using the UNPACK_STGTAB_SQLSET procedure

```sql
BEGIN
  DBMS_SQLTUNE.unpack_stgtab_sqlset(sqlset_name          => '%',
                                    sqlset_owner         => 'SYS',
                                    replace              => TRUE,
                                    staging_table_name   => 'SQLSET_TAB',
                                    staging_schema_owner => 'SPA_TEST_USER');
END;
/
```
