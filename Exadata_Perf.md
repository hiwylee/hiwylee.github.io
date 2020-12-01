## Exadata Performance Tuning
### The logical steps in Oracle tuning
1. Reduce application demand to its logical minimum by tuning SQL and PL/SQL and optimizing physical design (partitioning, indexing, etc.).
2. Maximize concurrency by minimizing contention for locks, latches, buffers, and other resources in the Oracle code layer.
3. Having normalized logical I/O demand in the preceding steps, minimize the resulting physical I/O by optimizing Oracle memory.
4. Now that the physical I/O demand is realistic, configure the I/O subsystem to meet that demand by providing adequate I/O bandwidth and evenly distributing the resulting load.

### Oracle Performance Troubleshooting
1. Using the Oracle views that implement the wait and time model interface
2. Using the Oracle views that implement information about SQL statement execution (V$SQL and related tables), identify the SQL statements that are consuming the most database resources or that have the highest elapsed time and tune these using techniques such as indexing, baselines, or SQL rewrites.

* Top Ten Waits and Time Model Categories
```sql
wiTH waits
         AS (  SELECT event,SUM (total_waits) AS total_waits,
                      ROUND (SUM (time_waited_micro) / 1000000, 0)
                         AS time_waited_seconds
                 FROM gv$system_event
                WHERE wait_class <> 'Idle'
             GROUP BY event
             UNION
               SELECT stat_name, NULL AS waits,
                     ROUND (SUM (VALUE) / 1000000, 0)
                        AS time_waited_seconds
                FROM v$sys_time_model
               WHERE stat_name IN ('DB CPU', 'background cpu time')
            GROUP BY stat_name)
     SELECT event,
            total_waits,
            time_waited_seconds,
            ROUND (time_waited_seconds * 100 /
                   SUM (time_waited_seconds) OVER (),2)
               AS pct_time
       FROM (SELECT w.*,RANK () OVER (
                      ORDER BY time_waited_seconds DESC) time_rank
               FROM waits w)
      WHERE time_rank <= 10
  ORDER BY 3 DESC
/
EVENT                                                            TOTAL_WAITS TIME_WAITED_SECONDS   PCT_TIME
---------------------------------------------------------------- ----------- ------------------- ----------
background cpu time                                                                       113298      58.56
DB CPU                                                                                     15331       7.92
Sync ASM rebalance                                                   1669626               14091       7.28
control file sequential read                                        44371450               10999       5.69
PX Deq: reap credit                                               1445416697                9202       4.76
ASM file metadata operation                                         50446253                7763       4.01
IMR slave acknowledgement msg                                       34858964                6956        3.6
Disk file Mirror Read                                               15654547                6645       3.43
Disk file I/O Calibration                                             560000                4934       2.55
direct path write                                                     140109                4238       2.19

10 rows selected.

Elapsed: 00:00:00.01

```
* Top Ten SQL Statements

```sql
      SELECT sql_id, child_number,elapsed_time_sec, sql_text
        FROM (  SELECT sql_id, child_number,  substr(sql_text,1,90) sql_text,
                       SUM (elapsed_time/1000000) elapsed_time_sec,
                       SUM (cpu_time) cpu_time,
                       SUM (disk_reads) disk_reads,
                       RANK () OVER (ORDER BY SUM (elapsed_time) DESC)
                          AS elapsed_rank
                  FROM gv$sql
              GROUP BY sql_id, child_number, sql_text)
      WHERE elapsed_rank <= 5
  ORDER BY elapsed_rank
/
SQL_ID        CHILD_NUMBER ELAPSED_TIME_SEC SQL_TEXT
------------- ------------ ---------------- ------------------------------------------------------------
6hnhqahphpk8n            0       9982.02798 select free_mb from v$asm_diskgroup_stat where name=:1
cf8xhssjgbc19            1       2624.72801 insert into  WRH$_ASM_BAD_DISK  (dbid, per_pdb, con_dbid, sn
                                            ap_id,  GROUP_NUMBER, NAME, PA

4xm1ruvkx3awx            0       1673.41293 DECLARE job BINARY_INTEGER := :job;  next_date TIMESTAMP WIT
                                            H TIME ZONE := :mydate;  broke

b6usrg82hwsa3            0       759.403232 call dbms_stats.gather_database_stats_job_proc (  )
cf8xhssjgbc19            0       720.602193 insert into  WRH$_ASM_BAD_DISK  (dbid, per_pdb, con_dbid, sn
                                            ap_id,  GROUP_NUMBER, NAME, PA


5 rows selected.


```
### APPLICATION DESIGN FOR EXADATA
* Eliminates unnecessary requests from the application to the database server:  
  * By eliminating any unnecessary SQL execution requests   
  * By eliminating unnecessary SQL parse requests through bind variables and effective cursor management
* Reduces network overhead and unnecessary network round trips:
  * By exploiting the array fetch and insert interface
  * By using stored procedures when appropriate
* Reduces application-driven lock contention through sensible transaction design and locking strategies

### DATABASE DESIGN FOR EXADATA

* onitoring Offloading, Storage Indexes, and Flash Activity

```sql
    SELECT name, VALUE
      FROM v$sysstat where name in ('cell flash cache read hits',
      'cell physical IO bytes saved by storage index',
      'cell physical IO bytes eligible for predicate offload',
      'cell scans'
     )
    order by name
/
NAME                                                                  VALUE
---------------------------------------------------------------- ----------
cell flash cache read hits                                         17041724
cell physical IO bytes eligible for predicate offload            1.2732E+12
cell physical IO bytes saved by storage index                    5784788992
cell scans                                                             6381

4 rows selected.
```
* Identifying Redundant and Disused Indexes

```sql
SELECT table_name, index_name
  FROM user_indexes i
 WHERE uniqueness <> 'UNIQUE'
   AND index_name NOT IN
(SELECT DISTINCT object_name
         FROM v$sql_plan
        WHERE operation LIKE '%INDEX%'
         --  AND object_owner = USER
          )
/

-- Turn monitoring on for all indexes:

BEGIN
   FOR r IN (SELECT index_name FROM user_indexes)
   LOOP
      EXECUTE IMMEDIATE 'ALTER INDEX ' || r.index_name || ' MONITORING USAGE';
   END LOOP;
END;
/

-- Later run this query

SELECT index_name,
       table_name,
       used,
       start_monitoring
  FROM v$object_usage
 WHERE MONITORING = 'YES';

```

* Storage Indexes as well as Smart Scan Offloading:

```sql
SELECT name, VALUE
      FROM v$statname JOIN v$mystat USING (statistic#)
     WHERE name IN
     ('cell physical IO bytes eligible for predicate offload',
      'cell physical IO interconnect bytes returned by smart scan',
     'cell physical IO bytes saved by storage index')
/
NAME                                                                  VALUE
---------------------------------------------------------------- ----------
cell physical IO bytes eligible for predicate offload                     0
cell physical IO bytes saved by storage index                             0
cell physical IO interconnect bytes returned by smart scan                0

3 rows selected.


```

* Top Ten Waits and Time Model Categories

```sql
WITH waits
     AS (  SELECT event,SUM (total_waits) AS total_waits,
                  ROUND (SUM (time_waited_micro) / 1000000, 0)
                     AS time_waited_seconds
             FROM gv$system_event
            WHERE wait_class <> 'Idle'
         GROUP BY event
         UNION
           SELECT stat_name, NULL AS waits,
                  ROUND (SUM (VALUE) / 1000000, 0)
                   AS time_waited_seconds
             FROM v$sys_time_model
            WHERE stat_name IN ('DB CPU', 'background cpu time')
         GROUP BY stat_name)
  SELECT event,
         total_waits,
         time_waited_seconds,
         ROUND (time_waited_seconds * 100 /
                SUM (time_waited_seconds) OVER (),2)
            AS pct_time
    FROM (SELECT w.*,RANK () OVER (
                   ORDER BY time_waited_seconds DESC) time_rank
            FROM waits w)
   WHERE time_rank <= 10
ORDER BY 3 DESC;
                                                Total         Time
EVENT                                           Waits   Waited (s)    Pct
---------------------------------------- ------------ ------------ ------
control file sequential read               84,364,933       94,116  29.08
DB CPU                                                      69,513  21.48
cell single block physical read             9,944,146       37,987  11.74
cell smart table scan                      52,059,906       30,534   9.44
Streams AQ: qmn coordinator waiting for         5,153       27,998   8.65
slave to start
background cpu time                                         25,857   7.99
Disk file Mirror Read                      13,256,135       17,052   5.27
DFS lock handle                             2,394,441        8,311   2.57
db file parallel write                      3,276,183        6,210   1.92
enq: TM - contention                           17,262        6,031   1.86

```
### EXADATA RAC TUNING

* Summary of Wait Categories Showing Cluster Overhead

```sql
SELECT wait_class time_cat,
       ROUND((time_secs),2) time_secs,
       ROUND((time_secs) * 100 / SUM(time_secs)
           OVER (), 2) pct
FROM (SELECT wait_class wait_class,
             SUM(time_waited_micro)/1000000 time_secs
      FROM gv$system_event
      WHERE wait_class <> 'Idle' AND time_waited > 0
      GROUP BY wait_class
      UNION
      SELECT 'CPU', ROUND((SUM(VALUE)/1000000),2) time_secs
      FROM gv$sys_time_model
      WHERE stat_name IN ('background cpu time', 'DB CPU'))
ORDER BY time_secs DESC;
Time category           Time (s)    pct
-------------------- ----------- ------
User I/O              721,582.92  41.61
System I/O            459,658.69  26.51
CPU                   389,056.04  22.44
Other                 124,291.97   7.17
Cluster                18,341.66   1.06
Concurrency            11,545.14    .67
Application             6,503.29    .38
Commit                  2,433.27    .14
Configuration             525.96    .03
Network                    87.24    .01
Administrative             82.90    .00
Scheduler                   2.53    .00

```
* Breakdown of Cluster Waits

```sql

WITH system_event AS
   (SELECT CASE
             WHEN wait_class = 'Cluster' THEN event
             ELSE wait_class
           END  wait_type, e.*
     FROM gv$system_event e)
SELECT wait_type,  ROUND(total_waits/1000,2) waits_1000 ,
       ROUND(time_waited_micro/1000000/3600,2) time_waited_hours,
       ROUND(time_waited_micro/1000/total_waits,2) avg_wait_ms  ,
       ROUND(time_waited_micro*100
          /SUM(time_waited_micro) OVER(),2) pct_time
FROM (SELECT wait_type, SUM(total_waits) total_waits,
             SUM(time_waited_micro) time_waited_micro
        FROM system_event e
       GROUP BY wait_type
       UNION
      SELECT 'CPU',   NULL, SUM(VALUE)
        FROM gv$sys_time_model
       WHERE stat_name IN ('background cpu time', 'DB CPU'))
WHERE wait_type <> 'Idle'
ORDER BY  time_waited_micro  DESC;

                                     Waits       Time  Avg Wait Pct of
Wait Type                            \1000      Hours        Ms   Time
------------------------------ ----------- ---------- --------- ------
CPU                                              6.15            43.62
Other                               38,291       1.76       .17  12.50
Application                             32       1.41    157.35  10.00
User I/O                               822        .97      4.25   6.88
System I/O                             995        .96      3.46   6.78
gc current multi block request       9,709        .87       .32   6.15
gc cr multi block request           16,210        .48       .11   3.37
Commit                                 300        .44      5.31   3.13
gc current block 2-way               5,046        .37       .26   2.59
gc current block 3-way               2,294        .28       .43   1.97
gc cr block busy                       984        .16       .58   1.11


```

* Breakdown of Cluster Waits

```sql
SELECT event, SUM(total_waits) total_waits,
       ROUND(SUM(time_waited_micro) / 1000000, 2)
         time_waited_secs,
       ROUND(SUM(time_waited_micro) / 1000 /
         SUM(total_waits), 2) avg_ms
FROM gv$system_event
WHERE       event LIKE 'gc%block%way'
      OR event LIKE 'gc%multi%'
      OR event LIKE 'gc%grant%'
      OR event LIKE 'cell single%'
GROUP BY event
HAVING SUM(total_waits) > 0
ORDER BY event;

                                           Total         Time  Avg Wait
Wait event                                 Waits       (secs)      (ms)
----------------------------------- ------------ ------------ ---------
cell single block physical rea        58,658,569      343,451      5.86
gc cr block 2-way                      1,226,123          133       .11
gc cr grant 2-way                      3,557,547          329       .09
gc cr grant congested                     33,230            3       .10
gc cr multi block request              1,867,799        2,716      1.45
gc current block 2-way                 4,245,674          449       .11
gc current grant 2-way                 1,885,528          166       .09
gc current grant busy                    656,165          145       .22
gc current grant congested                17,004            2       .10
gc current multi block request            10,996            2       .18

```
