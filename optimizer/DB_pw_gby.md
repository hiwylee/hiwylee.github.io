## Partition-Wise Operations – New Features in 12c and 18c
* 참조 : [링크](https://antognini.ch/2018/05/partition-wise-operations-new-features-in-12c-and-18c/)

### 연습
### 필요 스키마 생성

* 
```
CREATE TABLE t (
  id NUMBER,
  d1 DATE,
  n1 NUMBER,
  n2 NUMBER,
  n3 NUMBER,
  pad VARCHAR2(4000),
  CONSTRAINT t_pk PRIMARY KEY (id)
)
PARTITION BY RANGE (d1)
SUBPARTITION BY LIST (n1)
SUBPARTITION TEMPLATE (
  SUBPARTITION sp_1 VALUES (1),
  SUBPARTITION sp_2 VALUES (2),
  SUBPARTITION sp_3 VALUES (3),
  SUBPARTITION sp_4 VALUES (4)
)(
  PARTITION t_q1_2018 VALUES LESS THAN (to_date('2018-04-01 00:00:00','YYYY-MM-DD HH24:MI:SS')),
  PARTITION t_q2_2018 VALUES LESS THAN (to_date('2018-07-01 00:00:00','YYYY-MM-DD HH24:MI:SS')),
  PARTITION t_q3_2018 VALUES LESS THAN (to_date('2018-10-01 00:00:00','YYYY-MM-DD HH24:MI:SS')),
  PARTITION t_q4_2018 VALUES LESS THAN (to_date('2019-01-01 00:00:00','YYYY-MM-DD HH24:MI:SS'))
);

INSERT INTO t
SELECT rownum AS id,
       trunc(to_date('2018-01-01','YYYY-MM-DD')+rownum/27.4) AS d1,
       1+mod(rownum,4) AS n1,
       rownum AS n2,
       rownum AS n3,
       rpad('*',100,'*') AS pad
FROM dual
CONNECT BY level <= 10000;

BEGIN
  dbms_stats.gather_table_stats(
    ownname          => user,
    tabname          => 'T'
  );
END;
/
``
