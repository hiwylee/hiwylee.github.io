## Automatic Indexing
* https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=576&p210_type=3&session=8714429437393

### setup for test
* exdata 흉내내기 : "_exadata_feature_on"=true
```sql
sqlplus / as sysdba <<EOF

alter system set "_exadata_feature_on"=true scope=spfile;
shutdown immediate;
startup;

exit;
EOF
```
*  _exadata_feature_on 
```sql
sqlplus / as sysdba <<EOF

alter system reset "_exadata_feature_on" scope=spfile;
shutdown immediate;
startup;

exit;
EOF
```
### auto indexing test
* enable auto index 
  * OFF : disables automatic indexing in a database so that no new auto indexes are created, and the existing auto indexes are disabled.
  * IMPLEMENT : enables automatic indexing in a database and creates any new auto indexes as visible indexes so that they can be used in SQL statements.
  * REPORT ONLY : enables automatic indexing in a database, but creates any new auto indexes as invisible indexes, so that they cannot be used in SQL statements.
```sql
SQL> ED
Wrote file afiedt.buf

  1* SELECT name FROM V$DATAFILE
SQL> /

NAME
------------------------------------------------------------------------------------------------------------------------
/u01/app/oracle/oradata/ORCL/orclpdb/system01.dbf
/u01/app/oracle/oradata/ORCL/orclpdb/sysaux01.dbf
/u01/app/oracle/oradata/ORCL/orclpdb/undotbs01.dbf
/u01/app/oracle/oradata/ORCL/orclpdb/users01.dbf
/u01/app/oracle/oradata/ORCL/orclpdb/tbs_auto_idx01.dbf

SQL> exec DBMS_AUTO_INDEX.CONFIGURE('AUTO_INDEX_DEFAULT_TABLESPACE','TBS_AUTO_IDX');

PL/SQL procedure successfully completed.

SQL>

```
* View configuration details.

```sql
SQL> select * from DBA_AUTO_INDEX_CONFIG;

PARAMETER_NAME                      PARAMETER_VALUE                LAST_MODIFIED                  MODIFIED_BY
----------------------------------- ------------------------------ ------------------------------ --------------------
AUTO_INDEX_COMPRESSION              OFF
AUTO_INDEX_DEFAULT_TABLESPACE       TBS_AUTO_IDX                   01-SEP-20 11.35.50.000000 AM   SYS
AUTO_INDEX_MODE                     OFF
AUTO_INDEX_REPORT_RETENTION         31
AUTO_INDEX_RETENTION_FOR_AUTO       373
AUTO_INDEX_RETENTION_FOR_MANUAL
AUTO_INDEX_SCHEMA
AUTO_INDEX_SPACE_BUDGET             50

8 rows selected.
SQL> exec DBMS_AUTO_INDEX.CONFIGURE('AUTO_INDEX_SCHEMA', 'OE', TRUE);

PL/SQL procedure successfully completed.

SQL> exec DBMS_AUTO_INDEX.CONFIGURE('AUTO_INDEX_SCHEMA', 'SH', TRUE);

PL/SQL procedure successfully completed.

SQL> select * from DBA_AUTO_INDEX_CONFIG;

PARAMETER_NAME                      PARAMETER_VALUE                LAST_MODIFIED                  MODIFIED_BY
----------------------------------- ------------------------------ ------------------------------ --------------------
AUTO_INDEX_COMPRESSION              OFF
AUTO_INDEX_DEFAULT_TABLESPACE       TBS_AUTO_IDX                   01-SEP-20 11.35.50.000000 AM   SYS
AUTO_INDEX_MODE                     OFF
AUTO_INDEX_REPORT_RETENTION         31
AUTO_INDEX_RETENTION_FOR_AUTO       373
AUTO_INDEX_RETENTION_FOR_MANUAL
AUTO_INDEX_SCHEMA                   schema IN (OE, SH) AND schema  01-SEP-20 11.43.09.000000 AM   SYS
                                    NOT IN (HR)

AUTO_INDEX_SPACE_BUDGET             50

8 rows selected.

SQL> set linesize 120 trims on pagesize 1000 long 100000

column REPORT format a120

select DBMS_AUTO_INDEX.REPORT_ACTIVITY(sysdate-30,NULL,'text','all','all') REPORT from DUAL;SQL> SQL> SQL> SQL>

REPORT
------------------------------------------------------------------------------------------------------------------------
GENERAL INFORMATION
-------------------------------------------------------------------------------
 Activity start               : 02-AUG-2020 11:44:01
 Activity end                 : 01-SEP-2020 11:44:01
 Executions completed         : 0
 Executions interrupted       : 0
 Executions with fatal error  : 0
-------------------------------------------------------------------------------

SUMMARY (AUTO INDEXES)
-------------------------------------------------------------------------------
 Index candidates            : 0
 Indexes created             : 0
 Space used                  : 0 B
 Indexes dropped             : 0
 SQL statements verified     : 0
 SQL statements improved     : 0
 SQL plan baselines created  : 0
 Overall improvement factor  : 0x
-------------------------------------------------------------------------------

SUMMARY (MANUAL INDEXES)
-------------------------------------------------------------------------------
 Unused indexes    : 0
 Space used        : 0 B
 Unusable indexes  : 0
-------------------------------------------------------------------------------

ERRORS
---------------------------------------------------------------------------------------------
No errors found.
---------------------------------------------------------------------------------------------


```
* Step 4:Run a workload
```sql
[oracle@workshop ~]$ sqlplus sh/Ora_DB4U@localhost:1521/orclpdb

SQL*Plus: Release 19.0.0.0.0 - Production on Tue Sep 1 11:45:28 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

Last Successful login time: Mon Aug 31 2020 11:35:20 +00:00

Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.7.0.0.0

SQL> drop table temp_ai purge;

create table temp_ai(c number, d varchar2(1000));
Table dropped.

SQL> SQL>

Table created.

SQL>
SQL>
SQL>
SQL>
SQL>
SQL>
SQL>
SQL>
SQL> begin
  2    for i in 1..20000 loop
  3      insert into temp_ai values(-i,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
  end loop;
  commit;
  4    5    6  end;
/  7

PL/SQL procedure successfully completed.

SQL> drop table customers_ai purge;

create table customers_ai as select * from sh.customers;
Table dropped.

SQL> SQL>

Table created.

SQL> execute dbms_stats.gather_schema_stats(ownname => 'SH', estimate_percent=> DBMS_STATS.AUTO_SAMPLE_SIZE, method_opt => 'FOR ALL COLUMNS SIZE  AUTO', degree => 4);

PL/SQL procedure successfully completed.

SQL>

```
* Step 5: View Advisor Tasks
```sql
set lines 100

column task_name format a32
column description format a28
column advisor_name format a28
column execution_start format a18
column execution_end format a18
column status format a12

select task_name,description,advisor_name,execution_start,status
from dba_advisor_tasks;
SQL> /

TASK_NAME                        DESCRIPTION                  ADVISOR_NAME                 EXECUTION_START    STATUS
-------------------------------- ---------------------------- ---------------------------- ------------------ ------------
SYS_AUTO_SPM_EVOLVE_TASK         Automatic SPM Evolve Task    SPM Evolve Advisor           01-SEP-20          COMPLETED
SYS_AI_SPM_EVOLVE_TASK           Automatic SPM Evolve Task    SPM Evolve Advisor                              INITIAL
SYS_AI_VERIFY_TASK                                            SQL Performance Analyzer                        INITIAL
SYS_AUTO_INDEX_TASK                                           SQL Access Advisor                              INITIAL
AUTO_STATS_ADVISOR_TASK                                       Statistics Advisor           01-SEP-20          COMPLETED
INDIVIDUAL_STATS_ADVISOR_TASK                                 Statistics Advisor                              INITIAL

6 rows selected.
SQL> select to_char(execution_start, 'DD-MM-YY HH24:MI:SS') execution_start,
  to_char(execution_end, 'DD-MM-YY HH24:MI:SS') execution_end,
  status
from dba_advisor_executions where task_name='SYS_AUTO_INDEX_TASK';  2    3    4

no rows selected



```

* Step 6: Generate Workload
```sql
SQL>
SQL> begin
for i in 1..20 loop
  FOR sales_data IN (
  SELECT ch.channel_class, c.cust_city, t.calendar_quarter_desc, SUM(s.amount_sold) sales_amount
  2    3    4    5    FROM sh.sales s, sh.times t, sh.customers c, sh.channels ch
  6    WHERE s.time_id = t.time_id AND s.cust_id = c.cust_id AND s.channel_id = ch.channel_id
  AND c.cust_state_province = 'CA' AND ch.channel_desc in ('Internet','Catalog')
  AND t.calendar_quarter_desc IN ('1999-01','1999-02')
  7    8    9    GROUP BY ch.channel_class, c.cust_city, t.calendar_quarter_desc)
 10    LOOP
 11      DBMS_OUTPUT.PUT_LINE('Sales data: ' || sales_data.channel_class || ' ' || sales_data.cust_city || ' '  || sales_data.calendar_quarter_desc || ' ' || sales_data.sales_amount);
 12    END LOOP;
 13  end loop;
 14  end;
/ 15

...
Sales data: Indirect Pescadero 1999-02 298.44
Sales data: Indirect Cloverdale 1999-02 266.28

PL/SQL procedure successfully completed.

Elapsed: 00:00:00.76


```
```sql
begin
  for i in 1..20 loop
    FOR sales_data IN (
    SELECT c.country_id, c.cust_city, c.cust_last_name
    FROM sh.customers c
    WHERE c.country_id in (52790, 52798)
    ORDER BY c.country_id, c.cust_city, c.cust_last_name)
    LOOP  
      DBMS_OUTPUT.PUT_LINE('Sales data: ' || sales_data.country_id || ' ' || sales_data.cust_city || ' '  || sales_data.cust_last_name);
    END LOOP;
  end loop;
end;
/
```
```sql
begin
for i in 1..20 loop
  FOR sales_data IN (
  SELECT ch.channel_class, c.cust_city, t.calendar_quarter_desc, SUM(s.amount_sold) sales_amount
  FROM sh.sales s, sh.times t, sh.customers c, sh.channels ch
  WHERE s.time_id = t.time_id AND s.cust_id = c.cust_id AND s.channel_id = ch.channel_id
  AND c.cust_state_province = 'CA' AND ch.channel_desc in ('Internet','Catalog')
  AND t.calendar_quarter_desc IN ('1999-03','1999-04')
  GROUP BY ch.channel_class, c.cust_city, t.calendar_quarter_desc)
  LOOP  
    DBMS_OUTPUT.PUT_LINE('Sales data: ' || sales_data.channel_class || ' ' || sales_data.cust_city || ' '  || sales_data.calendar_quarter_desc || ' ' || sales_data.sales_amount);
  END LOOP;
end loop;
end;
/
```
```sql
begin
  for i in 1..20 loop
    FOR sales_data IN (
    select /* func_indx */ count(*) howmany from temp_ai where abs(c)=5)
    LOOP  
      DBMS_OUTPUT.PUT_LINE('Sales data: ' || sales_data.howmany);
    END LOOP;
  end loop;
end;
/
```
```sql
begin
  for i in 1..20 loop
    FOR sales_data IN (
      SELECT * FROM customers_ai WHERE cust_state_province = 'CA')
      LOOP  
      DBMS_OUTPUT.PUT_LINE('Sales data: ' || sales_data.CUST_FIRST_NAME || ' ' || sales_data.CUST_LAST_NAME || ' '  || sales_data.CUST_EMAIL);
      END LOOP;
    end loop;
end;
/
```

* Step 7: Calculate a sales projection
```sql
SQL> drop table currency purge;

Table dropped.

Elapsed: 00:00:00.03
SQL> CREATE TABLE currency (
country         VARCHAR2(20),
year            NUMBER,
month           NUMBER,
to_us           NUMBER);  2    3    4    5

Table created.

Elapsed: 00:00:00.01
SQL>
```
```sql
INSERT INTO currency
(SELECT distinct
SUBSTR(country_name,1,20), calendar_year, calendar_month_number, 1
FROM countries
CROSS JOIN times t
WHERE calendar_year IN (2000,2001,2002)
);
```
```sql
UPDATE currency set to_us=.74 WHERE country='Canada';
```
```sql
WITH  prod_sales_mo AS
  ( SELECT country_name c, prod_id p, calendar_year  y,
    calendar_month_number  m, SUM(amount_sold) s
    FROM sales s, customers c, times t, countries cn, promotions p, channels ch
    WHERE  s.promo_id = p.promo_id AND p.promo_total_id = 1 AND
          s.channel_id = ch.channel_id AND ch.channel_total_id = 1 AND
          s.cust_id=c.cust_id  AND
          c.country_id=cn.country_id AND country_name='Canada' AND
          s.time_id=t.time_id  AND t.calendar_year IN  (2000, 2001,2002)
    GROUP BY cn.country_name, prod_id, calendar_year, calendar_month_number), time_summary AS( SELECT DISTINCT calendar_year cal_y,
                      calendar_month_number cal_m
                      FROM times
                      WHERE  calendar_year IN  (2000, 2001, 2002)
          )
SELECT c, p, y, m, s, nr FROM (
    SELECT c, p, y, m, s, nr
    FROM prod_sales_mo s
    PARTITION BY (s.c, s.p)
    RIGHT OUTER JOIN time_summary ts ON (s.m = ts.cal_m AND s.y = ts.cal_y )
MODEL
  REFERENCE curr_conversion ON
    (SELECT country, year, month, to_us
    FROM currency ORDER BY country,year,month)
  DIMENSION BY (country, year y,month m ) MEASURES (to_us)
  PARTITION BY (s.c c)
  DIMENSION BY (s.p p, ts.cal_y y, ts.cal_m m)
          MEASURES (s.s s, CAST(NULL AS NUMBER) nr, s.c cc )
  RULES ( nr[ANY, ANY, ANY] ORDER BY y, m ASC =
            CASE
              WHEN s[CV(), CV(), CV()] IS NOT NULL
              THEN s[CV(), CV(), CV()]
              ELSE ROUND(AVG(s)[CV(), CV(), m BETWEEN 1 AND 12],2)
            END,
      nr[ANY, 2002, ANY] ORDER BY y,m ASC =
        ROUND(((nr[CV(),2001,CV()] - nr[CV(),2000, CV()])/ nr[CV(),2000, CV()]) * nr[CV(),2001, CV()] + nr[CV(),2001,  CV()],2),
      nr[ANY,y != 2002,ANY] ORDER BY y,m ASC =
        ROUND(nr[CV(),CV(),CV()] * curr_conversion.to_us[ cc[CV(),CV(),CV()], CV(y), CV(m)], 2)
      )
ORDER BY c, p, y, m)
WHERE y = '2002'
ORDER BY c, p, y, m;
```
```sql
commit;
```
* Step 8: Automatic Indexing Results
```sql
SQL> show user
USER is "SYS"
```
```sql
select to_char(execution_start, 'DD-MM-YY HH24:MI:SS') execution_start,
to_char(execution_end, 'DD-MM-YY HH24:MI:SS') execution_end, status
from dba_advisor_executions where task_name='SYS_AUTO_INDEX_TASK';
```
```sql
select count(*)
from dba_indexes
where auto = 'YES'
  and visibility = 'VISIBLE'
  and status = 'VALID'
  and table_owner = 'SH';
```
```sql
set linesize 120

column table_name format a30
column  index_name format a30
column  index_type format a25
column  last_analyzed format a25

select table_name,index_name,index_type,last_analyzed
from dba_indexes where table_owner = 'SH';
```
```sql
set linesize 120 trims on pagesize 1000 long 100000

column REPORT format a120

select DBMS_AUTO_INDEX.REPORT_ACTIVITY(sysdate-30, NULL, 'text', 'all', 'all') REPORT from DUAL;
```
```sql
```


