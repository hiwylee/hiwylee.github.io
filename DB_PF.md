
* https://oracle-base.com/articles/misc/pipelined-table-functions
* http://www.oracle-developer.net/display.php?id=429

### TEST
#### ENV 
* TABLE
```sql
drop table PRI purge;
drop table ST_MON purge;

CREATE TABLE PRI
nologging
PARTITION BY HASH (CUST_NO)
PARTITIONS 32
AS
SELECT 'id' || level AS CUST_NO,'id'||level AS id0 , 'id'||level AS id1 , 'id'||level AS id2
FROM   dual
CONNECT BY level <= 1000000;

create table ST_MON
nologging
AS
SELECT 'id' || level AS id0, 'id'||level AS id1 , 'id'||level AS id2
FROM   dual
CONNECT BY level <= 52;

INSERT /*+ APPEND */ INTO PRI (SELECT * FROM PRI);
commit;
INSERT /*+ APPEND */ INTO PRI (SELECT * FROM PRI);
commit;

```

#### Pipelined function
* Head
```sql
CREATE OR REPLACE PACKAGE PF AS

  TYPE ret_row_type IS RECORD (
    id0   ST_MON.id0%TYPE,
    id1   ST_MON.id0%TYPE,
    id2   ST_MON.id0%TYPE
  );


  TYPE ret_tab_type IS TABLE OF ret_row_type ;

  TYPE pri_ref_cursor IS REF CURSOR RETURN PRI%ROWTYPE;


  FUNCTION pf_func4 (
    p_pri_cursor in pri_ref_cursor
  )
  RETURN ret_tab_type PIPELINED
  PARALLEL_ENABLE(PARTITION p_pri_cursor BY HASH (CUST_NO));

END PF;
/

CREATE OR REPLACE PACKAGE BODY PF AS

  FUNCTION pf_func4 (
    p_pri_cursor in pri_ref_cursor
  )
  RETURN ret_tab_type PIPELINED
  PARALLEL_ENABLE(PARTITION p_pri_cursor BY HASH (CUST_NO))
  IS

    TYPE v_ret IS RECORD (
      id0   ST_MON.id0%TYPE,
      id1   ST_MON.id0%TYPE,
      id2   ST_MON.id0%TYPE
    );

    -- for ST_MON cursor
    TYPE sty_ref_cursor IS REF CURSOR RETURN ST_MON%ROWTYPE;
    CURSOR p_sty_cursor IS SELECT * FROM ST_MON;

    -- for fetch st_mon bulk into
    TYPE stmon_tab_type IS TABLE OF ST_MON%ROWTYPE INDEX BY PLS_INTEGER;
    v_rec_l stmon_tab_type := stmon_tab_type() ;

    -- pri
    TYPE pri_tab_type IS TABLE OF PRI%ROWTYPE  INDEX BY PLS_INTEGER;

    v_pri_row PRI%ROWTYPE;
    v_pri_tab pri_tab_type;

    v_ret_row ret_row_type := ret_row_type();
    v_ret_tab ret_tab_type := ret_tab_type();


    v_cnt number := 0;
    v_sub number :=  52 ;
    v_max number :=  1000000;


  BEGIN

 --DBMS_OUTPUT.ENABLE('1000000000');
 --  DBMS_OUTPUT.PUT_LINE( 'BEGIN' );


    -- ST_MON
    OPEN p_sty_cursor;
    LOOP   -- ST_MON
      FETCH p_sty_cursor BULK COLLECT INTO v_rec_l  ;
      EXIT WHEN p_sty_cursor%NOTFOUND;
    END LOOP;
    CLOSE p_sty_cursor;

    for i in 1..v_rec_l.count loop
       v_rec_l(i).id0 := 'id' || i;
       v_rec_l(i).id1 := 'id' || i;
       v_rec_l(i).id2 := 'id' || i;
       DBMS_OUTPUT.PUT_LINE( v_rec_l(i).id0);
    end loop;


--    DBMS_OUTPUT.PUT_LINE( 'STEP 1' );

    v_sub := 0;
    LOOP   -- ST_MON
      v_sub := v_sub + 1;
      FETCH p_pri_cursor BULK COLLECT INTO v_pri_tab limit 100000 ;
      DBMS_OUTPUT.PUT_LINE( 'STEP 1' );
      FOR k in v_pri_tab.first..v_pri_tab.last LOOP
--          DBMS_OUTPUT.PUT_LINE( 'STEP LOOPING' );
         -- check pri is in st_mon
         v_cnt := 1;
         FOR i in 1..v_rec_l.count LOOP
            v_cnt := v_cnt + 1;
            IF (   v_pri_tab(k).cust_no = v_rec_l(i).id0
                or v_pri_tab(k).cust_no  = v_rec_l(i).id1
                or v_pri_tab(k).cust_no  = v_rec_l(i).id2)  then
                v_cnt := v_cnt + 1;
                -- PIPE ROW(rec_row_type(v_rec_l(i).id0,v_rec_l(i).id1,v_rec_l(i).id2));
                PIPE ROW(ret_row_type('cnt = ' || k ||'/' || i ,v_rec_l(i).id1,v_rec_l(i).id2));
             end if;
         end loop;
      END LOOP;
      EXIT WHEN p_pri_cursor%NOTFOUND;
    END LOOP;

--    DBMS_OUTPUT.PUT_LINE( 'END' );
  END;
END PF;
/

```

#### Test
* Perf 

```sql
SYS@odidb2> !cat ft41.sql

alter session force parallel QUERY parallel 16;

select  count(*)
  from TABLE(pf.pf_func4(CURSOR(SELECT * FROM PRI)));

select count(*)
  from pri p, st_mon s
 where (case when (p.cust_no = s.id0 or p.cust_no = s.id1 or p.cust_no = s.id2) then 1 else 0 end) = 1;

```
#####  ``백만건``
```sql

SYS@odidb2> @ft41

Session altered.

Elapsed: 00:00:00.00

  COUNT(*)
----------
        52

1 row selected.

Elapsed: 00:00:05.23

  COUNT(*)
----------
        52

1 row selected.

Elapsed: 00:00:01.51
SYS@odidb2>

```
##### ``4백만건``
```sql
SYS@odidb2> @ft42

Session altered.

Elapsed: 00:00:00.00

Function created.

Elapsed: 00:00:00.01
Pipeline function : 589824

PL/SQL procedure successfully completed.

Elapsed: 00:00:19.56
Nomarl sql : 393216

PL/SQL procedure successfully completed.

Elapsed: 00:00:05.66

```

##### ``8백만건``
```
SYS@odidb2> @ft42

Session altered.

Elapsed: 00:00:00.00

Function created.

Elapsed: 00:00:00.01
Pipeline function : 196608

PL/SQL procedure successfully completed.

Elapsed: 00:00:37.79
Nomarl sql : 262144

PL/SQL procedure successfully completed.

Elapsed: 00:00:52.46

```

##### ``천육백만건`` (fetch size 10000)

```sql
SYS@odidb2> @ft42

Session altered.

Elapsed: 00:00:00.00

Function created.

Elapsed: 00:00:00.00
Pipeline function : 196608

PL/SQL procedure successfully completed.

Elapsed: 00:01:16.31
Nomarl sql : 131072

PL/SQL procedure successfully completed.

Elapsed: 00:01:20.24

```
* PGA
```sql
alter session force parallel QUERY parallel 16;

CREATE OR REPLACE FUNCTION get_stat (p_stat IN VARCHAR2) RETURN NUMBER AS
  l_return  NUMBER;
BEGIN
  SELECT ms.value
  INTO   l_return
  FROM   v$mystat ms,
         v$statname sn
  WHERE  ms.statistic# = sn.statistic#
  AND    sn.name = p_stat;
  RETURN l_return;
END get_stat;
/

SET SERVEROUTPUT ON

DECLARE
  l_start  NUMBER;
BEGIN
  l_start := get_stat('session pga memory');

  FOR cur_rec IN (SELECT *
                 from TABLE(pf.pf_func4(CURSOR(SELECT * FROM PRI))))
  LOOP
    NULL;
  END LOOP;

  DBMS_OUTPUT.put_line('Pipeline function : ' ||
                        (get_stat('session pga memory') - l_start));
END;
/


DECLARE
  l_start  NUMBER;
BEGIN
  l_start := get_stat('session pga memory');

  FOR cur_rec IN (SELECT p.*
                    from pri p, st_mon s
                   where (case when (p.cust_no = s.id0 or p.cust_no = s.id1 or p.cust_no = s.id2) then 1 else 0 end) = 1)
  LOOP
    NULL;
  END LOOP;

  DBMS_OUTPUT.put_line('Nomarl sql : ' ||
                        (get_stat('session pga memory') - l_start));
END;
/

```


### TEST
* PROTOTYPE PF 2

```sql
DROP TYPE rec_tab_type;
DROP TYPE rec_row_type;

CREATE TYPE rec_row_type AS OBJECT (
    id0   VARCHAR2(30),
    id1   VARCHAR2(30),
    id2   VARCHAR2(30)
  );

/ed ins4.sql

CREATE TYPE rec_tab_type IS TABLE OF rec_row_type ; -- INDEX BY PLS_INTEGER;
/

CREATE OR REPLACE FUNCTION pf_func3(
  p_pri in number default 1000,
  p_sty in number default 52,
  p_param IN varchar
)
RETURN rec_tab_type PIPELINED
-- PARALLEL_ENABLE(PARTITION parameter-name BY [{HASH | RANGE} (column-list) | ANY ]) IS

AS

   v_test VARCHAR2(100);

   TYPE v_rec IS RECORD (
    id0   VARCHAR2(35),
    id1   VARCHAR2(35),
    id2   VARCHAR2(35)
  );

  TYPE v_tab_type IS TABLE OF v_rec INDEX BY PLS_INTEGER;

  v_rec_l v_tab_type := v_tab_type() ;

  v_cnt number := 0;
  v_sub number :=  p_sty ;
  v_max number :=  p_pri;

BEGIN

    for i in 1..v_sub loop
       v_rec_l(i).id0 := 'id' || i;
       v_rec_l(i).id1 := 'id' || i;
       v_rec_l(i).id2 := 'id' || i;
    end loop;
    --for j in 1..v_rec_l.count loop
    for k in 1..v_max loop
       v_cnt := v_cnt + 1;
       if v_cnt = 52 then
          v_cnt := 1;
       end if;
       -- PIPE ROW(rec_row_type(p_param,v_rec_l(v_cnt).id1,v_rec_l(v_cnt).id2));
       for i in 1..v_rec_l.count loop
          if (p_param = v_rec_l(v_cnt).id0  or p_param = v_rec_l(v_cnt).id1 or p_param = v_rec_l(v_cnt).id2)  then
              v_cnt := v_cnt + 1;
              -- PIPE ROW(rec_row_type(v_rec_l(i).id0,v_rec_l(i).id1,v_rec_l(i).id2));
              PIPE ROW(rec_row_type('cnt = ' || k ||'/' || i ,v_rec_l(i).id1,v_rec_l(i).id2));
           end if;
       end loop;

    end loop;
END;
/
~

```

```sql

alter session force parallel QUERY parallel 8;

select max(id0) from TABLE(pf_func3(p_pri=>1000000, p_sty=> 52, p_param=>'id1'));
```

* PROTOTYPE PF
```sql
DROP TYPE rec_tab_type;
DROP TYPE rec_row_type;

CREATE TYPE rec_row_type AS OBJECT (
    id0   VARCHAR2(5),
    id1   VARCHAR2(5),
    id2   VARCHAR2(5)
  );

/

CREATE TYPE rec_tab_type IS TABLE OF rec_row_type ; -- INDEX BY PLS_INTEGER;
/

CREATE OR REPLACE FUNCTION pf_func (p_param IN varchar) RETURN rec_tab_type PIPELINED AS

   v_test VARCHAR2(100);

   TYPE v_rec IS RECORD (
    id0   VARCHAR2(5),
    id1   VARCHAR2(5),
    id2   VARCHAR2(5)
  );

  TYPE v_tab_type IS TABLE OF v_rec INDEX BY PLS_INTEGER;

  v_rec_l v_tab_type := v_tab_type() ;

  cnt number;

BEGIN

    cnt := 0;
    for i in 1..51 loop
       v_rec_l(i).id0 := 'id' || i;
       v_rec_l(i).id1 := 'id' || i;
       v_rec_l(i).id2 := 'id' || i;
    end loop;

       PIPE ROW(rec_row_type('id0', 'id2','id2'));

    for j in 1..v_rec_l.count loop
       PIPE ROW(rec_row_type(v_rec_l(j).id0,v_rec_l(j).id1,v_rec_l(j).id2));
       if (p_param = v_rec_l(j).id0  or p_param = v_rec_l(j).id1 or p_param = v_rec_l(j).id2)  then
         cnt := cnt + 1;
         for i in 1..v_rec_l.count loop
            PIPE ROW(rec_row_type(v_rec_l(i).id0,v_rec_l(i).id1,v_rec_l(i).id2));
         end loop;
       end if;

    end loop;
END;
/


```

```sql
select * from TABLE(pf_func('id0'));
```

```sql
GRANT EXECUTE ONdmbmnimpTO PUBLIC WITH GRANT OPTION;
```
```sql
SELECT * FROM TABLE(ST_MON_F(CURSOR(SELECT * FROM CUST), CURSOR(SELECT * FROM ST_MON));
ST_MON_F
{

       FETCH ST_MON_cur 
            BULK COLLECT INTO l_ST_MON;
       FETCH CUST_cur 
            BULK COLLECT INTO l_CUST LIMIT limit_in;     // 100,000건
			FOR indx IN 1 .. l_CUST.COUNT 
			LOOP
			    ST_MON_F_List
				FOR indx2 IN 1 .. l_CUST.COUNT 
				LOOP
					if l_CUST(indx)).ST_DAY <  l_ST_MON(indx2)).ST_DAY <= l_CUST(indx)).ED_DAY
						out_rec.x := ST_MON_F_List(indx2)).ST_DAY;
						out_rec.y := ST_MON_F_List(indx2)).ST_DAY;
						out_rec.z := ST_MON_F_List(indx2)).ST_DAY;
						PIPE ROW(out_rec);					   
					END IF    
				END LOOP;
			END LOOP;
ST_MON_F_List

TYPE 필요 : OUT_REC, IN_REC
ST_MON : TABLE OF ST_MON <= SINGLE TONE



출처: https://argolee.tistory.com/40 [놀멍]

```

* bulk pipe row
```sql
create or replace package body mypkg
as
   function execute_query(startNode in varchar2) RETURN node PIPELINED
    AS
        results node;
        my_query VARCHAR2(100);
        output VARCHAR2(1000);
        c sys_refcursor;
    BEGIN -- don't use concatenation, it leads to sql injections:
        my_query := 'SELECT DISTINCT * FROM EDGES WHERE src=:startNode';
        -- use bind variables and bind them using cluase "using":
        open c for my_query using startNode;
        loop
            fetch c bulk collect into results limit 100;
            -- "results" is a collection, so you need to iterate it to pipe rows:
            for i in 1..results.count loop
                PIPE Row(results(i));
            end loop;
            exit when c%notfound;
        end loop;
        close c;
    END;
end;
/
```
```sql

1) bulk fetch
/////////////////////////////////////////////////////////////////
Fetching from the Results of Table Functions
    OPEN employees_cur;
    LOOP
        FETCH employees_cur 
            BULK COLLECT INTO l_employees LIMIT limit_in;

        FOR indx IN 1 .. l_employees.COUNT 
        LOOP
            analyze_compensation (l_employees(indx));
        END LOOP;

        EXIT WHEN l_employees.COUNT < limit_in;

   END LOOP;


출처: https://argolee.tistory.com/40 [놀멍]


 

OPEN c FOR SELECT * FROM TABLE(f(...));

Cursors over table functions have the same fetch semantics as ordinary cursors. REF CURSOR assignments based on table functions do not have any special semantics.

However, the SQL optimizer will not optimize across PL/SQL statements. For example:

BEGIN
    OPEN r FOR SELECT * FROM TABLE(f(CURSOR(SELECT * FROM tab)));
    SELECT * BULK COLLECT INTO rec_tab FROM TABLE(g(r));
END;


1) REF CURSOR
1) Parallel 
CREATE FUNCTION function-name(parameter-name ref-cursor-type)
  RETURN rec_tab_type PIPELINED
  PARALLEL_ENABLE(PARTITION parameter-name BY [{HASH | RANGE} (column-list) | ANY ]) IS
BEGIN
  ...
END;


------------
CREATE OR REPLACE PACKAGE parallel_ptf_api AS

  TYPE t_parallel_test_row IS RECORD (
    id             NUMBER(10),
    country_code   VARCHAR2(5),
    description    VARCHAR2(50),
    sid            NUMBER
  );

  TYPE t_parallel_test_tab IS TABLE OF t_parallel_test_row;

  TYPE t_parallel_test_ref_cursor IS REF CURSOR RETURN parallel_test%ROWTYPE;
  
  FUNCTION test_ptf_any (p_cursor  IN  t_parallel_test_ref_cursor)
    RETURN t_parallel_test_tab PIPELINED
    PARALLEL_ENABLE(PARTITION p_cursor BY ANY);
    
  FUNCTION test_ptf_hash (p_cursor  IN  t_parallel_test_ref_cursor)
    RETURN t_parallel_test_tab PIPELINED
    PARALLEL_ENABLE(PARTITION p_cursor BY HASH (country_code));
    
  FUNCTION test_ptf_range (p_cursor  IN  t_parallel_test_ref_cursor)
    RETURN t_parallel_test_tab PIPELINED
    PARALLEL_ENABLE(PARTITION p_cursor BY RANGE (country_code));
    
END parallel_ptf_api;
/

CREATE OR REPLACE PACKAGE BODY parallel_ptf_api AS

  FUNCTION test_ptf_any (p_cursor  IN  t_parallel_test_ref_cursor)
    RETURN t_parallel_test_tab PIPELINED
    PARALLEL_ENABLE(PARTITION p_cursor BY ANY)
  IS
    l_row  t_parallel_test_row;
  BEGIN
    LOOP
      FETCH p_cursor
      INTO  l_row.id,
            l_row.country_code,
            l_row.description;
      EXIT WHEN p_cursor%NOTFOUND;
      
      SELECT sid
      INTO   l_row.sid
      FROM   v$mystat
      WHERE  rownum = 1;
      
      PIPE ROW (l_row);
    END LOOP;
    RETURN;
  END test_ptf_any;

  FUNCTION test_ptf_hash (p_cursor  IN  t_parallel_test_ref_cursor)
    RETURN t_parallel_test_tab PIPELINED
    PARALLEL_ENABLE(PARTITION p_cursor BY HASH (country_code))
  IS
    l_row  t_parallel_test_row;
  BEGIN
    LOOP
      FETCH p_cursor
      INTO  l_row.id,
            l_row.country_code,
            l_row.description;
      EXIT WHEN p_cursor%NOTFOUND;
      
      SELECT sid
      INTO   l_row.sid
      FROM   v$mystat
      WHERE  rownum = 1;
      
      PIPE ROW (l_row);
    END LOOP;
    RETURN;
  END test_ptf_hash;

  FUNCTION test_ptf_range (p_cursor  IN  t_parallel_test_ref_cursor)
    RETURN t_parallel_test_tab PIPELINED
    PARALLEL_ENABLE(PARTITION p_cursor BY RANGE (country_code))
  IS
    l_row  t_parallel_test_row;
  BEGIN
    LOOP
      FETCH p_cursor
      INTO  l_row.id,
            l_row.country_code,
            l_row.description;
      EXIT WHEN p_cursor%NOTFOUND;
      
      SELECT sid
      INTO   l_row.sid
      FROM   v$mystat
      WHERE  rownum = 1;
      
      PIPE ROW (l_row);
    END LOOP;
    RETURN;
  END test_ptf_range;
      
END parallel_ptf_api;
/
-------------------------
```
