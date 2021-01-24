## dba_hist_sql_plan tips
* http://www.dba-oracle.com/oracle10g_tuning/t_dba_hist_sql_plan.htm
* http://www.rampant-books.com/book_0214_oracle_tuning_definitive_reference_3rd_ed.htm

### The dba_hist_sql_plan Table

* The dba_hist_sql_plan table contains time-series data about each object, table, index, or view, involved in the query.  The important columns include the cost, cardinality, cpu_cost , io_cost  and temp_space required for the object.
* The sample query below retrieves SQL statements which have high query execution cost identified by Oracle optimizer.

#### awr_high_cost_sql.sql

```sql
col c1 heading ‘SQL|ID’              format a13
col c2 heading ‘Cost’                format 9,999,999
col c3 heading ‘SQL Text’            format a200

select
  p.sql_id            c1,
  p.cost              c2,
  to_char(s.sql_text) c3
from
  dba_hist_sql_plan    p,
  dba_hist_sqltext     s
where
      p.id = 0
  and
      p.sql_id = s.sql_id
  and
      p.cost is not null
order by 
  p.cost desc
;

The output of the above query might look like this, showing the high cost SQL statements over time:



SQL
ID                  Cost SQL Text
------------- ---------- -------------------------------------------
847ahztscj4xw    358,456 select
                            s.begin_interval_time  c1,
                            pl.sql_id               c2,
                            pl.object_name          c3,
                            pl.search_columns       c4,
                            pl.cardinality          c5,
                            pl.access_predicates    c6,
                            pl.filter_predicates    c7
                         from
                            dba_hist_sql_plan pl,
                            dba_hist_snapshot s
                         order by
                            c1, c2

58du2p8phcznu      5,110 select
                            begin_interval_time  c1,
                            search_columns       c2,
                            count(*)             c3
                         from
                            dba_hist_sqltext
                         natural join
                            dba_hist_snapshot
                         natural join
                            dba_hist_sql_plan
                         where
                            lower(sql_text) like lower('%idx%')
                         group by
                            begin_interval_time,search_columns
 
 
There is much more information in dba_hist_sql_plan that is useful.  The query below will extract important costing information for all objects involved in each query.  SYS objects are not counted.
 ```
####          awr_sql_object_char.sql

```sql
col c1 heading ‘Owner’              format a13
col c2 heading ‘Object|Type’        format a15
col c3 heading ‘Object|Name’        format a25
col c4 heading ‘Average|CPU|Cost’   format 9,999,999
col c5 heading ‘Average|IO|Cost’    format 9,999,999
break on c1 skip 2
break on c2 skip 2

select
  p.object_owner    c1,
  p.object_type     c2,
  p.object_name     c3,
  avg(p.cpu_cost )   c4,
  avg(p.io_cost )    c5
from
  dba_hist_sql_plan p
where
        p.object_name is not null
    and
        p.object_owner <> 'SYS'
group by
  p.object_owner,
  p.object_type,
  p.object_name
order by
  1,2,4 desc
;


The following is a sample of the output.  The results show the average CPU and I/O costs for all objects that participate in queries, over time periods.
 
                                                          Average    Average
              Object          Object                           CPU         IO
Owner         Type            Name                            Cost       Cost
------------- --------------- ------------------------- ---------- ----------
OLAPSYS       INDEX           CWM$CUBEDIMENSIONUSE_IDX         200          0
OLAPSYS       INDEX (UNIQUE)  CWM$DIMENSION_PK
OLAPSYS                       CWM$CUBE_PK                    7,321          0
OLAPSYS                       CWM$MODEL_PK                   7,321          0
OLAPSYS       TABLE           CWM$CUBE                       7,911          0
OLAPSYS                       CWM$MODEL                      7,321          0
OLAPSYS                       CWM2$CUBE                      7,121          2
OLAPSYS                       CWM$CUBEDIMENSIONUSE             730          0
MYSCHEMA                      CUSTOMER_DETS_PK              21,564          2
MYSCHEMA                      STATS$SGASTAT_U               21,442          2
MYSCHEMA                      STATS$SQL_SUMMARY_PK          16,842          2
MYSCHEMA                      STATS$SQLTEXT_PK              14,442          1
MYSCHEMA                      STATS$IDLE_EVENT_PK            8,171          0
SPV           INDEX (UNIQUE)  WSPV_REP_PK                    7,321          0
SPV                           SPV_ALERT_DEF_PK               7,321          0
SPV           TABLE           WSPV_REPORTS                 789,052         28
SPV                           SPV_MONITOR                   54,092          3
SPV                           SPV_SAVED_CHARTS              38,337          3
SPV                           SPV_DB_LIST                   37,487          3
SPV                           SPV_SCHED                     35,607          3
SPV                           SPV_FV_STAT                   35,607          3

This script can now be changed to allow the user to enter a table name and see changes in access details over time:
```

#### awr_sql_object_char_detail.sql

```sql
accept tabname prompt ‘Enter Table Name:’
col c0 heading ‘Begin|Interval|time’ format a8
col c1 heading ‘Owner’               format a10
col c2 heading ‘Object|Type’         format a10
col c3 heading ‘Object|Name’         format a15
col c4 heading ‘Average|CPU|Cost’    format 9,999,999
col c5 heading ‘Average|IO|Cost’     format 9,999,999
break on c1 skip 2
break on c2 skip 2
select
  to_char(sn.begin_interval_time,'mm-dd hh24') c0, 
  p.object_owner                               c1,
  p.object_type                                c2,
  p.object_name                                c3,
  avg(p.cpu_cost)                              c4,
  avg(p.io_cost)                               c5
from
  dba_hist_sql_plan p,
  dba_hist_sqlstat  st,
  dba_hist_snapshot sn
where
  p.object_name is not null
and
   p.object_owner <> 'SYS'
and
   p.object_name = 'CUSTOMER_DETS'
and
  p.sql_id = st.sql_id
and
  st.snap_id = sn.snap_id    
group by
  to_char(sn.begin_interval_time,'mm-dd hh24'),
  p.object_owner,
  p.object_type,
  p.object_name
order by
  1,2,3 desc
;

This script is great because it is possible to see changes to the table’s access patterns over time, which is a very useful feature:

Begin                                             Average    Average
Interval            Object     Object                 CPU         IO
time     Owner      Type       Name                  Cost       Cost
-------- ---------- ---------- --------------- ---------- ----------
10-25 17 MYSCHEMA   TABLE      CUSTOMER_DETS       28,935          3
10-26 15 MYSCHEMA              CUSTOMER_DETS       28,935          3
10-27 18 MYSCHEMA              CUSTOMER_DETS    5,571,375         24
10-28 12 MYSCHEMA              CUSTOMER_DETS       28,935          3
 
 ```
