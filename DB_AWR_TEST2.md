## 실행 시간이 일정하지 않은 SQL 원인 분석
### 문제 접근 방법
* 해당 시간대(비교 시간대) awr ash addm 리포트 분석
* 문제 sql의 시간대별 plan 변경 여부 확인 
* 문제 sql_id 식별
* 문제 sql_id 의 시간대별 통계 변화 확인
* Top 30 SQL
 * ![](http://www.dba-oracle.com/images/awr_sql_tables.jpg)
### 문제 sql_id 의 시간대별 통계 변화 확인

```sql
col module format a30
col begin format a22
set pagesize 50
select sql_id, module,
      TO_CHAR(b.begin_interval_time,'MM/DD/YYYY HH24:MI:SS') "begin",
       -- b.begin_interval_time,
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
where a.sql_id = '0qv27wt724y7s'
  and a.snap_id  = b.snap_id
  and a.dbid = b.dbid
  and b.instance_number = 1
--  and b.begin_interval_time between to_timestamp('20110701','YYYYMMDD') and to_timestamp('2012','YYYY')
  order by a.snap_id;

SQL_ID        MODULE                         begin                  BUFFER_GETS DISK_READS     FETCHS ROWS_PROCESSED ELAPSED_TIME     IOWAIT     APWAIT     CLWAIT     CCWAIT EXECUTIONS
------------- ------------------------------ ---------------------- ----------- ---------- ---------- -------------- ------------ ---------- ---------- ---------- ---------- ----------
0qv27wt724y7s                                01/23/2021 03:00:13              0          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 04:00:22              0          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 04:00:22              0          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 05:00:25              0          0          1              0            0          0          0          0          0          4
0qv27wt724y7s                                01/23/2021 05:00:25              0          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 06:00:38              2          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 06:00:38              3          0          1              0            0          0          0          0          0          4
0qv27wt724y7s                                01/23/2021 07:00:49              0          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 07:00:49              0          0          1              0            0          0          0          0          0          4
0qv27wt724y7s                                01/23/2021 08:00:55              0          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 08:00:55              0          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 09:00:02              0          0          1              0            0          0          0          0          0          4
0qv27wt724y7s                                01/23/2021 09:00:02              0          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 10:00:10              3          0          1              0            0          0          0          0          0          4
0qv27wt724y7s                                01/23/2021 10:00:10              2          0          1              0            0          0          0          0          0          6
0qv27wt724y7s                                01/23/2021 11:00:17              0          0          1              0            0          0          0          0          0          6

```

###  sql plan 

```sql 
col plan format a100

select sql_id,lpad(' ',depth*4,'  ')||' '||operation|| ' ' ||options|| ' '
 ||object_name|| ' (' ||cost||')'plan, to_char(timestamp,'YYYY-MM-DD HH24:MI:SS') as "date"
   from DBA_HIST_SQL_PLAN
where sql_id in ('0qv27wt724y7s')
order by timestamp,sql_id,plan_hash_value, id;

SQL> @awr_4

SQL_ID        PLAN                                                                                                 date
------------- ---------------------------------------------------------------------------------------------------- -------------------
0qv27wt724y7s  SELECT STATEMENT   (4)                                                                              2020-09-04 22:16:56
0qv27wt724y7s      MERGE JOIN OUTER  (4)                                                                           2020-09-04 22:16:56
0qv27wt724y7s          HASH JOIN OUTER  (3)                                                                        2020-09-04 22:16:56
0qv27wt724y7s              NESTED LOOPS OUTER  (1)                                                                 2020-09-04 22:16:56
0qv27wt724y7s                  NESTED LOOPS OUTER  (1)                                                             2020-09-04 22:16:56
0qv27wt724y7s                      FILTER   ()                                                                     2020-09-04 22:16:56
0qv27wt724y7s                          MERGE JOIN OUTER  (1)                                                       2020-09-04 22:16:56
0qv27wt724y7s                              TABLE ACCESS BY INDEX ROWID SCHEDULER$_LIGHTWEIGHT_JOB (0)              2020-09-04 22:16:56
0qv27wt724y7s                                  INDEX FULL SCAN SCHEDULER$_LWJOB_PK (0)                             2020-09-04 22:16:56
0qv27wt724y7s                              SORT JOIN  (1)                                                          2020-09-04 22:16:56
0qv27wt724y7s                                  PX COORDINATOR   ()                                                 2020-09-04 22:16:56
0qv27wt724y7s                                      PX SEND QC (RANDOM) :TQ10000 (0)                                2020-09-04 22:16:56
0qv27wt724y7s                                          VIEW  GV$SCHEDULER_INMEM_RTINFO ()                          2020-09-04 22:16:56
0qv27wt724y7s                                              FIXED TABLE FULL X$JSKMIMRT (0)                         2020-09-04 22:16:56
0qv27wt724y7s                      TABLE ACCESS BY INDEX ROWID SCHEDULER$_CLASS (0)                                2020-09-04 22:16:56
0qv27wt724y7s                          INDEX UNIQUE SCAN SCHEDULER$_CLASS_PK (0)                                   2020-09-04 22:16:56
0qv27wt724y7s                  TABLE ACCESS BY INDEX ROWID SCHEDULER$_JOB (0)                                      2020-09-04 22:16:56
0qv27wt724y7s                      INDEX UNIQUE SCAN SCHEDULER$_JOB_PK (0)                                         2020-09-04 22:16:56
0qv27wt724y7s              TABLE ACCESS FULL SERVICE$ (2)                                                          2020-09-04 22:16:56
0qv27wt724y7s          BUFFER SORT  (2)                                                                            2020-09-04 22:16:56
0qv27wt724y7s              VIEW  VW_LAT_F3D67240 (1)                                                               2020-09-04 22:16:56
0qv27wt724y7s                  VIEW  VW_ORE_4CF31DA3 (1)                                                           2020-09-04 22:16:56
0qv27wt724y7s                      UNION-ALL   ()                                                                  2020-09-04 22:16:56
0qv27wt724y7s                          TABLE ACCESS BY INDEX ROWID SCHEDULER$_PROGRAM (0)                          2020-09-04 22:16:56
0qv27wt724y7s                              INDEX UNIQUE SCAN SCHEDULER$_PROGRAM_PK (0)                             2020-09-04 22:16:56
0qv27wt724y7s                          FILTER   ()                                                                 2020-09-04 22:16:56
0qv27wt724y7s                              TABLE ACCESS BY INDEX ROWID SCHEDULER$_PROGRAM (1)                      2020-09-04 22:16:56
0qv27wt724y7s                                  INDEX UNIQUE SCAN SCHEDULER$_PROGRAM_PK (0)                         2020-09-04 22:16:56

28 rows selected.

```

### sql plan with chaild _number

```sql
select p.plan_table_output
  from (select distinct sql_id, child_number
          from v$sql_plan s
         where s.address = '' or
               s.sql_id = '0qv27wt724y7s') s,
        table(dbms_xplan.display_cursor (s.sql_id, s.child_number, 'typical')) p;

SQL_ID  0qv27wt724y7s, child number 6
-------------------------------------
SELECT /*+ NO_STATEMENT_QUEUING RESULT_CACHE (SYSOBJ=TRUE SHELFLIFE=30)
*/ "OBJ#","CLASS_OID","JOB_FLAGS","CLASS_FLAGS","RUN_TIME","PRIORITY","J

PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
OB_STATUS","RUNNING_INSTANCE","SCHEDULE_LIMIT","JOB_WEIGHT","INSTANCE_ID
","AFFINITY","SERVICE_FLAGS" FROM "SYS"."SCHEDULER$_LWJOB_REFRESH"
"SCHEDULER$_LWJOB_REFRESH" WHERE 1=1

Plan hash value: 3051189468

---------------------------------------------------------------------------------------------------------------------------------------------
| Id  | Operation                         | Name                       | Rows  | Bytes | Cost (%CPU)| Time     |    TQ  |IN-OUT| PQ Distrib |
---------------------------------------------------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                  |                            |       |       |     4 (100)|          |        |      |            |
|   1 |  MERGE JOIN OUTER                 |                            |     1 |   300 |     4  (25)| 00:00:01 |        |      |            |
|*  2 |   HASH JOIN OUTER                 |                            |     1 |   261 |     3  (34)| 00:00:01 |        |      |            |
|   3 |    NESTED LOOPS OUTER             |                            |     1 |   233 |     1 (100)| 00:00:01 |        |      |            |
|   4 |     NESTED LOOPS OUTER            |                            |     1 |   228 |     1 (100)| 00:00:01 |        |      |            |
|*  5 |      FILTER                       |                            |       |       |            |          |        |      |            |
|   6 |       MERGE JOIN OUTER            |                            |     1 |   195 |     1 (100)| 00:00:01 |        |      |            |
|   7 |        TABLE ACCESS BY INDEX ROWID| SCHEDULER$_LIGHTWEIGHT_JOB |     1 |   121 |     0   (0)|          |        |      |            |
|   8 |         INDEX FULL SCAN           | SCHEDULER$_LWJOB_PK        |     1 |       |     0   (0)|          |        |      |            |
|*  9 |        SORT JOIN                  |                            |     1 |    74 |     1 (100)| 00:00:01 |        |      |            |
|* 10 |         PX COORDINATOR            |                            |       |       |            |          |        |      |            |
|  11 |          PX SEND QC (RANDOM)      | :TQ10000                   |     1 |    87 |            |          |  Q1,00 | P->S | QC (RAND)  |
|* 12 |           VIEW                    | GV$SCHEDULER_INMEM_RTINFO  |       |       |            |          |  Q1,00 | PCWP |            |
|* 13 |            FIXED TABLE FULL       | X$JSKMIMRT                 |     1 |    87 |            |          |  Q1,00 | PCWP |            |
|  14 |      TABLE ACCESS BY INDEX ROWID  | SCHEDULER$_CLASS           |     1 |    43 |     0   (0)|          |        |      |            |
|* 15 |       INDEX UNIQUE SCAN           | SCHEDULER$_CLASS_PK        |     1 |       |     0   (0)|          |        |      |            |
|  16 |     TABLE ACCESS BY INDEX ROWID   | SCHEDULER$_JOB             |     1 |    15 |     0   (0)|          |        |      |            |
|* 17 |      INDEX UNIQUE SCAN            | SCHEDULER$_JOB_PK          |     1 |       |     0   (0)|          |        |      |            |
|  18 |    TABLE ACCESS FULL              | SERVICE$                   |     1 |    28 |     2   (0)| 00:00:01 |        |      |            |
|  19 |   BUFFER SORT                     |                            |     2 |    78 |     2  (50)| 00:00:01 |        |      |            |
|  20 |    VIEW                           | VW_LAT_F3D67240            |     2 |    78 |     1   (0)| 00:00:01 |        |      |            |
|  21 |     VIEW                          | VW_ORE_4CF31DA3            |     2 |    78 |     1   (0)| 00:00:01 |        |      |            |
|  22 |      UNION-ALL                    |                            |       |       |            |          |        |      |            |
|  23 |       TABLE ACCESS BY INDEX ROWID | SCHEDULER$_PROGRAM         |     1 |    12 |     0   (0)|          |        |      |            |
|* 24 |        INDEX UNIQUE SCAN          | SCHEDULER$_PROGRAM_PK      |     1 |       |     0   (0)|          |        |      |            |
|* 25 |       FILTER                      |                            |       |       |            |          |        |      |            |
|  26 |        TABLE ACCESS BY INDEX ROWID| SCHEDULER$_PROGRAM         |     1 |    12 |     1   (0)| 00:00:01 |        |      |            |
|* 27 |         INDEX UNIQUE SCAN         | SCHEDULER$_PROGRAM_PK      |     1 |       |     0   (0)|          |        |      |            |
---------------------------------------------------------------------------------------------------------------------------------------------

Predicate Information (identified by operation id):
---------------------------------------------------

   2 - access(LOWER("C"."AFFINITY")=CASE  WHEN (ROWID IS NOT NULL) THEN LOWER("NAME"||'.'||SYS_CONTEXT('USERENV','DB_DOMAIN')) ELSE
              NULL END )
   5 - filter((BITAND(DECODE(BITAND("L"."FLAGS",17592186044416),0,"L"."JOB_STATUS",BITAND(DECODE(BITAND("L"."JOB_STATUS",1),0,4294967
              294,4294967295),"JOB_STATUS")),515)=1 AND SYS_EXTRACT_UTC(DECODE(BITAND("L"."FLAGS",16384),0,DECODE(BITAND("L"."FLAGS",17592186044416
              ),0,"L"."NEXT_RUN_DATE","NEXT_RUN_DATE"),"L"."LAST_ENABLED_TIME"))<SYS_EXTRACT_UTC(SYSTIMESTAMP(6)+INTERVAL'+00 00:30:00' DAY(2) TO

PLAN_TABLE_OUTPUT
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
              SECOND(0)) AND (BITAND("L"."FLAGS",402653184)=0 OR BITAND(DECODE(BITAND("L"."FLAGS",17592186044416),0,"L"."JOB_STATUS",BITAND(DECODE(
              BITAND("L"."JOB_STATUS",1),0,4294967294,4294967295),"JOB_STATUS")),1024)<>0)))
   9 - access("L"."OBJ#"="OBJID")
       filter("L"."OBJ#"="OBJID")
  10 - filter((INTERNAL_FUNCTION("CON_ID") AND NVL("CON_ID",0)=TO_NUMBER(NVL(SYS_CONTEXT('USERENV','CON_ID'),'0'))))
  12 - filter((INTERNAL_FUNCTION("CON_ID") AND NVL("CON_ID",0)=TO_NUMBER(NVL(SYS_CONTEXT('USERENV','CON_ID'),'0'))))
  13 - filter((INTERNAL_FUNCTION("CON_ID") AND NVL("CON_ID",0)=TO_NUMBER(NVL(SYS_CONTEXT('USERENV','CON_ID'),'0'))))
  15 - access("L"."CLASS_OID"="C"."OBJ#")
  17 - access("L"."PROGRAM_OID"="PJ"."OBJ#")
  24 - access("P"."OBJ#"="L"."PROGRAM_OID")
  25 - filter("PJ"."PROGRAM_OID" IS NOT NULL)
  27 - access("P"."OBJ#"="PJ"."PROGRAM_OID")
       filter(LNNVL("P"."OBJ#"="L"."PROGRAM_OID"))
.........


1236 rows selected.

SQL>

```

### sql hist 

```sql
select
   to_char(s.begin_interval_time,'MM/DD/YYYY HH24:MI:SS') "begin",
   to_char(s.end_interval_time,'MM/DD/YYYY HH24:MI:SS')   "end",
   --s.begin_interval_time,
   --s.end_interval_time ,
   q.snap_id,
   q.dbid,
   q.sql_id,
   q.plan_hash_value,
   q.optimizer_cost,
   q.optimizer_mode
from
   dba_hist_sqlstat q,
   dba_hist_snapshot s
where
   1=1 -- q.dbid = nnnnnnn
and q.sql_id = '0qv27wt724y7s'
and q.snap_id = s.snap_id
and s.begin_interval_time between sysdate-2 and sysdate
-- and rownum < 10
order by s.snap_id desc
/

egin                  end                    SNAP_ID       DBID SQL_ID        PLAN_HASH_VALUE OPTIMIZER_COST OPTIMIZER_
---------------------- ------------------- ---------- ---------- ------------- --------------- -------------- ----------
01/22/2021 18:00:08    01/22/2021 19:00:13       3415 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 18:00:08    01/22/2021 19:00:13       3415 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 18:00:08    01/22/2021 19:00:13       3415 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 17:00:02    01/22/2021 18:00:08       3414 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 17:00:02    01/22/2021 18:00:08       3414 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 17:00:02    01/22/2021 18:00:08       3414 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 17:00:02    01/22/2021 18:00:08       3414 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 16:00:10    01/22/2021 17:00:02       3413 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 16:00:10    01/22/2021 17:00:02       3413 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 16:00:10    01/22/2021 17:00:02       3413 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 16:00:10    01/22/2021 17:00:02       3413 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE
01/22/2021 15:00:46    01/22/2021 16:00:10       3412 3013874817 0qv27wt724y7s      3051189468              4 CHOOSE

```


### Top 30 SQL

```sql
WITH TMP_SQLSTAT_HIST AS(
SELECT /*+ LEADING(X B) USE_NL(B) USE_HASH(A) FULL(B) */
       B.DBID, B.SQL_ID, B.INSTANCE_NUMBER
     , TO_CHAR(END_INTERVAL_TIME, 'YYYYMMDD:HH24MISS') SNAP_DATE
     , MAX(PARSING_SCHEMA_NAME) PARSING_SCHEMA_NAME
     , B.PLAN_HASH_VALUE
     , MAX(MODULE) MODULE
     , SUM(EXECUTIONS_DELTA) EXECUTIONS
     , SUM(BUFFER_GETS_DELTA) BUFFER_GETS
     , ROUND(SUM(BUFFER_GETS_DELTA) / DECODE(SUM(EXECUTIONS_DELTA), 0, 1, SUM(EXECUTIONS_DELTA))) EXEC_BUFFER_GETS
     , SUM(DISK_READS_DELTA) DISK_READS
     , ROUND(SUM(DISK_READS_DELTA) / DECODE(SUM(EXECUTIONS_DELTA), 0, 1, SUM(EXECUTIONS_DELTA))) EXEC_DISK_READS
     , SUM(ROWS_PROCESSED_DELTA) ROWS_PROCESSED
     , ROUND(SUM(ROWS_PROCESSED_DELTA) / DECODE(SUM(EXECUTIONS_DELTA), 0, 1, SUM(EXECUTIONS_DELTA))) EXEC_ROWS
     , SUM(CPU_TIME_DELTA) CPU_TIME
     , ROUND(SUM(CPU_TIME_DELTA) / DECODE(SUM(EXECUTIONS_DELTA), 0, 1, SUM(EXECUTIONS_DELTA)) / 1000000, 6) EXEC_CPU_TIME
     , SUM(CLWAIT_DELTA) CLUSTER_WAIT_TIME
     , ROUND(SUM(CLWAIT_DELTA) / DECODE(SUM(EXECUTIONS_DELTA), 0, 1, SUM(EXECUTIONS_DELTA)) / 1000000, 6) EXEC_CLWAIT_TIME
     , SUM(ELAPSED_TIME_DELTA) ELAPSED_TIME
     , ROUND(SUM(ELAPSED_TIME_DELTA) / DECODE(SUM(EXECUTIONS_DELTA), 0, 1, SUM(EXECUTIONS_DELTA)) / 1000000, 6) EXEC_ELAPSED_TIME
     , ROUND(MAX(EXECUTIONS_DELTA) / 3600, 3) EXEC_FOR_SEC
     , ROW_NUMBER() OVER(PARTITION BY B.DBID, B.SQL_ID ORDER BY TO_CHAR(END_INTERVAL_TIME, 'YYYYMMDD:HH24MISS') DESC
     , SUM(BUFFER_GETS_DELTA) DESC) RNK
     , MAX(DECODE(B.FORCE_MATCHING_SIGNATURE,0,NULL,B.FORCE_MATCHING_SIGNATURE)) FORCE_MATCHING_SIGNATURE
  FROM (SELECT /*+ NO_MERGE */
               DBID, MIN(SNAP_ID) MIN_SNAP_ID, MAX(SNAP_ID) MAX_SNAP_ID
          FROM SYS.WRM$_SNAPSHOT --DBA_HIST_SNAPSHOT --SQL 실행 구간
         WHERE 1 = 1
         GROUP BY DBID) X,    --DBA_HIST_SQLSTAT과 조인 시 해당 파티션만 SCAN하기 위해 만든 집합임
       SYS.WRM$_SNAPSHOT A,   --DBA_HIST_SNAPSHOT
       SYS.WRH$_SQLSTAT B     --DBA_HIST_SQLSTAT과
 WHERE X.DBID = B.DBID
   AND B.SNAP_ID BETWEEN X.MIN_SNAP_ID AND X.MAX_SNAP_ID
   AND A.DBID = B.DBID
   AND A.SNAP_ID = B.SNAP_ID
   AND A.INSTANCE_NUMBER = B.INSTANCE_NUMBER
   AND A.END_INTERVAL_TIME BETWEEN SYSDATE-7 AND SYSDATE
   AND NVL(B.PARSING_SCHEMA_NAME,'-') NOT IN ('SYS','SYSMAN','DBSNMP','SYSTEM','EXFSYS')
   AND NOT REGEXP_LIKE(NVL(B.MODULE,'-'), 'Orange|SQL Developer|SQLGate|Data Pump|TOAD|golden|ERwin|PL.SQL Developer|SQL Loader|oracle|DBMS_SCHEDULER', 'i')
   AND PLAN_HASH_VALUE > 0
   AND MODULE IS NOT NULL
 GROUP BY B.DBID, B.SQL_ID, B.INSTANCE_NUMBER, B.PLAN_HASH_VALUE, TO_CHAR(END_INTERVAL_TIME, 'YYYYMMDD:HH24MISS')
)
SELECT --같거나 비슷한 SQL은 같은 GROUP으로 표현
       DENSE_RANK() OVER(ORDER BY FORCE_MATCHING_SIGNATURE) SQL_GRP_TYPE
     , A.DBID
     , A.INSTANCE_NUMBER    --최종 수행된 INSTANCE
     , A.SNAP_DATE          --최종 수행 일자
     , A.SQL_ID             --SQL_ID
     , A.PLAN_HASH_VALUE    --실행 계획에 종속적인 값
     , A.MODULE             --실행 모듈
     , A.EXECUTIONS         --총 실행수
     , A.EXEC_ROWS          --실행당 결과 건수
     , A.EXEC_BUFFER_GETS   --실행당 BUFFER_GET
     , A.BUFFER_GETS        --총 BUFFER_GET
     , A.EXEC_DISK_READS    --실행당 DISK_READ
     , A.EXEC_ELAPSED_TIME  --실행당 수행 시간
     , A.EXEC_CPU_TIME      --실행당 CPU 시간
     , A.EXEC_FOR_SEC       --초당 실행수, 특정 시간에만 집중적으로 수행되는 SQL 판별위함
     , A.ELAPSED_TIME       --총 수행시간
     , A.CPU_TIME           --총 CPU 시간
     , A.CLUSTER_WAIT_TIME  --총 CLUSTER 대기 시간
     , DECODE(A.CPU_TIME,0,0,ROUND(A.CPU_TIME / A.ELAPSED_TIME, 2)) CPU_RATE -- 수행시간 대비 CPU 시간 비율
  FROM (
        SELECT SNAP_DATE, DBID, INSTANCE_NUMBER, SQL_ID, PLAN_HASH_VALUE, MODULE
             , EXECUTIONS, EXEC_ROWS, EXEC_BUFFER_GETS, BUFFER_GETS, EXEC_DISK_READS
             , ELAPSED_TIME, CPU_TIME, CLUSTER_WAIT_TIME
             , EXEC_ELAPSED_TIME, EXEC_CPU_TIME, EXEC_FOR_SEC
             , FORCE_MATCHING_SIGNATURE
             , RANK() OVER(PARTITION BY DBID ORDER BY EXECUTIONS DESC) EXECUTIONS_RNK
             , RANK() OVER(PARTITION BY DBID ORDER BY BUFFER_GETS DESC) BUFFER_GETS_RNK
             , RANK() OVER(PARTITION BY DBID ORDER BY EXEC_CPU_TIME DESC) EXEC_CPU_TIME_RNK
             , RANK() OVER(PARTITION BY DBID ORDER BY EXEC_BUFFER_GETS DESC) EXEC_BUFFER_GETS_RNK
          FROM TMP_SQLSTAT_HIST
) A,
       DBA_HIST_SQLTEXT B
 WHERE A.DBID = B.DBID
   AND A.SQL_ID = B.SQL_ID
   AND (A.EXECUTIONS_RNK <= 30 OR     --실행수 TOP 30
        A.BUFFER_GETS_RNK <= 30 OR    --BUFFER_GET TOP 30
        A.EXEC_BUFFER_GETS_RNK <= 30 )  --실행당 BUFFER_GET TOP 30
ORDER BY SNAP_DATE DESC
;
```
