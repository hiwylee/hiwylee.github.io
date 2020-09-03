## SQL Tuning 
### Scripts
* https://techgoeasy.com/useful-scripts-oracle-database/
* https://oracle-base.com/dba/scripts
### stratistics
* EXEC DBMS_STATS.GATHER_DICTIONARY_STATS;
* exec dbms_stats.gather_fixed_objects_stats;
* exec  dbms_stats.GATHER_SCHEMA_STATS ('SYS');
### Monitoring
* script - SQL List   - smonl2.sql
```sql
--:
--:NAME
--:
--:     smonl.sql
--:
--:
--:SYNOPSIS
--:
--:     @smonl.sql [n]
--:
--:
--:DESCRIPTION
--:
--:     Real-time SQL monitoring 리스트 조회
--:
--:     n
--:         건수. (기본값: top 50)
--:

set feedback off
set timing off

column 1 new_value 1 noprint

select '' "1" from dual where rownum = 0;
define n = &1 "50"

undefine 1

set feedback on
set timing on


set feedback off
set heading off
set timing off

select '[Real-time SQL Monitoring List: '||to_char(sysdate, 'YYYY-MM-DD HH24:MI:SS')||']' from dual;

set feedback on
set heading on
set timing on


set tab off
set timing off

column status         format a15 truncate  heading Status
column sql_exec_start format a8           heading Start
column duration       format a8           heading Duration
column cpu_pct        format 990.90        heading CPU%
column user_io_pct    format 990.90        heading IO%
column other_pct      format 990.90        heading Other%
column id             format a15          heading ID
column username       format a8  truncate heading User
column program        format a16 truncate heading Program
column module         format a15 truncate heading Module
column action         format a15 truncate heading Action
column dop            format a8
column sql_text       format a40 truncate heading "SQL Text"

select * from (
  select inst_id,status,
               to_char(sql_exec_start, 'HH24:MI:SS') as sql_exec_start,
               case
                    when status = 'EXECUTING' or status = 'QUEUED' then
                        to_char(to_date('1970-01-01 00:00:00', 'YYYY-MM-DD HH24:MI:SS') + (sysdate - sql_exec_start), 'HH24:MI:SS')
                    else
                        to_char(to_date('1970-01-01 00:00:00', 'YYYY-MM-DD HH24:MI:SS') + (last_refresh_time - sql_exec_start), 'HH24:MI:SS')
                end as duration,
                nvl(dbop_name, sql_id) as id,
                username,
                case
                    when instr(program, '@') != 0 then
                        regexp_replace(program, '@.*') || ' ' || regexp_substr(program, '\(.*\)')
                    else program
                end as program,
                module,
                action,
                case
                    when sm.px_servers_allocated > 0 then
                        sm.px_servers_allocated || '(' || sm.px_maxdop_instances ||
                        case
                            when sm.px_servers_allocated < sm.px_servers_requested then
                                '-D'
                            else
                                null
                        end ||
                        ')'
                    else
                        null
                end as dop,
                sql_text
           from gv$sql_monitor sm
          where process_name = 'ora' -- foreground only
          and sm.sql_exec_start > sysdate - 4/24
         --and sm.status = 'EXECUTING'
        order by sm.last_refresh_time)
    order by substr(status,1,4),sql_exec_start
;

set tab on
set timing on
```

* ``script - SQL plan``   - smonl.sql
```sql
```
--:
--:NAME
--:
--:     smon.sql
--:
--:
--:SYNOPSIS
--:
--:     @smon.sql [sql_id]
--:
--:
--:DESCRIPTION
--:
--:     주어진 SQL에 대해 real-time SQL monitoring 조회
--:
--:     sql_id
--:         Monitor된 SQL (기본값: 마지막으로 모니터링된 SQL)
--:

set feedback off
set timing off

column 1 new_value 1 noprint

select '' "1" from dual where rownum = 0;
define sql_id = &1 ""

undefine 1

set feedback on
set timing on


set feedback off
set linesize 512
set timing off

select dbms_sqltune.report_sql_monitor(sql_id =>'&&sql_id', report_level => 'ALL') as report
  from dual;

set feedback on
set linesize 236
set timing on
```

* 사용예제
```sql
SQL> @smonl2

[Real-time SQL Monitoring List: 2020-09-03 02:22:24]

   INST_ID Status          Start    Duration ID              User     Program          Module          Action          DOP      SQL Text
---------- --------------- -------- -------- --------------- -------- ---------------- --------------- --------------- -------- ----------------------------------------
         1 DONE (ALL ROWS) 00:50:14 00:00:01 gudpnkn1cxszt   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     select /*+ ordered parallel(a,4) paralle
         1 DONE (ALL ROWS) 00:53:28 00:00:00 93366v8nv3tag   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     select /*+ ordered parallel(a,4) paralle
         1 DONE (ALL ROWS) 00:53:34 00:00:01 93366v8nv3tag   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     select /*+ ordered parallel(a,4) paralle
         1 DONE (ALL ROWS) 01:39:35 00:00:01 93366v8nv3tag   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     select /*+ ordered parallel(a,4) paralle
         1 DONE (ALL ROWS) 01:46:48 00:00:00 g4hs5spqvputq   SYS      sqlplus (TNS V1- sqlplus@worksho                 2(1)     select  /*+ parallel (2) pq_filter(seria
         1 DONE (ALL ROWS) 01:48:47 00:00:00 6mmqu76rgrj4u   SYS      sqlplus (TNS V1- sqlplus@worksho                 2(1)     select  /*+ parallel (2) pq_filter(none)
         1 DONE (ERROR)    01:54:15 00:00:11 8c3704cfgjztb   SYS      sqlplus (TNS V1- sqlplus@worksho                          SELECT
         1 DONE            01:55:41 00:01:26 65ppdfwmj3krr   SYS      sqlplus (TNS V1- sqlplus@worksho                          BEGIN DBMS_STATS.GATHER_FIXED_OBJECTS_ST
         1 DONE (FIRST N R 01:56:27 00:00:01 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (FIRST N R 01:56:28 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (FIRST N R 01:56:28 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (FIRST N R 01:56:28 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (ALL ROWS) 01:57:05 00:00:00 605x8179cuahu   SYS      sqlplus (TNS V1- sqlplus@worksho                 2(1)     select directory_path from dba_directori
         1 DONE (ERROR)    01:58:50 00:00:51 8c3704cfgjztb   SYS      sqlplus (TNS V1- sqlplus@worksho                          SELECT
         1 DONE            02:05:50 00:01:22 2cn87bmkfwu10   SYS      sqlplus (TNS V1- sqlplus@worksho                          BEGIN dbms_stats.GATHER_SCHEMA_STATS ('S
         1 DONE (FIRST N R 02:06:23 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (FIRST N R 02:06:23 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (FIRST N R 02:06:23 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (FIRST N R 02:06:23 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (ERROR)    02:07:21 00:01:02 8c3704cfgjztb   SYS      sqlplus (TNS V1- sqlplus@worksho                          SELECT
         1 DONE            02:09:23 00:01:30 gydz89x3vzu14   SYS      sqlplus (TNS V1- sqlplus@worksho                          BEGIN dbms_stats.gather_fixed_objects_st
         1 DONE (FIRST N R 02:10:14 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (FIRST N R 02:10:14 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (FIRST N R 02:10:14 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (FIRST N R 02:10:14 00:00:00 fn0snbuqyccq5   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     SELECT NAME, PATH, READ, WRITE, EXECUTE
         1 DONE (ALL ROWS) 02:10:51 00:00:00 605x8179cuahu   SYS      sqlplus (TNS V1- sqlplus@worksho                 2(1)     select directory_path from dba_directori
         1 DONE            02:11:01 00:00:08 gqd4m1achy5u0   SYS      sqlplus (TNS V1- sqlplus@worksho                          BEGIN DBMS_STATS.GATHER_DICTIONARY_STATS
         1 DONE (ERROR)    02:11:26 00:00:07 8c3704cfgjztb   SYS      sqlplus (TNS V1- sqlplus@worksho                          SELECT
         1 DONE (ALL ROWS) 02:12:07 00:01:36 8c3704cfgjztb   SYS      sqlplus (TNS V1- sqlplus@worksho                          SELECT
         1 DONE (ALL ROWS) 02:17:07 00:00:00 g4hs5spqvputq   SYS      sqlplus (TNS V1- sqlplus@worksho                 2(1)     select  /*+ parallel (2) pq_filter(seria
         1 DONE (ALL ROWS) 02:18:47 00:00:00 gudpnkn1cxszt   SYS      sqlplus (TNS V1- sqlplus@worksho                 8(1)     select /*+ ordered parallel(a,4) paralle

31 rows selected.

SQL>

```
* PLAN
```sql
set long 10000   -- DBMS_SQLTUNE.REPORT_SQL_MONITOR 실행시 결과가 모두 나오지 않을때
col report format a200  -- line wrap 될 경우

SQL> @smon gudpnkn1cxszt
old   1: select dbms_sqltune.report_sql_monitor(sql_id =>'&&sql_id', report_level => 'ALL') as report
new   1: select dbms_sqltune.report_sql_monitor(sql_id =>'gudpnkn1cxszt', report_level => 'ALL') as report

REPORT
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SQL Monitoring Report

SQL Text
------------------------------
select /*+ ordered parallel(a,4) parallel(b,4) pq_distribute(p, hash, hash) monitored gather_plan_statistics */ * from t1 a, t2 b where b.c1=a.c1

Global Information
------------------------------
 Status              :  DONE (ALL ROWS)
 Instance ID         :  1
 Session             :  SYS (373:60605)
 SQL ID              :  gudpnkn1cxszt
 SQL Execution ID    :  16777217
 Execution Started   :  09/03/2020 02:18:47
 First Refresh Time  :  09/03/2020 02:18:47
 Last Refresh Time   :  09/03/2020 02:18:47
 Duration            :  .017148s
 Module/Action       :  sqlplus@workshop (TNS V1-V3)/-
 Service             :  pdb3
 Program             :  sqlplus@workshop (TNS V1-V3)
 Fetch Calls         :  668

Global Stats
=================================================
| Elapsed |   Cpu   |  Other   | Fetch | Buffer |
| Time(s) | Time(s) | Waits(s) | Calls |  Gets  |
=================================================
|    0.04 |    0.02 |     0.01 |   668 |    118 |
=================================================

Parallel Execution Details (DOP=4 , Servers Allocated=8)
==========================================================================================
|      Name      | Type  | Server# | Elapsed |   Cpu   |  Other   | Buffer | Wait Events |
|                |       |         | Time(s) | Time(s) | Waits(s) |  Gets  | (sample #)  |
==========================================================================================
| PX Coordinator | QC    |         |    0.02 |    0.00 |     0.01 |     10 |             |
| p000           | Set 1 |       1 |    0.00 |    0.00 |          |        |             |
| p001           | Set 1 |       2 |    0.00 |    0.00 |          |        |             |
| p002           | Set 1 |       3 |    0.00 |    0.00 |          |        |             |
| p003           | Set 1 |       4 |    0.00 |    0.00 |          |        |             |
| p004           | Set 2 |       1 |    0.00 |    0.00 |          |     15 |             |
| p005           | Set 2 |       2 |    0.00 |    0.00 |          |     33 |             |
| p006           | Set 2 |       3 |    0.00 |    0.00 |          |     30 |             |
| p007           | Set 2 |       4 |    0.00 |    0.00 |          |     30 |             |
==========================================================================================

SQL Plan Monitoring Details (Plan Hash Value=1272085988)
=============================================================================================================================================
| Id |          Operation          |   Name   |  Rows   | Cost |   Time    | Start  | Execs |   Rows   |  Mem  | Activity | Activity Detail |
|    |                             |          | (Estim) |      | Active(s) | Active |       | (Actual) | (Max) |   (%)    |   (# samples)   |
=============================================================================================================================================
|  0 | SELECT STATEMENT            |          |         |      |         1 |     +0 |     9 |    10000 |     . |          |                 |
|  1 |   PX COORDINATOR            |          |         |      |         1 |     +0 |     9 |    10000 |     . |          |                 |
|  2 |    PX SEND QC (RANDOM)      | :TQ10002 |   10000 |    4 |         1 |     +0 |     4 |    10000 |     . |          |                 |
|  3 |     HASH JOIN BUFFERED      |          |   10000 |    4 |         1 |     +0 |     4 |    10000 |  19MB |          |                 |
|  4 |      PX RECEIVE             |          |   10000 |    2 |         1 |     +0 |     4 |    10000 |     . |          |                 |
|  5 |       PX SEND HYBRID HASH   | :TQ10000 |   10000 |    2 |         1 |     +0 |     4 |    10000 |     . |          |                 |
|  6 |        STATISTICS COLLECTOR |          |         |      |         1 |     +0 |     4 |    10000 |     . |          |                 |
|  7 |         PX BLOCK ITERATOR   |          |   10000 |    2 |         1 |     +0 |     4 |    10000 |     . |          |                 |
|  8 |          TABLE ACCESS FULL  | T1       |   10000 |    2 |         1 |     +0 |    18 |    10000 |     . |          |                 |
|  9 |      PX RECEIVE             |          |   10000 |    2 |         1 |     +0 |     4 |    10000 |     . |          |                 |
| 10 |       PX SEND HYBRID HASH   | :TQ10001 |   10000 |    2 |         1 |     +0 |     4 |    10000 |     . |          |                 |
| 11 |        PX BLOCK ITERATOR    |          |   10000 |    2 |         1 |     +0 |     4 |    10000 |     . |          |                 |
| 12 |         TABLE ACCESS FULL   | T2       |   10000 |    2 |         1 |     +0 |    18 |    10000 |     . |          |                 |
=============================================================================================================================================

SQL>

```
### Consideration
* Business Logic
* Data Desgin
* Application Design
* Change db Structure(Indexes)
* Tuning SQL
* Access Path - change to indexc
* Memory Allocation - Instance Tuning
### Hint
* pq_distribute
* opt_param
* leading
* swap_join_inputs
* pq_replicate
* no_gather_optimizer_statistics
```
INSERT /*+ pq_distribute(t none) opt_param('optimizer_adaptive_plans','false') */
...
SELECT * FROM (
	SELECT /*+ leading(f p j c) swap_join_inputs(c) swap_join_inputs(j)  swap_join_inputs(p)  pq_replicate(c) pq_replicate(j) pq_replicate(p) no_gather_optimizer_statistics pq_distribute(p none broadcast) */
..  
```
