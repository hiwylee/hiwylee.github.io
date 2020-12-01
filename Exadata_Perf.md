## Oracle Performance Troubleshooting
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
