## TKPROF 사용
### 테스트 스트립트
* Base Table
```sql
 CREATE TABLE T_BASE PCTFREE 0 PARALLEL 4 NOLOGGING STORAGE(BUFFER_POOL KEEP) PARTITION BY HASH(CUST_NO) PARTITIONS 4 COMPRESS FOR QUERY HIGH
 AS SELECT /*+ PARALLEL(4) */ LEVEL AS CUST_NO, SYSDATE AS STDAY, 6411 AS RQST_NO FROM DUAL
    CONNECT BY LEVEL < 1000000;

```

* TRACE 할 SQL
```sql
ALTER SESSION SET STATISTICS_LEVEL=ALL;
ALTER SESSION SET statistics_level=ALL;
ALTER SESSION SET sql_trace=true;
ALTER SESSION SET tracefile_identifier='TRACEFILE_IDENTIFIER';
ALTER SESSION SET EVENTS '10046 trace name context forever, level 12';

set heading off;
set linesize 172;
set timing on;

-- TRACE 할 SQL
DROP TABLE T_CTAS purge;
CREATE TABLE T_CTAS PCTFREE 0 PARALLEL 4 NOLOGGING STORAGE(CELL_FLASH_CACHE KEEP) PARTITION BY HASH(CUST_NO) PARTITIONS 64 COMPRESS FOR QUERY LOW
AS SELECT CUST_NO, TO_DATE(STDAY, 'YYYYMMDD') AS STDAY, RQST_NO
     , CASE WHEN SUBSTR(STDAY,7, 2) < '15' THEN LAST_DAY(ADD_MONTHS(STDAY,-2))
            ELSE LAST_DAY(ADD_MONTHS(STDAY,-1))
       END AS STDAY_W
     , SUBSTR(STDAY,7, 2) CPS_BSDD
     , LAST_DAY(ADD_MONTHS(STDAY,-1))  STDAY_1
     , LAST_DAY(ADD_MONTHS(STDAY,-2))  STDAY_2
     , LAST_DAY(ADD_MONTHS(STDAY,-3))  STDAY_3
     , LAST_DAY(ADD_MONTHS(STDAY,-4))  STDAY_4
     , LAST_DAY(ADD_MONTHS(STDAY,-5))  STDAY_5
     , LAST_DAY(ADD_MONTHS(STDAY,-6))  STDAY_6
     , LAST_DAY(ADD_MONTHS(STDAY,-7))  STDAY_7
     , LAST_DAY(ADD_MONTHS(STDAY,-8))  STDAY_8
     , LAST_DAY(ADD_MONTHS(STDAY,-9))  STDAY_9
     , LAST_DAY(ADD_MONTHS(STDAY,-10)) STDAY_10
     , LAST_DAY(ADD_MONTHS(STDAY,-11)) STDAY_11
     , LAST_DAY(ADD_MONTHS(STDAY,-12)) STDAY_12
     , LAST_DAY(ADD_MONTHS(STDAY,-13)) STDAY_13
     , LAST_DAY(ADD_MONTHS(STDAY,-14)) STDAY_14
     , LAST_DAY(ADD_MONTHS(STDAY,-15)) STDAY_15
  FROM TBIX00A_PRS
 WHERE RQST_NO = 6411
 GROUP BY CUST_NO, STDAY, RQST_NO;

-- SHOW XPLAN
SELECT
    *
FROM
    TABLE(DBMS_XPLAN.DISPLAY_CURSOR(null, 0
        , 'ALLSTATS LAST -ROWS +OUTLINE +PREDICATE'));
ALTER SESSION SET EVENTS '10046 TRACE NAME CONTEXT OFF';

```

* tkprof script
```bash
#!/bin/sh

ARG_CNT=$#

echo "...argument count is $ARG_CNT"

if [ $ARG_CNT != "2" ]; then
    echo "Error- Invalid parameter"
    echo "Usage : trace.sh test.sql identifier"
    exit 1
fi

DUMP_PATH=$ORACLE_BASE/diag/rdbms/cdb21/CDB21/trace
SQL_FILE=$1
TEMP_SQL_FILE=/tmp/$SQL_FILE
TRACEFILE_IDENTIFIER=$2

# select value from v$diag_info where name = 'Diag Trace';
echo '.. set tracefile identifier'
#sed -e 's/:TRACEFILE_IDENTIFIER:/'"$TRACEFILE_IDENTIFIER"'/g' $SQL_FILE > $TEMP_SQL_FILE
sed -e 's/TRACEFILE_IDENTIFIER/'"$TRACEFILE_IDENTIFIER"'/g' $SQL_FILE > $TEMP_SQL_FILE

SQLPLUS_CMD="sqlplus / as sysdba  < $TEMP_SQL_FILE"
echo $SQLPLUS_CMD
eval $SQLPLUS_CMD

echo "... run tkprof command"

pushd $DUMP_PATH

# TRACE_FILE=`ls -lrt *${TRACEFILE_IDENTIFER}* | tail -1 | awk -F " " '{print \$9}'`
TRACE_FILE=`ls -lrt *${TRACEFILE_IDENTIFIER}* | tail -1 | awk -F " " '{print \$9}'`
PID=$$
OUTPUT_FILE=/tmp/${TRACEFILE_IDENTIFIER}_${PID}.prof

tkprof $DUMP_PATH/$TRACE_FILE $OUTPUT_FILE SYS=NO
# tkprof $DUMP_PATH/$TRACE_FILE $OUTPUT_FILE.prof SYS=NO

cat $OUTPUT_FILE

if [ -f $TEMP_SQL_FILE ]
then
    rm -fr $TEMP_SQL_FILE
fi
popd

```

### 사용법
* tk.sh sqlscript tracefile_identifier
* 예제

```sql
[oracle@db21c kcb]$ ./tk.sh ctas.sql ok_xyz
...argument count is 2
.. set tracefile identifier
sqlplus / as sysdba < /tmp/ctas.sql

SQL*Plus: Release 21.0.0.0.0 - Production on Wed Jan 27 23:05:13 2021
Version 21.1.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 21c EE High Perf Release 21.0.0.0.0 - Production
Version 21.1.0.0.0

SQL> SQL>
Session altered.

SQL>
Session altered.

SQL>
Session altered.

SQL>
Session altered.

SQL>
Session altered.

SQL> SQL> SQL> SQL> SQL> SQL>
Table dropped.

Elapsed: 00:00:00.64
SQL>   2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24
Table created.

Elapsed: 00:00:00.49
SQL> SQL>
Session altered.

Elapsed: 00:00:00.01
SQL> SQL> SQL>   2    3    4    5
SQL_ID  5tbf3tzxs087a, child number 24
--------------------------------------
CREATE TABLE T_CTAS PCTFREE 0 PARALLEL 4 NOLOGGING
STORAGE(CELL_FLASH_CACHE KEEP) PARTITION BY HASH(CUST_NO) PARTITIONS 64
COMPRESS FOR QUERY LOW AS SELECT CUST_NO, TO_DATE(STDAY, 'YYYYMMDD') AS
STDAY, RQST_NO      , CASE WHEN SUBSTR(STDAY,7, 2) < '15' THEN
LAST_DAY(ADD_MONTHS(STDAY,-2))             ELSE
LAST_DAY(ADD_MONTHS(STDAY,-1))        END AS STDAY_W      ,
SUBSTR(STDAY,7, 2) CPS_BSDD      , LAST_DAY(ADD_MONTHS(STDAY,-1))
STDAY_1      , LAST_DAY(ADD_MONTHS(STDAY,-2))  STDAY_2      ,
LAST_DAY(ADD_MONTHS(STDAY,-3))  STDAY_3      ,
LAST_DAY(ADD_MONTHS(STDAY,-4))  STDAY_4      ,
LAST_DAY(ADD_MONTHS(STDAY,-5))  STDAY_5      ,

LAST_DAY(ADD_MONTHS(STDAY,-6))  STDAY_6      ,
LAST_DAY(ADD_MONTHS(STDAY,-7))  STDAY_7      ,
LAST_DAY(ADD_MONTHS(STDAY,-8))  STDAY_8      ,
LAST_DAY(ADD_MONTHS(STDAY,-9))  STDAY_9      ,
LAST_DAY(ADD_MONTHS(STDAY,-10)) STDAY_10      ,
LAST_DAY(ADD_MONTHS(STDAY,-11)) STDAY_11      ,
LAST_DAY(ADD_MONTHS(STDAY,-12)) STDAY_12      ,
LAST_DAY(ADD_MONTHS(STDAY,-13))

Plan hash value: 300121676

------------------------------------------------------------------------------------------------------
| Id  | Operation                             | Name        | Starts | A-Rows |   A-Time   | Buffers |

------------------------------------------------------------------------------------------------------
|   0 | CREATE TABLE STATEMENT                |             |      1 |      0 |00:00:00.04 |      25 |
|   1 |  PX COORDINATOR                       |             |      1 |      0 |00:00:00.04 |      25 |
|   2 |   PX SEND QC (RANDOM)                 | :TQ10002    |      0 |      0 |00:00:00.01 |       0 |
|   3 |    LOAD AS SELECT (TEMP SEGMENT MERGE)| T_CTAS      |      0 |      0 |00:00:00.01 |       0 |
|   4 |     PX RECEIVE                        |             |      0 |      0 |00:00:00.01 |       0 |
|   5 |      PX SEND PARTITION (KEY)          | :TQ10001    |      0 |      0 |00:00:00.01 |       0 |
|   6 |       HASH GROUP BY                   |             |      0 |      0 |00:00:00.01 |       0 |
|   7 |        PX RECEIVE                     |             |      0 |      0 |00:00:00.01 |       0 |
|   8 |         PX SEND HASH                  | :TQ10000    |      0 |      0 |00:00:00.01 |       0 |
|   9 |          HASH GROUP BY                |             |      0 |      0 |00:00:00.01 |       0 |
|  10 |           PX BLOCK ITERATOR           |             |      0 |      0 |00:00:00.01 |       0 |
|* 11 |            TABLE ACCESS FULL          | TBIX00A_PRS |      0 |      0 |00:00:00.01 |       0 |

------------------------------------------------------------------------------------------------------

Outline Data
-------------

  /*+
      BEGIN_OUTLINE_DATA
      IGNORE_OPTIM_EMBEDDED_HINTS
      OPTIMIZER_FEATURES_ENABLE('21.1.0')
      DB_VERSION('21.1.0')
      ALL_ROWS
      OUTLINE_LEAF(@"SEL$1")
      FULL(@"SEL$1" "TBIX00A_PRS"@"SEL$1")

      GBY_PUSHDOWN(@"SEL$1")
      USE_HASH_AGGREGATION(@"SEL$1" GROUP_BY)
      END_OUTLINE_DATA
  */

Predicate Information (identified by operation id):
---------------------------------------------------

  11 - access(:Z>=:Z AND :Z<=:Z)
       filter("RQST_NO"=6144)

Note
-----

   - Degree of Parallelism is 4 because of table property


67 rows selected.

Elapsed: 00:00:00.07
SQL> SQL> Disconnected from Oracle Database 21c EE High Perf Release 21.0.0.0.0 - Production
Version 21.1.0.0.0
... run tkprof command
/u01/app/oracle/diag/rdbms/cdb21/CDB21/trace ~/kcb


TKPROF: Release 21.0.0.0.0 - Development on Wed Jan 27 23:05:14 2021

Copyright (c) 1982, 2020, Oracle and/or its affiliates.  All rights reserved.

Trace file: /u01/app/oracle/diag/rdbms/cdb21/CDB21/trace/CDB21_ora_33268_ok_xyz.trc
Sort options: default

********************************************************************************
count    = number of times OCI procedure was executed
cpu      = cpu time in seconds executing
elapsed  = elapsed time in seconds executing
disk     = number of physical reads of buffers from disk
query    = number of buffers gotten for consistent read
current  = number of buffers gotten in current mode (usually for update)
rows     = number of rows processed by the fetch or execute call
********************************************************************************
CREATE TABLE T_CTAS PCTFREE 0 PARALLEL 4 NOLOGGING STORAGE(CELL_FLASH_CACHE KEEP) PARTITION BY HASH(CUST_NO) PARTITIONS 64 COMPRESS FOR QUERY LOW
AS SELECT CUST_NO, TO_DATE(STDAY, 'YYYYMMDD') AS STDAY, RQST_NO
     , CASE WHEN SUBSTR(STDAY,7, 2) < '15' THEN LAST_DAY(ADD_MONTHS(STDAY,-2))
            ELSE LAST_DAY(ADD_MONTHS(STDAY,-1))
       END AS STDAY_W
     , SUBSTR(STDAY,7, 2) CPS_BSDD
     , LAST_DAY(ADD_MONTHS(STDAY,-1))  STDAY_1
     , LAST_DAY(ADD_MONTHS(STDAY,-2))  STDAY_2
     , LAST_DAY(ADD_MONTHS(STDAY,-3))  STDAY_3
     , LAST_DAY(ADD_MONTHS(STDAY,-4))  STDAY_4
     , LAST_DAY(ADD_MONTHS(STDAY,-5))  STDAY_5
     , LAST_DAY(ADD_MONTHS(STDAY,-6))  STDAY_6
     , LAST_DAY(ADD_MONTHS(STDAY,-7))  STDAY_7
     , LAST_DAY(ADD_MONTHS(STDAY,-8))  STDAY_8
     , LAST_DAY(ADD_MONTHS(STDAY,-9))  STDAY_9
     , LAST_DAY(ADD_MONTHS(STDAY,-10)) STDAY_10
     , LAST_DAY(ADD_MONTHS(STDAY,-11)) STDAY_11
     , LAST_DAY(ADD_MONTHS(STDAY,-12)) STDAY_12
     , LAST_DAY(ADD_MONTHS(STDAY,-13)) STDAY_13
     , LAST_DAY(ADD_MONTHS(STDAY,-14)) STDAY_14
     , LAST_DAY(ADD_MONTHS(STDAY,-15)) STDAY_15
  FROM TBIX00A_PRS
 WHERE RQST_NO = 6144
 GROUP BY CUST_NO, STDAY, RQST_NO

call     count       cpu    elapsed       disk      query    current        rows
------- ------  -------- ---------- ---------- ---------- ----------  ----------
Parse        1      0.00       0.00          0          0          0           0
Execute      1      0.05       0.09         72         90        412           0
Fetch        0      0.00       0.00          0          0          0           0
------- ------  -------- ---------- ---------- ---------- ----------  ----------
total        2      0.06       0.09         72         90        412           0


Misses in library cache during parse: 1
Optimizer mode: ALL_ROWS
Parsing user id: SYS
Number of plan statistics captured: 1

Rows (1st) Rows (avg) Rows (max)  Row Source Operation
---------- ---------- ----------  ---------------------------------------------------
         0          0          0  PX COORDINATOR  (cr=24 pr=0 pw=0 time=37483 us starts=1)
         0          0          0   PX SEND QC (RANDOM) :TQ10002 (cr=0 pr=0 pw=0 time=0 us starts=0 cost=310 size=17 card=1)
         0          0          0    LOAD AS SELECT (TEMP SEGMENT MERGE) T_CTAS (cr=0 pr=0 pw=0 time=0 us starts=0)
         0          0          0     PX RECEIVE  (cr=0 pr=0 pw=0 time=0 us starts=0 cost=310 size=17 card=1)
         0          0          0      PX SEND PARTITION (KEY) :TQ10001 (cr=0 pr=0 pw=0 time=0 us starts=0 cost=310 size=17 card=1)
         0          0          0       HASH GROUP BY (cr=0 pr=0 pw=0 time=0 us starts=0 cost=310 size=17 card=1)
         0          0          0        PX RECEIVE  (cr=0 pr=0 pw=0 time=0 us starts=0 cost=310 size=17 card=1)
         0          0          0         PX SEND HASH :TQ10000 (cr=0 pr=0 pw=0 time=0 us starts=0 cost=310 size=17 card=1)
         0          0          0          HASH GROUP BY (cr=0 pr=0 pw=0 time=0 us starts=0 cost=310 size=17 card=1)
         0          0          0           PX BLOCK ITERATOR PARTITION: 1 4 (cr=0 pr=0 pw=0 time=0 us starts=0 cost=310 size=17 card=1)
         0          0          0            TABLE ACCESS FULL TBIX00A_PRS PARTITION: 1 4 (cr=0 pr=0 pw=0 time=0 us starts=0 cost=310 size=17 card=1)


Elapsed times include waiting on following events:
  Event waited on                             Times   Max. Wait  Total Waited
  ----------------------------------------   Waited  ----------  ------------
  PX Deq: Join ACK                                8        0.00          0.00
  PX Deq: Parse Reply                             8        0.00          0.01
  PGA memory operation                            4        0.00          0.00
  PX Deq: Execute Reply                         104        0.00          0.01
  db file parallel read                          64        0.00          0.00
  Disk file operations I/O                        2        0.00          0.00
  db file scattered read                          1        0.00          0.00
  log file sync                                   1        0.00          0.00
  PX Deq: Signal ACK EXT                          8        0.00          0.00
  PX Deq: Slave Session Stats                     8        0.00          0.00
  enq: PS - contention                            1        0.00          0.00
  SQL*Net message to client                       1        0.00          0.00
  SQL*Net message from client                     1        0.00          0.00
********************************************************************************
...
```
