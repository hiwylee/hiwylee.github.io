### Partion 테이블에 병렬로 일련번호를 효율적으로 부여하는 방법
### 기본아이어디
* Query 에 rowmum을 주면 병렬처리가 아닌 순차처리를 하기 떄문에 성능이 저하됨
* 파티션 별로 시작 번호와 끝 번호에 대한 정보를 별도로 저장하고 파티션 별로 조인하여 순번을 부여

### 테스트
* base table   : h_p

```sql
 Name                                                                   Null?    Type
 ---------------------------------------------------------------------- -------- -----------------------------------------------
 CUST_NO                                                                         NUMBER
 NAME                                                                            VARCHAR2(44)
```

* 파티션 정보 및 건수 테이블
  * 검수 정보 테이블 : h_p_s

```
KCB@DB09021> desc h_p_s
 Name                                                                   Null?    Type
 ---------------------------------------------------------------------- -------- -----------------------------------------------
 TABLE_OWNER                                                                     VARCHAR2(128)
 TABLE_NAME                                                                      VARCHAR2(128)
 PART_NAME                                                                       VARCHAR2(128)
 PART_NUM                                                                        NUMBER
 BEGIN_NO                                                                        NUMBER
 ACCUM_CNT                                                                       NUMBER
```
#### 단계별 테스트
* 1) base table 생성 - hash partition 8

```sql
create /*+ parallel(8) */ table h_p nologging partition by hash(cust_no) partitions 8 
as select level as cust_no , 'xyz ' || level as name from dual connect by level < 240000;
 
 Wrote file afiedt.buf

  1   create /*+ parallel(8) */ table h_p nologging partition by hash(cust_no) partitions 8
  2*  as select level as cust_no , 'xyz ' || level as name from dual connect by level < 240000
SYS@DB09021> /
```
* 2)  h_p 파티션 확인

```sql
set linesize 128
col table_name for a30
col PARTITION_NAME for a30

select TABLE_NAME , PARTITION_NAME,PARTITION_POSITION  from dba_tab_partitions
   where TABLE_NAME = 'H_P'
     AND TABLE_OWNER = 'KCB'
     order by PARTITION_POSITION
	 ; 
KCB@DB09021>   2    3    4    5
TABLE_NAME                     PARTITION_NAME                 PARTITION_POSITION
------------------------------ ------------------------------ ------------------
H_P                            SYS_P1783                                       1
H_P                            SYS_P1784                                       2
H_P                            SYS_P1785                                       3
H_P                            SYS_P1786                                       4
H_P                            SYS_P1787                                       5
H_P                            SYS_P1788                                       6
H_P                            SYS_P1789                                       7
H_P                            SYS_P1790                                       8

8 rows selected.

Elapsed: 00:00:00.07
KCB@DB09021>
```

* 3) 파티션별로 시작 순번을 테이블로 저장 (rownum이 1 부터이므로 마지막 순번  - 1)
 
```sql
define part_cnt = 8

drop table h_p_s purge;
create table h_p_s as
select TABLE_OWNER, TABLE_NAME, PART_NAME, part_num , begin_no,accum_cnt
  from
	(SELECT TABLE_OWNER, TABLE_NAME, PARTITION_NAME as PART_NAME, PARTITION_POSITION 
	  from dba_tab_partitions
	  WHERE TABLE_NAME = 'H_P'
	    AND TABLE_OWNER = 'KCB'
	) x,
	(  
	select part_num,
		   -- nvl(lag(cum_cnt) over (order by part_num) + 1, 1) begin_no
		   -- rownum 은 1 부터 시작.
		   cum_cnt as accum_cnt,
		   nvl(lag(cum_cnt) over (order by part_num) , 0) begin_no
	from   (
			select part_num,
				   sum(cnt) over (order by part_num rows between unbounded preceding and current row) as cum_cnt
				   
			from   (
					select ora_hash(cust_no, &&part_cnt-1)+1 as part_num,
						   count(*) cnt
					from   h_p
					group by ora_hash(cust_no, &&part_cnt-1)+1
				   )
		   )
	fetch first &&part_cnt rows only
	) y
 WHERE x.PARTITION_POSITION = y.part_num
 order by part_num
/
```

```sql
col table_name for a30
col PART_NAME for a30
col TABLE_OWNER for a30

select * from  h_p_s;
KCB@DB09021>
TABLE_OWNER                    TABLE_NAME                     PART_NAME                        PART_NUM   BEGIN_NO  ACCUM_CNT
------------------------------ ------------------------------ ------------------------------ ---------- ---------- ----------
KCB                            H_P                            SYS_P1783                               1          0      30172
KCB                            H_P                            SYS_P1784                               2      30172      60488
KCB                            H_P                            SYS_P1785                               3      60488      90538
KCB                            H_P                            SYS_P1786                               4      90538     120496
KCB                            H_P                            SYS_P1787                               5     120496     150245
KCB                            H_P                            SYS_P1788                               6     150245     180144
KCB                            H_P                            SYS_P1789                               7     180144     210221
KCB                            H_P                            SYS_P1790                               8     210221     239999



8 rows selected.

Elapsed: 00:00:00.01
```


* >> partion 별 데이터 언로드 
  * unload 생성 SQL script

```sql
select 'SELECT /*+ NO_PARALLEL */ rownum + b.begin_no, a.* FROM  ' || TABLE_NAME || ' PARTITION (' ||   PARTITION_NAME || ') a , h_p_s b where b.part_name = ''' ||   PARTITION_NAME  ||  ''';'  from dba_tab_partitions
   where TABLE_NAME = 'H_P'
     AND TABLE_OWNER = 'KCB'
     order by PARTITION_POSITION; 
```
* >> partiton 1.  - last 10 rows

```sql

SELECT /*+ NO_PARALLEL */ rownum + b.begin_no as no, a.* FROM  H_P PARTITION (SYS_P1783) a , h_p_s b
 where b.part_name = 'SYS_P1783'
   and b.table_owner = 'KCB'
   and b.TABLE_NAME = 'H_P'
 offset 30162 rows fetch first 10 rows only;

        NO    CUST_NO NAME
---------- ---------- ----------------------------------------------------------------------------------------
     30163     239946 xyz 239946
     30164     239955 xyz 239955
     30165     239959 xyz 239959
     30166     239971 xyz 239971
     30167     239974 xyz 239974
     30168     239976 xyz 239976
     30169     239979 xyz 239979
     30170     239982 xyz 239982
     30171     239987 xyz 239987
     30172     239991 xyz 239991
```
* >> partiton 2.  first 10 rows

```sql
SELECT /*+ NO_PARALLEL */ rownum + b.begin_no as no , a.* FROM  H_P PARTITION (SYS_P1784) a , h_p_s b
 where b.part_name = 'SYS_P1784'
   and b.table_owner = 'KCB'
   and b.TABLE_NAME = 'H_P'
 offset 0 rows fetch first 10 rows only
   ;
        NO    CUST_NO NAME
---------- ---------- ----------------------------------------------------------------------------------------
     30173         10 xyz 10
     30174         26 xyz 26
     30175         28 xyz 28
     30176         31 xyz 31
     30177         32 xyz 32
     30178         52 xyz 52
     30179         67 xyz 67
     30180         69 xyz 69
     30181         70 xyz 70
     30182         86 xyz 86
```

*  >> partiton 8.  last 10 rows

```sql
SELECT /*+ NO_PARALLEL */ rownum + b.begin_no as no , a.* FROM  H_P PARTITION (SYS_P1790) a , h_p_s b
 where b.part_name = 'SYS_P1790'
   and b.table_owner = 'KCB'
   and b.TABLE_NAME = 'H_P'
 offset 0 rows fetch first 10 rows only 

        NO    CUST_NO NAME
---------- ---------- ------------------------------
    210222          1 xyz 1
    210223          7 xyz 7
    210224         14 xyz 14
    210225         15 xyz 15
    210226         25 xyz 25
    210227         29 xyz 29
    210228         38 xyz 38
    210229         45 xyz 45
    210230         57 xyz 57
    210231         59 xyz 59
```

