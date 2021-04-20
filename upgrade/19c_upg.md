## Upgrade to Oracle Database 19c 
* [Live Labs Upgrade to Oracle Database 19c ](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=606&p210_type=3&session=114292430617317)
* [SQL TUNING SET 요약](https://m.blog.naver.com/qowndyd/221334359445)
* [How to Move a SQL Tuning Set from One Database to Another (Doc ID 751068.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=194405980567391&parent=EXTERNAL_SEARCH&sourceId=HOWTO&id=751068.1&_afrWindowMode=0&_adf.ctrl-state=199scbuynz_4) 
* [Moving SQL Tuning Set (STS) Accross Databases](https://taliphakanozturken.wordpress.com/2011/12/20/moving-sql-tuning-set-sts-accross-databases/)
 
### SQL Tuning Sets Capture and Preserve SQL

* Collect Statements from Cursor Cache: @/home/oracle/scripts/capture_awr.sql

```sql
-- -----------------------------------------------------------------------------------
-- File Name    : https://MikeDietrichDE.com/wp-content/scripts/12c/capture_awr.sql
-- Author       : Mike Dietrich
-- Description  : Capture SQL Statements from AWR into a SQL Tuning Set
-- Requirements : Access to the DBA role.
-- Call Syntax  : @capture_awr.sql
-- Last Modified: 31/05/2017
-- -----------------------------------------------------------------------------------

SET SERVEROUT ON
SET PAGESIZE 1000
SET LONG 2000000
SET LINESIZE 400

--
-- Drop the SQL Tuning SET if it exists
--

DECLARE

  sts_exists number;
  stmt_count number;
  cur sys_refcursor;
  begin_id   number;
  end_id     number;

BEGIN

  SELECT count(*)
  INTO   sts_exists
  FROM   DBA_SQLSET
  WHERE  rownum = 1 AND
         name = 'STS_CaptureAWR';

  IF sts_exists = 1 THEN
    SYS.DBMS_SQLTUNE.DROP_SQLSET(
       sqlset_name=>'STS_CaptureAWR'
       );
  ELSE
    DBMS_OUTPUT.PUT_LINE('SQL Tuning Set does not exist - will be created ...');
  END IF;


--
-- Create a SQL Tuning SET 'STS_CaptureCursorCache'
--

  SYS.DBMS_SQLTUNE.CREATE_SQLSET(
     sqlset_name=>'STS_CaptureAWR',
     description=>'Statements from AWR Before-Change'
     );

DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT;

SELECT min(snap_id)
INTO begin_id
FROM dba_hist_snapshot;


SELECT max(snap_id)
INTO end_id
FROM dba_hist_snapshot;

DBMS_OUTPUT.PUT_LINE('Snapshot Range between ' || begin_id || ' and ' || end_id || '.');

open cur for
  select value(p) from table(dbms_sqltune.select_workload_repository(
       begin_snap       => begin_id,
       end_snap         => end_id,
       basic_filter     => 'parsing_schema_name not in (''DBSNMP'',''SYS'',''ORACLE_OCM'',''LBACSYS'',''WMSYS'',''XDB'')',
       ranking_measure1 => 'elapsed_time',
       result_limit     => 5000,
       attribute_list   => 'ALL')) p;
  dbms_sqltune.load_sqlset('STS_CaptureAWR', cur);
close cur;

--
-- Display the amount of statements collected in the STS
--

SELECT statement_count
INTO stmt_count
FROM dba_sqlset
WHERE name = 'STS_CaptureAWR';

DBMS_OUTPUT.PUT_LINE('There are ' || stmt_count || ' SQL Statements in STS_CaptureAWR.');

--
-- If you need more details please use:
--
--    SELECT sql_text,cpu_time,elapsed_time, executions, buffer_gets
--      FROM dba_sqlset_statements
--      WHERE sqlset_name='STS_CaptureAWR';
--

END;
/

```
* Collect Statements from Cursor Cache: @/home/oracle/scripts/capture_cc.sql

```sql
-- -----------------------------------------------------------------------------------
-- File Name    : https://MikeDietrichDE.com/wp-content/scripts/12c/check_patches.sql
-- Author       : Mike Dietrich
-- Description  : Capture SQL Statements from Cursor Cache into a SQL Tuning Set
-- Requirements : Access to the DBA role.
-- Call Syntax  : @capture_cc.sql
-- Last Modified: 29/05/2017
-- -----------------------------------------------------------------------------------

SET SERVEROUT ON
SET PAGESIZE 1000
SET LONG 2000000
SET LINESIZE 400

--
-- Drop the SQL Tuning SET if it exists
--

DECLARE

  sts_exists number;
  stmt_count number;

BEGIN

  SELECT count(*)
  INTO   sts_exists
  FROM   DBA_SQLSET
  WHERE  rownum = 1 AND
         name = 'STS_CaptureCursorCache';

  IF sts_exists = 1 THEN
    SYS.DBMS_SQLTUNE.DROP_SQLSET(
       sqlset_name=>'STS_CaptureCursorCache'
       );
  ELSE
    DBMS_OUTPUT.PUT_LINE('SQL Tuning Set does not exist - will be created ...');
  END IF;


--
-- Create a SQL Tuning SET 'STS_CaptureCursorCache'
--

  SYS.DBMS_SQLTUNE.CREATE_SQLSET(
     sqlset_name=>'STS_CaptureCursorCache',
     description=>'Statements from Before-Change'
     );


--
-- Poll the Cursor Cache
-- time_limit: The total amount of time, in seconds, to execute
-- repeat_interval: The amount of time, in seconds, to pause between sampling
-- Adjust both settings based on needs
--

 DBMS_OUTPUT.PUT_LINE('Now polling the cursor cache for 240 seconds every 10 seconds ...');
 DBMS_OUTPUT.PUT_LINE('You will get back control in 4 minutes.');
 DBMS_OUTPUT.PUT_LINE('.');

 DBMS_SQLTUNE.CAPTURE_CURSOR_CACHE_SQLSET(
        sqlset_name => 'STS_CaptureCursorCache',
        time_limit => 240,
        repeat_interval => 10,
        capture_option => 'MERGE',
        capture_mode => DBMS_SQLTUNE.MODE_ACCUMULATE_STATS,
        basic_filter => 'parsing_schema_name not in (''DBSNMP'',''SYS'',''ORACLE_OCM'',''LBACSYS'',''XDB'',''WMSYS'')',
        sqlset_owner => NULL,
        recursive_sql => 'HAS_RECURSIVE_SQL');

--
-- Display the amount of statements collected in the STS
--

SELECT statement_count
INTO stmt_count
FROM dba_sqlset
WHERE name = 'STS_CaptureCursorCache';

DBMS_OUTPUT.PUT_LINE('There are now ' || stmt_count || ' SQL Statements in this STS.');

--
-- If you need more details please use:
--
--    SELECT sql_text,cpu_time,elapsed_time, executions, buffer_gets
--      FROM dba_sqlset_statements
--      WHERE sqlset_name='STS_CaptureCursorCache';
--

END;
/

```

* Optional - Export AWR
*
```sql
@?/rdbms/admin/awrextr.sql
```

### AutoUpgrade
* Prepare cfg

```bash
. upgr
cd /home/oracle/scripts
java -jar $OH19/rdbms/admin/autoupgrade.jar -create_sample_file config
vi /home/oracle/scripts/sample_config.cfg
mv /home/oracle/scripts/sample_config.cfg /home/oracle/scripts/UPGR.cfg
```
* Analyze Phase

```bash
. upgr
java -jar $OH19/rdbms/admin/autoupgrade.jar -config /home/oracle/scripts/UPGR.cfg -mode analyze
```
* Upgrade
 
```bash
java -jar $OH19/rdbms/admin/autoupgrade.jar -config /home/oracle/scripts/UPGR.cfg -mode deploy
```
* check 

```sql
sudo su - oracle
. upgr19
cd /home/oracle/scripts
sqlplus / as sysdba
```

### SQL Performance Analyzer
* Simulate the execution of all statements

```sql
-- -----------------------------------------------------------------------------------
-- File Name    : https://MikeDietrichDE.com/wp-content/scripts/12c/run_spa.sql
-- Author       : Mike Dietrich
-- Description  : Run SQL Performance Analyzer on a SQL Tuning Set
-- Requirements : Access to the DBA role.
-- Call Syntax  : @run_spa.sql
-- Last Modified: 20/06/2018
-- -----------------------------------------------------------------------------------

SET SERVEROUT ON
SET PAGESIZE 1000
SET LONG 2000000
SET LINESIZE 400

--
-- Check if SQL Tuning SET if it exists
--

DECLARE

  sts_exists number;
  sts_task   VARCHAR2(64);
  tname      VARCHAR2(100);
  spa_exists number;

BEGIN

  SELECT count(*)
  INTO   sts_exists
  FROM   DBA_SQLSET
  WHERE  rownum = 1 AND
         name = 'STS_CaptureAWR';

  IF sts_exists <> 1 THEN
    DBMS_OUTPUT.PUT_LINE('SQL Tuning Set does not exist - creating it ...');
    SYS.DBMS_SQLTUNE.CREATE_SQLSET(
     sqlset_name=>'STS_CaptureAWR',
     description=>'Statements from AWR Before-Change'
     );
  ELSE
    DBMS_OUTPUT.PUT_LINE('SQL Tuning Set does exist - will run SPA now ...');
  END IF;


  SELECT count(*)
  INTO   spa_exists
  FROM   DBA_ADVISOR_TASKS
  WHERE  rownum = 1 AND
         task_name = 'UPGRADE_TO_19C';

  IF spa_exists = 1 THEN
    SYS.DBMS_SQLPA.DROP_ANALYSIS_TASK(
       task_name=>'UPGRADE_TO_19C'
       );
  ELSE
    DBMS_OUTPUT.PUT_LINE('SQL Performance Analyzer Task does not exist - will be created ...');
  END IF;

--
-- Create a SPA Task and parameterize it
--


  tname := DBMS_SQLPA.CREATE_ANALYSIS_TASK(
            sqlset_name=>'STS_CaptureAWR',
            task_name=>'UPGRADE_TO_19C',
            description=>'Move to 19c');

--
-- Set Parameters for SPA Task
--

 DBMS_SQLPA.SET_ANALYSIS_TASK_PARAMETER(
     task_name => 'UPGRADE_TO_19C',
     parameter => 'workload_impact_threshold',
     value     => 2);
 DBMS_SQLPA.SET_ANALYSIS_TASK_PARAMETER(
     task_name => 'UPGRADE_TO_19C',
     parameter => 'sql_impact_threshold',
     value     => 2);

--
-- Convert STS information from 11.2.0.4
--

  DBMS_SQLPA.EXECUTE_ANALYSIS_TASK(
     task_name => 'UPGRADE_TO_19C',
     execution_name => 'EXEC_SPA_TASK_11204',
     execution_type => 'CONVERT SQLSET',
     execution_desc => 'Convert 11204 Workload');

--
-- Simulate execution of STS in 19c
--

  DBMS_SQLPA.EXECUTE_ANALYSIS_TASK(
     task_name => 'UPGRADE_TO_19C',
     execution_name => 'EXEC_SPA_TASK_19C',
     execution_type => 'TEST EXECUTE',
     execution_desc => 'Test 11204 Workload in 19c');

--
-- Compare performance before/after on CPU_TIME
--

   DBMS_SQLPA.EXECUTE_ANALYSIS_TASK(
     task_name => 'UPGRADE_TO_19C',
     execution_name => 'Compare 11204 to 19c CPU_TIME',
     execution_type => 'COMPARE PERFORMANCE',
     execution_params =>
       DBMS_ADVISOR.ARGLIST(
               'comparison_metric',
               'cpu_time',     -- or 'elapsed_time',
               'execution_name1','EXEC_SPA_TASK_11204',
               'execution_name2','EXEC_SPA_TASK_19C'),
     execution_desc => 'Compare 11204 to 19c CPU_TIME'
     );


END;
/

```
* Compare before/after

```sql
SET PAGESIZE 0
SET LINESIZE 1000
SET LONG 1000000
SET LONGCHUNKSIZE 1000000
SET TRIMSPOOL ON
SET TRIM ON

set echo on
column filename new_val filename
select 'compare_spa_runs_' || to_char(sysdate, 'yyyymmddhh24miss' ) || '.html' filename from dual;

spool &filename

set echo off
set feedback off

SELECT DBMS_SQLPA.report_analysis_task(
  'UPGRADE_TO_19C',
  'HTML',
  'ALL',
  'ALL'
  )
FROM   dual;

SPOOL OFF

```

### SQL Plan Management
