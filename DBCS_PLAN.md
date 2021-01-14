## DBMS_XPLAN
### DBMS_XPLAN.DISPLAY_CURSOR
* 기본 사용법 
 * https://theone79.tistory.com/865
 * [Oracle Database - Explain Plan from Cursor Cache (DBMS_XPLAN.DISPLAY_CURSOR)](https://datacadamia.com/db/oracle/display_cursor#dbms_xplandisplay_cursor)
 
### 테스트 환경 

* env.sql

```sql
alter session enable parallel query;
alter session enable parallel dml;
alter session enable parallel ddl;

alter session force parallel ddl parallel 4;
alter session force parallel dml parallel 4;
alter session force parallel query parallel 4;

--alter session set statistics_level=typical;
--alter session set "_rowsource_execution_statistics"=false;

```
* r_base.sql

```sql
@env.sql

drop table R_base purge;

set timing on
create table R_base   nologging tablespace users
as
select empno, salary, deptno,
       lpad(big_ename, 3000, big_ename) as big_ename,
       lpad(big_addr, 3000, big_addr) as big_addr
from ( select level + 10000000 as empno,
              mod(level,1000) + 10000 as salary,
              mod(level,20) as deptno,
              chr(97+mod(level,26)) as big_ename,
              chr(65+mod(level,26)) as big_addr
       from dual
       connect by level <= 100000
     )
;

```
* norecycle.sql

'''sql
@env.sql
alter session set statistics_level=typical;
alter session set "_rowsource_execution_statistics"=false;

alter session set recyclebin=off;

show parameter recyclebin;

drop table R_off purge;

set timing on
create table R_off nologging tablespace users
as
select * from r_base
;
```


* recycle.sql
```sql
@env

alter session set recyclebin=on;

show parameter recyclebin;
drop table R_on purge;

set timing on
create table R_On   nologging tablespace users
as
select * from r_base
;

```
