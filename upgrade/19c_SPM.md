## SQL Plan Management
* [Automatic SQL Plan Management in Oracle Database 19c](Automatic SQL Plan Management in Oracle Database 19c)

* [19c Database Self-Guided Upgrade with Best Practices (Doc ID 1919.2](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=9924793278331&parent=DOCUMENT&sourceId=1919.2&id=1919.2&_afrWindowMode=0&_adf.ctrl-state=159yujiz9m_45)

### 참조 자료
* 놀멍
  * [SPM(SQL PLAN MANAGEMENT) 사용 방법 #1](https://argolee.tistory.com/14?category=748261)
  * [SPM(SQL PLAN MANAGEMENT) 사용 방법 #2](https://argolee.tistory.com/15?category=748261)
### SQL Plan Management
* [Upgrade to Oracle Database 19c Workshop - LAB 9 ](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=606&p210_type=3&session=1561372510513)
  * Plan capture
  * Plan selection
  * Plan evolution

* Load and fixed

```sql

SET SERVEROUT ON
SET PAGESIZE 1000
SET LONG 2000000
SET LINESIZE 400


DECLARE

l_plans_loaded  PLS_INTEGER;

BEGIN

  l_plans_loaded := DBMS_SPM.load_plans_from_sqlset(
                       sqlset_name  => 'STS_CaptureCursorCache',
                       fixed        => 'YES',
                       enabled      => 'YES'
                       );

END;
/
```

```sql
SQL> SELECT sql_handle, plan_name, enabled, accepted FROM dba_sql_plan_baselines;
SQL_0c79b6d2c87ca446           SQL_PLAN_0sydqub47t926ee6188f4           YES YES
SQL_1465e6eba9245647           SQL_PLAN_18tg6xfnk8pk7f4091add           YES YES
SQL_1d3eb12408a63da1           SQL_PLAN_1ugpj4h4acgd12e067175           YES YES
SQL_2469648692a7cf75           SQL_PLAN_28ub4hu9agmvp341d91fc           YES YES
SQL_248d6d8dbf8dc7a0           SQL_PLAN_293bdjqzsvjx06e1fb41e           YES YES
SQL_2f304ba11a91bba2           SQL_PLAN_2yc2bn4d93fx23efd80e4           YES YES
SQL_3276f16ef07d6f11           SQL_PLAN_34xrjdvs7uvsj872680f9           YES YES
.....
SQL_fc5efaa8ffabe508           SQL_PLAN_gsrrup3zurt88e90e4d55           YES YES
```

#### ``플랜이 고정되는 것보다 변경되는 것이 보다 나은 성능을 내는 경우가 많으므로 고정전에 측정을 해야 한다.``
```sql
@/home/oracle/scripts/spa_cpu.sql
@/home/oracle/scripts/spa_report_cpu.sql
```

```sql
@/home/oracle/scripts/spa_elapsed.sql
@/home/oracle/scripts/spa_report_elapsed.sql
```


### SQL Tuning Advisor


```sql
-- -----------------------------------------------------------------------------------
-- File Name    : https://MikeDietrichDE.com/wp-content/scripts/
-- Author       : Mike Dietrich
-- Description  : Run SQL Tuning Advisor on a SQL Tuning Set
-- Requirements : Access to the DBA role.
-- Call Syntax  : @sta_ccr.sql
-- Last Modified: 09/05/2019
-- -----------------------------------------------------------------------------------

SET SERVEROUT ON
SET PAGESIZE 1000
SET LONG 2000000
SET LONGCHUNKSIZE 100000
SET LINESIZE 10000
SET PAGESIZE 10000


DECLARE

  sts_task   VARCHAR2(64);
  tname      VARCHAR2(100);
  sta_exists number;

BEGIN

  SELECT count(*)
  INTO   sta_exists
  FROM   DBA_ADVISOR_TASKS
  WHERE  rownum = 1 AND
         task_name = 'STA_UPGRADE_TO_19C_CC';

  IF sta_exists = 1 THEN
    SYS.DBMS_SQLTUNE.DROP_TUNING_TASK(
       task_name=>'STA_UPGRADE_TO_19C_CC'
       );
  ELSE
    DBMS_OUTPUT.PUT_LINE('SQL Tuning Task does not exist - will be created ...');
  END IF;

--
-- Create a STA Task and parameterize it
--


  tname := DBMS_SQLTUNE.CREATE_TUNING_TASK(
        sqlset_name  => 'STS_CaptureCursorCache',
        rank1        => 'BUFFER_GETS',
        time_limit   => 360,
        task_name    => 'STA_UPGRADE_TO_19C_CC',
        description  => 'Tune AWR Workload for upgrade to 19c');



--
-- Simulate execution of STS in 19c
--

  DBMS_SQLTUNE.EXECUTE_TUNING_TASK(
     task_name      => 'STA_UPGRADE_TO_19C_CC');

END;
/

--
-- Just in case you'd like to monitor the progress of a task
--
-- SELECT sofar, totalwork FROM V$ADVISOR_PROGRESS WHERE task_id = (SELECT task_id FROM USER_ADVISOR_TASKS WHERE task_name='STA_UPGRADE_TO_19C_CC');
--

SELECT DBMS_SQLTUNE.REPORT_TUNING_TASK(task_name=>'STA_UPGRADE_TO_19C_CC', section=>'FINDINGS', result_limit => 20) FROM DUAL;

SELECT DBMS_SQLTUNE.SCRIPT_TUNING_TASK(task_name=>'STA_UPGRADE_TO_19C_CC', rec_type=>'ALL') FROM DUAL;
~

```

```sql
@/home/oracle/scripts/spa_cpu.sql
@/home/oracle/scripts/spa_report_cpu.sql
```

```sql
@/home/oracle/scripts/spa_elapsed.sql
@/home/oracle/scripts/spa_report_elapsed.sql
```
