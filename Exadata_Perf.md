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
### EXADATA RAC TUNING
