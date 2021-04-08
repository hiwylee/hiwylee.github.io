## SQL_PROFILE and SPM

* 동영상
  * [How to Use SQL Plan Baselines and SQL Profiles](https://www.youtube.com/watch?v=OJog42VkcBM&t=308s)
* 참조 블로그
  * [SQL_PROFILE을 통한 비효율SQL 문장 plan fix](https://redkite777.tistory.com/entry/오라클SQLPROFILE을-통한-비효율SQL-문장-plan-fix) 

### 실습
* sql profile
  * script spt.sql
  
```sql
DROP TABLE DEPT;

CREATE TABLE DEPT
       (DEPTNO NUMBER(2),
        DNAME VARCHAR2(14),
        LOC VARCHAR2(13) );

INSERT INTO DEPT VALUES (10, 'ACCOUNTING', 'NEW YORK');
INSERT INTO DEPT VALUES (20, 'RESEARCH',   'DALLAS');
INSERT INTO DEPT VALUES (30, 'SALES',      'CHICAGO');
INSERT INTO DEPT VALUES (40, 'OPERATIONS', 'BOSTON');

COMMIT;
/

CREATE UNIQUE INDEX COET.DEPT_U1 ON COET.DEPT (DEPTNO);
EXEC DBMS_STATS.GATHER_TABLE_STATS('COET', 'DEPT', CASCADE => TRUE);

EXPLAIN PLAN FOR
SELECT *
FROM   DEPT D
WHERE  D.DEPTNO = :B1
;
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(NULL, NULL, 'OUTLINE'));

EXPLAIN PLAN FOR
SELECT /*+ FULL(D) */
       *
FROM   DEPT D
WHERE  D.DEPTNO = :B1
;

---
var B1 NUMBER
EXEC :B1 := 10

SELECT *
FROM   DEPT D
WHERE  D.DEPTNO = :B1
;

---
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(NULL, NULL, 'OUTLINE'));


SELECT SQL_ID,
       SQL_TEXT,
       SQL_FULLTEXT
FROM   V$SQL
WHERE  SQL_TEXT LIKE '%DEPT D%'
AND  SQL_TEXT NOT LIKE 'EXPLAIN%'
AND    PARSING_SCHEMA_NAME = 'COET'
;
```

```
@spt
SQL> @spt

Table dropped.


Table created.


1 row created.


1 row created.


1 row created.


1 row created.


Commit complete.


Commit complete.


Index created.


PL/SQL procedure successfully completed.


Explained.


Plan hash value: 1124108434

---------------------------------------------------------------------------------------
| Id  | Operation                   | Name    | Rows  | Bytes | Cost (%CPU)| Time     |
---------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT            |         |     1 |    20 |     1   (0)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID| DEPT    |     1 |    20 |     1   (0)| 00:00:01 |
|*  2 |   INDEX UNIQUE SCAN         | DEPT_U1 |     1 |       |     0   (0)| 00:00:01 |
---------------------------------------------------------------------------------------

Outline Data
-------------


  /*+
      BEGIN_OUTLINE_DATA
      INDEX_RS_ASC(@"SEL$1" "D"@"SEL$1" ("DEPT"."DEPTNO"))
      OUTLINE_LEAF(@"SEL$1")
      ALL_ROWS
      DB_VERSION('11.2.0.4')
      OPTIMIZER_FEATURES_ENABLE('11.2.0.4')
      IGNORE_OPTIM_EMBEDDED_HINTS
      END_OUTLINE_DATA
  */

Predicate Information (identified by operation id):
---------------------------------------------------


   2 - access("D"."DEPTNO"=TO_NUMBER(:B1))

28 rows selected.


Explained.


PL/SQL procedure successfully completed.


        10 ACCOUNTING     NEW YORK


Plan hash value: 3383998547

--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      |     1 |    20 |     3   (0)| 00:00:01 |
|*  1 |  TABLE ACCESS FULL| DEPT |     1 |    20 |     3   (0)| 00:00:01 |
--------------------------------------------------------------------------

Outline Data
-------------

  /*+

      BEGIN_OUTLINE_DATA
      FULL(@"SEL$1" "D"@"SEL$1")
      OUTLINE_LEAF(@"SEL$1")
      ALL_ROWS
      DB_VERSION('11.2.0.4')
      OPTIMIZER_FEATURES_ENABLE('11.2.0.4')
      IGNORE_OPTIM_EMBEDDED_HINTS
      END_OUTLINE_DATA
  */

Predicate Information (identified by operation id):
---------------------------------------------------


   1 - filter("D"."DEPTNO"=TO_NUMBER(:B1))

27 rows selected.


9yb33yh2fhjun SELECT SQL_ID,        SQL_TEXT,        S SELECT SQL_ID,
              QL_FULLTEXT FROM   V$SQL WHERE  SQL_TEXT        SQL_TEXT,
               NOT LIKE 'EXPLAIN%' AND    SQL_TEXT LIK        SQL_FULLTEXT
              E '%DEPT D%' AND    PARSING_SCHEMA_NAME  FROM   V$SQL
              = 'COET'                                 WHERE  SQL_TEXT

6u0srtmzc90xu SELECT SQL_ID,        SQL_TEXT,        S SELECT SQL_ID,
              QL_FULLTEXT FROM   V$SQL WHERE  SQL_TEXT        SQL_TEXT,
               LIKE '%DEPT D%' AND  SQL_TEXT NOT LIKE         SQL_FULLTEXT
              'EXPLAIN%' AND    PARSING_SCHEMA_NAME =  FROM   V$SQL
              'COET'                                   WHERE  SQL_TEXT

01j9p2y4yk7av SELECT SQL_ID, --       SQL_TEXT,        SELECT SQL_ID,

               SQL_FULLTEXT FROM   V$SQL WHERE  SQL_TE --       SQL_TEXT,
              XT LIKE '%DEPT D%' --AND  SQL_TEXT NOT L        SQL_FULLTEXT
              IKE 'EXPLAIN%' AND    PARSING_SCHEMA_NAM FROM   V$SQL
              E = 'COET'                               WHERE  SQL_TE

a24m4v0qcuhh1 SELECT SQL_ID,        SQL_TEXT,        S SELECT SQL_ID,
              QL_FULLTEXT FROM   V$SQL WHERE  SQL_TEXT        SQL_TEXT,
               LIKE '%DEPT D%' --AND  SQL_TEXT NOT LIK        SQL_FULLTEXT
              E 'EXPLAIN%' AND    PARSING_SCHEMA_NAME  FROM   V$SQL
              = 'COET'                                 WHERE  SQL_TEXT

dgktmj5x7v7d5 SELECT SQL_ID,        SQL_TEXT,        S SELECT SQL_ID,
              QL_FULLTEXT FROM   V$SQL WHERE  SQL_TEXT        SQL_TEXT,

               LIKE '%DEPT D%'                                SQL_FULLTEXT
                                                       FROM   V$SQL
                                                       WHERE  SQL_TEXT

abfnv4rva7df9 SELECT * FROM   DEPT D WHERE  D.DEPTNO = SELECT *
               :B1                                     FROM   DEPT D
                                                       WHERE  D.DEPTNO = :B1


6 rows selected.

SQL>

```

* sql profile 생성 및 태스트

```sql
set head off
EXPLAIN PLAN FOR
SELECT *
FROM   DEPT D
WHERE  D.DEPTNO = :B1
;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(NULL,NULL, 'OUTLINE'));

prompt

DECLARE
    V_SQL_TEXT CLOB;
BEGIN
    SELECT SQL_FULLTEXT
    INTO   V_SQL_TEXT
    FROM   V$SQL
    --WHERE  SQL_ID = '21thr1v5tk9xm';
    WHERE  SQL_ID = '&1';

    DBMS_SQLTUNE.IMPORT_SQL_PROFILE(
        NAME        => 'DEPT_PROFILE_0',
        DESCRIPTION => 'DEPT_PROFILE_0',
        CATEGORY    => 'DEPT_PROFILE_0',
        SQL_TEXT    => V_SQL_TEXT,
        PROFILE     => SQLPROF_ATTR('BEGIN_OUTLINE_DATA',
                                    'FULL(@"SEL$1" "D"@"SEL$1")',
                                    'OUTLINE_LEAF(@"SEL$1")',
                                    'ALL_ROWS',
                                    'IGNORE_OPTIM_EMBEDDED_HINTS',
                                    'END_OUTLINE_DATA'
                                    ),
        REPLACE     => TRUE
    );
END;
/

alter session set sqltune_category=DEPT_PROFILE_0;

EXPLAIN PLAN FOR
SELECT *
FROM   DEPT D
WHERE  D.DEPTNO = :B1
;
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY(NULL,NULL, 'OUTLINE'));

BEGIN

    DBMS_SQLTUNE.DROP_SQL_PROFILE(NAME        => 'DEPT_PROFILE_0');
END;
/

```
