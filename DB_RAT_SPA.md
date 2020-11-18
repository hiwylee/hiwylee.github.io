## Real Application Testing (RAT)
* [Where to Find Information About Performance Related Features (Doc ID 1361401.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=370702162634348&parent=DOCUMENT&sourceId=1600574.1&id=1361401.1&_afrWindowMode=0&_adf.ctrl-state=62i5lkkl6_210#aref_section257)


#### SPA
* [Document 455889.1](https://support.oracle.com/epmos/faces/DocumentDisplay?parent=DOCUMENT&sourceId=1361401.1&id=455889.1) SQL PERFORMANCE ANALYZER EXAMPLE
* [Document 562899.1](https://support.oracle.com/epmos/faces/DocumentDisplay?parent=DOCUMENT&sourceId=1361401.1&id=562899.1) Using SQL Performance Analyzer to Test SQL Performance Impact of 9i to 10gR2 Upgrade

### Real Application Testing: How to Run Workload Analyzer (Doc ID 1268920.1)	 
* [Doc ID 1268920.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=431505447515009&id=1268920.1&displayIndex=8&_afrWindowMode=0&_adf.ctrl-state=imgk5degr_176)


### Guide
* https://www.oracle.com/technetwork/articles/oem/298770-132432.pdf
* [Testing Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/ratug/testing-guide.pdf)

### Test SQL

#### 1. Sample Schema(SH) Install
* Guide : https://oracle-base.com/articles/misc/install-sample-schemas
* download samples : https://github.com/oracle/db-sample-schemas/releases

```sql
-- * replace "__SUB__CWD__
$ perl -p -i.bak -e 's#__SUB__CWD__#'$(pwd)'#g' *.sql */*.sql */*.dat

-- password policy -> simple
SQL> ALTER PROFILE DEFAULT LIMIT PASSWORD_VERIFY_FUNCTION NULL;

SQL> alter user system identified by welcome1;

User altered.
 
SQL>  alter user sys identified by welcome1;
User altered.

SQL> @mksample welcome1 welcome1  hr oe pm  ix sh bi EXAMPLE TEMP         $ORACLE_HOME/demo/schema/log/ xxx.dbsecsubnet.dbsecvcn.oraclevcn.com:1521/pdb.dbsecsubnet.dbsecvcn.oraclevcn.com

-- grant 
SQL> grant administer sql tuning set to sh;

SQL> grant administer sql management object to sh;

SQL> GRANT ADVISOR TO SH;

```

#### 2. 참고 문헌 
* [SQL TUNING SET](https://m.blog.naver.com/qowndyd/221334359445)
* [SQL Performance Analyzer Example (Doc ID 455889.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=199203154713329&id=455889.1&_afrWindowMode=0&_adf.ctrl-state=63tqt863a_347
)
#### 3. SPA 테스트
##### 1) Create the Sql Tuning Set (STS).
* Workload SQL

```sql
-- myworkload.sql

connect sh/sh

SELECT /*+ my_query */ p.prod_name, s.time_id, t.week_ending_day, SUM(s.amount_sold)
FROM sales s, products p, times t
WHERE s.time_id=t.time_id
AND s.prod_id = p.prod_id
GROUP BY p.prod_name, s.time_id, t.week_ending_day;

SELECT /*+ my_query */ p.prod_name, s.time_id, t.week_ending_day,
SUM(s.amount_sold)
FROM sales s, products p, times t
WHERE s.time_id=t.time_id
AND s.prod_id = p.prod_id
GROUP BY p.prod_name, s.time_id, t.week_ending_day;
SELECT /*+ my_query */ p.prod_category, t.week_ending_day, s.cust_id, SUM(s.amount_sold)
FROM sales s, products p, times t
WHERE s.time_id = t.time_id
AND s.prod_id = p.prod_id
AND p.prod_category = 'Photo'
GROUP BY p.prod_category, t.week_ending_day, s.cust_id;

SELECT /*+ my_query */ p.prod_subcategory_desc, t.week_ending_day, SUM(s.amount_sold)
FROM sales s, products p, times t
WHERE s.time_id = t.time_id
AND s.prod_id = p.prod_id
AND p.prod_subcategory_desc LIKE '%Audio'
GROUP BY p.prod_subcategory_desc, t.week_ending_day;
```
*  부하 발생.

```sql
sqlplus sh/sh@pdb

SQL*Plus: Release 19.0.0.0.0 - Production on Wed Nov 18 11:44:11 2020
Version 19.9.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

Last Successful login time: Wed Nov 18 2020 11:43:18 +09:00

Connected to:
Oracle Database 19c EE High Perf Release 19.0.0.0.0 - Production
Version 19.9.0.0.0

SQL> @myworkload
PROD_NAME                      TIME_ID   WEEK_ENDI SUM(S.AMOUNT_SOLD)
------------------------------ --------- --------- ------------------

Extension Cable                31-MAR-98 05-APR-98              319.6
5MP Telephoto Digital Camera   05-APR-98 05-APR-98           17404.26
Home Theatre Package with DVD- 07-JUN-98 07-JUN-98           17643.31
Audio/Video Play
.....
...

Home Audio                     15-JUL-01           42025.25
Home Audio                     02-SEP-01           13263.41

209 rows selected.

```


```sql

-- create_sts.sql
-- create my sql tuning set and populate it from the cursor cache

var sts_name varchar2(30);
exec :sts_name := 'small_sh_sts_4';
exec dbms_sqltune.drop_sqlset(:sts_name);
exec dbms_sqltune.create_sqlset(:sts_name, 'small demo workload to test SQLPA');

DECLARE
stscur dbms_sqltune.sqlset_cursor;
BEGIN

OPEN stscur FOR
SELECT VALUE(P)
FROM TABLE(dbms_sqltune.select_cursor_cache(
'sql_text like ''SELECT /*+ my_query%''',
null, null, null, null, null, null, 'ALL')) P;

-- populate the sqlset
dbms_sqltune.load_sqlset(:sts_name, stscur);

end;
/

```

```sql
SQL> @create_sts

PL/SQL procedure successfully completed.


PL/SQL procedure successfully completed.


PL/SQL procedure successfully completed.



PL/SQL procedure successfully completed.

SQL> SQL>

SQL> ed
Wrote file afiedt.buf

  1  select sql_id, plan_hash_value, buffer_gets, elapsed_time, substr(sql_text,1, 30
  2  ) text, executions
  3  from dba_sqlset_statements
  4  where sqlset_name = :sts_name
  5* order by sql_id, plan_hash_value
SQL> /

SQL_ID        PLAN_HASH_VALUE BUFFER_GETS ELAPSED_TIME TEXT                                     EXECUTIONS
------------- --------------- ----------- ------------ ---------------------------------------- ----------
4w2v9ug9vh5vp       248321137        6702       820913 SELECT /*+ my_query */ p.prod_                    4
8whxy4w69akgf      2083391562        8324       638282 SELECT /*+ my_query */ p.prod_                    5
ckm14c67njf0q      2422195864        6680      1086344 SELECT /*+ my_query */ p.prod_                    4
g37muqb81wjau      2422195864        6661       977383 SELECT /*+ my_query */ p.prod_                    4

SQL>

```

##### 2) Create a task to run Sql Performance Analyzer.
* create a task with a purpose of change impact analysis

```sql
create_sqlpa_task.sql
---create sql task
-- declare vars
var tname varchar2(30);
var sname varchar2(30);

-- init vars
exec :sname := 'small_sh_sts_4';
exec :tname := 'my_sqlpa_demo_task';

exec dbms_sqlpa.drop_analysis_task(task_name => :tname);

--
-- 1. create a task with a purpose of change impact analysis
------------------------------------------------------------
exec :tname := dbms_sqlpa.create_analysis_task(sqlset_name => :sname, -
task_name => :tname);

-- 2. check task status
---------------------------
SELECT task_name, status
FROM user_advisor_tasks
WHERE task_name = :tname;
```

```sql
SQL> @sqlpa_task.sql

PL/SQL procedure successfully completed.


PL/SQL procedure successfully completed.


PL/SQL procedure successfully completed.


PL/SQL procedure successfully completed.


TASK_NAME                      STATUS
------------------------------ -----------
my_sqlpa_demo_task             INITIAL

SQL>

```

##### 3) Execute Before Change TEST EXECUTE (Pre-Change SQL Trial).
```sql
--- beforechange.sql

--Now I am ready to run the Before Change Execute

begin
DBMS_SQLPA.EXECUTE_ANALYSIS_TASK(
task_name => 'my_sqlpa_demo_task',
execution_type => 'TEST EXECUTE',
execution_name => 'BEFORECHANGE');
end;
/

--Using a Database link
/*---------------------------
begin
DBMS_SQLPA.EXECUTE_ANALYSIS_TASK(
task_name => 'my_sqlpa_demo_task',
execution_type => 'TEST EXECUTE',
execution_name => 'BEFORECHANGE',
execution_params => dbms_advisor.arglist('DATABASE_LINK', '&dblink_name'));
end;
/
--------------------------------
*/
```

```sql
--We can check the status of this task.

select execution_name,status, execution_end
from DBA_ADVISOR_EXECUTIONS where task_name='my_sqlpa_demo_task';
```

##### Make a change that needs to tested.
* index invisiable

```sql
SQL> select index_name from user_indexes where INDEX_NAME like 'PRODUCT%';

INDEX_NAME
------------------------------
PRODUCTS_PK
PRODUCTS_PROD_CAT_IX
PRODUCTS_PROD_STATUS_BIX
PRODUCTS_PROD_SUBCAT_IX


SQL> ed
Wrote file afiedt.buf

  1* select 'alter index ' || index_name || ' INVISIBLE;' from user_indexes  where INDEX_NAME like 'PRODUCT%'
SQL> /

'ALTERINDEX'||INDEX_NAME||'INVISIBLE;'
-------------------------------------------------------------------------------------------------------------------------------------------------------
alter index PRODUCTS_PK INVISIBLE;
alter index PRODUCTS_PROD_CAT_IX INVISIBLE;
alter index PRODUCTS_PROD_STATUS_BIX INVISIBLE;
alter index PRODUCTS_PROD_SUBCAT_IX INVISIBLE;


SQL> alter index PRODUCTS_PK INVISIBLE;
alter index PRODUCTS_PROD_CAT_IX INVISIBLE;
alter index PRODUCTS_PROD_STATUS_BIX INVISIBLE;
alter index PRODUCTS_PROD_SUBCAT_IX INVISIBLE;

Index altered.

SQL>
Index altered.

SQL>
Index altered.

SQL>
Index altered.


```

##### 4) Execute After Change TEST EXECUTE (Post-Change SQL Trial).

```sql
-- afterchange.sql
begin
DBMS_SQLPA.EXECUTE_ANALYSIS_TASK(
task_name => 'my_sqlpa_demo_task',
execution_type => 'TEST EXECUTE',
execution_name => 'AFTERCHANGE');
end;
/
```
##### 5) Comparing SQL Trials.

```sql
--compare_runs.sql
begin
    DBMS_SQLPA.EXECUTE_ANALYSIS_TASK(
    task_name => 'my_sqlpa_demo_task',
    execution_type => 'COMPARE PERFORMANCE',
    execution_name => 'DEMOTASK',
    execution_params => dbms_advisor.arglist(
    'comparison_metric',
    'buffer_gets'));
end;
/
```
##### 6) Generate Compare report.

```sql
--report.sql
set long 100000 longchunksize 100000 linesize 200 head off feedback off echo off
spool report.html
SELECT dbms_sqlpa.report_analysis_task('my_sqlpa_demo_task', 'HTML', 'ALL','ALL') FROM dual;
spool off
```
---

####  [How to ``Load Queries into a SQL Tuning Set (STS)`` (Doc ID 1271343.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=250676624682144&parent=DOCUMENT&sourceId=455889.1&id=1271343.1&_afrWindowMode=0&_adf.ctrl-state=jskmkklw5_102)
###### 1. Create a SQL Tuning Set

```sql
EXEC dbms_sqltune.create_sqlset('mysts');
```
###### 2. Load SQL into the STS
* From Cursor Cache - To load a query with a specific sql_id

```sql
DECLARE
  cur sys_refcursor;
BEGIN
  open cur for
    select value(p) from table(dbms_sqltune.select_cursor_cache('sql_id = ''fgtq4z4vb0xx5''')) p;
    dbms_sqltune.load_sqlset('mysts', cur);
  close cur;
END;
/
```
* From Cursor Cache - To load queries with a specific query string and more than 1,000 buffer_gets

```sql
DECLARE
cur sys_refcursor;
BEGIN
    open cur for
        select value(p) from table(dbms_sqltune.select_cursor_cache('sql_text like ''%querystring%'' and buffer_gets > 1000')) p;
        dbms_sqltune.load_sqlset('mysts', cur);
    close cur;
END;
/
```
* From AWR Snapshots

```sql
-- 1) Find the two snapshots you want

select snap_id, begin_interval_time, end_interval_time from dba_hist_snapshot order by 1;

-- 2) To load all the queries between two snapshots

DECLARE
cur sys_refcursor;
BEGIN
    open cur for
        select value(p) from table(dbms_sqltune.select_workload_repository(begin_snap => 2245, end_snap => 2248)) p;
        dbms_sqltune.load_sqlset('mysts', cur);
    close cur;
END;
/

-- 3) To load a query with a specific sql_id and plan_hash_value

DECLARE
cur sys_refcursor;
BEGIN
    open cur for
        select value(p) from table(dbms_sqltune.select_workload_repository(begin_snap => 2245, end_snap => 2248, basic_filter => 'sql_id = ''fgtq4z4vb0xx5'' and plan_hash_value = 431456802')) p;
        dbms_sqltune.load_sqlset('mysts', cur);
    close cur;
END;
/
```

* From an AWR Baseline

```sql
-- 1) Find the baseline you want to load

select baseline_name, start_snap_id, end_snap_id from dba_hist_baseline;

-- 2) Load queries from the baseline

DECLARE
    cur sys_refcursor;
BEGIN
    open cur for
        select value(p) from table(dbms_sqltune.select_workload_repository('MY_BASELINE')) p;
        dbms_sqltune.load_sqlset('mysts', cur);
    close cur;
END;
/
```
* From another SQL Tuning Set

```sql
--1) Find the SQL Tuning Set you want to load

select name, owner, statement_count from dba_sqlset;

--2) Load queries from the SQL Tuning Set

DECLARE
    cur sys_refcursor;
BEGIN
    open cur for
        select value(p) from table(dbms_sqltune.select_sqlset(sqlset_name => 'HR_STS', sqlset_owner => 'HR', basic_filter => 'sql_text like ''%querystring%''')) p;
        dbms_sqltune.load_sqlset('mysts', cur);
    close cur;
END;
/

```
* From 10046 trace files (11g+)
  * 1)Loading into a SQL Tuning Set in the same database that it originated from

```sql

-- i. Create a directory object for the directory where the trace files are.

create directory my_dir as '/home/oracle/trace';
-- ii. Load the queries

DECLARE
    cur sys_refcursor;
BEGIN
    open cur for
        select value(p) from table(dbms_sqltune.select_sql_trace(directory=>'MY_DIR', file_name=>'%.trc')) p;
        dbms_sqltune.load_sqlset('mysts', cur);
    close cur;
END;
/
```
  * 2)Loading into a SQL Tuning Set in a different database

```sql

--- i. Create a mapping table from the database where the trace files were captured.

create table mapping as
    select object_id id, owner, substr(object_name, 1, 30) name
     from dba_objects
union all
    select user_id id, username owner, null name
     from dba_users;
 
--- ii. Copy the trace files into a directory of the target server and create a directory object for the directory. And import the mapping table into the target database.

create directory my_dir as '/home/oracle/trace';

--- iii. Specify the mapping table when loading the queries.


DECLARE
    cur sys_refcursor;
BEGIN
    open cur for
        select value(p) from table(dbms_sqltune.select_sql_trace(directory=>'MY_DIR', file_name=>'%.trc', mapping_table_name=> 'MAPPING', mapping_table_owner=> 'HR')) p;

        dbms_sqltune.load_sqlset('mysts', cur);
    close cur;
END;
/
 
```

##### [How to Move a SQL Tuning Set from One Database to Another (Doc ID 751068.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=252650877686625&parent=DOCUMENT&sourceId=1271343.1&id=751068.1&_afrWindowMode=0&_adf.ctrl-state=jskmkklw5_151)

* Create/load STS test_set owned by SYS
* Create stgtab SQLSET_TAB
* Pack test_set into the stgtab
* Export/import into test system, conn as scott
* Atempt to unpack an STS named 'testtarget_test_set'