
* https://oracle-base.com/articles/misc/pipelined-table-functions
* http://www.oracle-developer.net/display.php?id=429

```sql
SELECT * FROM TABLE(ST_MON_F(CURSOR(SELECT * FROM CUST));
ST_MON_F
{
       ARRAY_LIST OF ST_MON
       FETCH CUST_cur 
            BULK COLLECT INTO l_CUST LIMIT limit_in;     // 100,000건
			FOR indx IN 1 .. l_CUST.COUNT 
			LOOP
			    ST_MON_F_List
				if l_CUST(indx)).ST_DAY ;
				ST_MON_F_List
			END LOOP;
}
				FOR indx2 IN 1 .. ST_MON_F_List.COUNT 
				LOOP
					ST_MON_F_List
					if l_CUST(indx)).ST_DAY <  ST_MON_F_List(indx2)).ST_DAY <= l_CUST(indx)).ED_DAY
						out_rec.x := ST_MON_F_List(indx2)).ST_DAY;
						out_rec.y := ST_MON_F_List(indx2)).ST_DAY;
						out_rec.z := ST_MON_F_List(indx2)).ST_DAY;
						PIPE ROW(out_rec);					   
					END IF    
				END LOOP;

ST_MON_F_List

TYPE 필요 : OUT_REC, IN_REC
ST_MON : TABLE OF ST_MON <= SINGLE TONE



출처: https://argolee.tistory.com/40 [놀멍]

출처: https://argolee.tistory.com/40 [놀멍]



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
