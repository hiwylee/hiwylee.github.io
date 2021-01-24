## Oracle AWR report
### Perf Guide Portal - RAC Perfomance tuning with AWR/EM reports
* https://www.hhutzler.de/blog/rac-tuning-with-awr/#Tuning_Step_1_Avoid_sequences_by_using_a_JAVA_generated_sequence

### MOS 
* [``	AWR Report Interpretation Checklist for Diagnosing Database Performance Issues (Doc ID 1628089.1)``](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=253941980006798&id=1628089.1&displayIndex=5&_afrWindowMode=0&_adf.ctrl-state=hhpe3qlm4_166#aref_section31)
* [``Archive of Database Performance Related Webcasts and Videos (Doc ID 1597373.1``)](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=254265968004134&parent=DOCUMENT&sourceId=1628089.1&id=1597373.1&_afrWindowMode=0&_adf.ctrl-state=hhpe3qlm4_264)
* [Introduction to Performance Analysis Using AWR and ASH](http://education.oracle.com/pls/web_prod-plq-dad/db_pages.getpage?page_id=721&get_params=streamId:21)
* [How to generate 'Automatic Workload Repository' ( AWR), 'Automatic Database Diagnostic Monitor' (ADDM), 'Active Session History' (ASH) reports. (Doc ID 2349082.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=253954498490732&id=2349082.1&displayIndex=10&_afrWindowMode=0&_adf.ctrl-state=hhpe3qlm4_215#aref_section21)
### TOOLS : www.orapub.com
* https://www.orapub.com/tools

### AWR report

```sql
@?/rdbms/admin/awrrpt.sql      -- basic AWR report
@?/rdbms/admin/awrsqrpt.sql    -- Standard SQL statement Report
@?/rdbms/admin/awrddrpt.sql    -- Period diff on current instance
@?/rdbms/admin/awrrpti.sql     -- Workload Repository Report Instance (RAC)
@?/rdbms/admin/awrgrpt.sql     -- AWR Global Report (RAC)
@?/rdbms/admin/awrgdrpt.sql    -- AWR Global Diff Report (RAC)
@?/rdbms/admin/awrinfo.sql     -- Script to output general AWR information
```

### Oracle Database Tips by Donald Burleson
See my notes on Reading Oracle AWR report and see the book Oracle Tuning: The Definitive Reference for a comprehensive treatment of AWR for Oracle tuning.  Also see these tips for Oracle AWR reports:

* [Oracle AWR SQL Tuning Scripts](http://www.dba-oracle.com/art_orafaq_awr_sql_tuning.htm)
* [Oracle AWR sysaux tablespace](http://www.fast-track.cc/t_awr_workload_sysaux_tablespaces.htm)
* [Interpreting RAC AWR reports](http://www.dba-oracle.com/t_rac_statspack_awr_report_tips.htm)
* [Oracle STATSPACK vs. AWR](http://www.fast-track.cc/t_statspack_awr.htm)
* [AWR script for physical disk reads](http://www.dba-oracle.com/art_orafaq_awr_disk_reads.htm)
* [Oracle transportable AWR snapshots](http://www.rampant-books.com/art_oracle_awr_transportable_snapshots.htm)
* [Oracle Creating an AWR Report](http://www.dba-oracle.com/oracle10g_tuning/t_oracle_creating_awr_report_awrrpt.htm)
* [Oracle AWR disk file statistics](http://www.praetoriate.com/t_awr_disk_file_statistics.htm)

### [SQL Tuning Script](https://kosate.tistory.com/109)
* SQL 튜닝 대상선정(10g)하기

```sql
select trunc(a.disk_reads/a.executions,0) diskreads,
       trunc(a.buffer_gets/a.executions,0) bufferget, 
       trunc(a.elapsed_time/a.executions/1000000,0) elapsetime,
       trunc(a.ROWS_PROCESSED/a.executions,0) return_rows,
       a.executions,
       a.last_load_time,
       module,action, length(sql_fulltext), sql_fulltext, address,sql_id,parsing_schema_name
  from v$sql  a 
 where executions > 0
   and command_type in ( 3, 6,7)
   and module not in ( 'SQL Developer','Orange for ORACLE DBA')
   and buffer_gets / executions > 1000
 order by elapsetime desc ;
  
command_type - 2 (insert)
command_type - 3 (select)
command_type - 7 (delete)
command_type - 6 (update)

```

* bind 변수 확인
```sql
select * from v$sql_bind_capture where address = 'C000000095EFDDC0';
select * from dba_hist_sqlbind where sql_id = '0b5b05k3akd1w'  order by snap_id desc, position;

```
* full text

```sql
select 'AA'||sql_text||'BB' from  v$sqltext_with_newlines where address = 'C000000095EFDDC0'
 order by Piece
select 'AA'||sql_text||'BB' from  v$sqltext_with_newlines where sql_id = 'gzcf51wp0pqxt' 
order by Piece
```

* plan보기

```sql
select p.plan_table_output
  from (select distinct sql_id, child_number
          from v$sql_plan s
         where s.address = '' or 
               s.sql_id = '0as4u6a4fky2n') s,
        table(dbms_xplan.display_cursor (s.sql_id, s.child_number, 'typical')) p;
```
--  awr plan보기

```sql
select sql_id,lpad(' ',depth*4,'  ')||' '||operation|| ' ' ||options|| ' '
 ||object_name|| ' (' ||cost||')'plan, to_char(timestamp,'YYYY-MM-DD HH24:MI:SS') as "date"
   from DBA_HIST_SQL_PLAN 
where sql_id in ('fac0jhjuwg9k9') 
order by timestamp,sql_id,plan_hash_value, id;

```

* awr 성능 보기

```sql
select sql_id, module, b.begin_interval_time,
       trunc(buffer_gets_delta/decode(executions_delta,0,1,executions_delta)) buffer_gets,
       trunc(disk_reads_delta/decode(executions_delta,0,1,executions_delta)) disk_reads,
       trunc(fetches_delta/decode(executions_delta,0,1,executions_delta)) fetchs,
       trunc(ROWS_PROCESSED_DELTA/decode(executions_delta,0,1,executions_delta)) ROWS_PROCESSED,
       trunc(elapsed_time_delta/1000000/decode(executions_delta,0,1,executions_delta)) 
   as elapsed_time,
       trunc(IOWAIT_DELTA/1000000/decode(executions_delta,0,1,executions_delta)) IOWAIT,
       trunc(APWAIT_DELTA/1000000/decode(executions_delta,0,1,executions_delta)) APWAIT,
       trunc(CLWAIT_DELTA/1000000/decode(executions_delta,0,1,executions_delta)) CLWAIT,
       trunc(CCWAIT_DELTA/1000000/decode(executions_delta,0,1,executions_delta)) CCWAIT,
       executions_delta executions
 from DBA_HIST_SQLSTAT a, 
      dba_hist_snapshot b
where a.sql_id = '7rcjrfsh81jy2'
  and a.snap_id  = b.snap_id
  and a.dbid = b.dbid
  and b.instance_number = 1
  and b.begin_interval_time between to_timestamp('20110701','YYYYMMDD')
 and to_timestamp('2012','YYYY')
  order by a.snap_id;
```
* trace를 못 뜰때?ㅋ 

```sql
select /*+ gather_plan_statistics */ * 
from SCOTT.TEST where key > 10000;
select * from table(dbms_xplan.display_cursor(null,null,'ALLSTATS LAST'));

dbms_xplan.display_cursor format 종류
   - Basic, Typical, Outline, All, Advanced, 
   - allstats last, +peeked_binds
 ```
   
