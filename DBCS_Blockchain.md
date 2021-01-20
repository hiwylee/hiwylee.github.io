## BLOCKCHAIN TABLE
### Basic Usage

* Table Creation - 일반 테이블 생성 문법을 실행하면 오류 발생

```sql
SQL> /
create blockchain table ledger_emp(employee_id number , salary number)
                                                                     *
ERROR at line 1:
ORA-00905: missing keyword

```

* 

```sql
SQL>
    CREATE BLOCKCHAIN TABLE ledger_emp (employee_id NUMBER, salary NUMBER)
    no drop until 2 days idle
    no delete locked
    hashing using "SHA2_512" version "v1" 
    /

Table created.

SQL> COL "Data Length" FORMAT 9999
SQL> COL "Column Name" FORMAT A24
SQL> COL "Data Type" FORMAT A28

SQL> 
    SELECT internal_column_id "Col ID", SUBSTR(column_name,1,30) "Column Name",
           SUBSTR(data_type,1,30) "Data Type", data_length "Data Length"
      FROM   user_tab_cols
     WHERE  table_name = 'LEDGER_EMP' ORDER BY internal_column_id
     /

    Col ID Column Name              Data Type                    Data Length
---------- ------------------------ ---------------------------- -----------
         1 EMPLOYEE_ID              NUMBER                                22
         2 SALARY                   NUMBER                                22
         3 ORABCTAB_INST_ID$        NUMBER                                22
         4 ORABCTAB_CHAIN_ID$       NUMBER                                22
         5 ORABCTAB_SEQ_NUM$        NUMBER                                22
         6 ORABCTAB_CREATION_TIME$  TIMESTAMP(6) WITH TIME ZONE           13
         7 ORABCTAB_USER_NUMBER$    NUMBER                                22
         8 ORABCTAB_HASH$           RAW                                 2000
         9 ORABCTAB_SIGNATURE$      RAW                                 2000
        10 ORABCTAB_SIGNATURE_ALG$  NUMBER                                22
        11 ORABCTAB_SIGNATURE_CERT$ RAW                                   16
        12 ORABCTAB_SPARE$          RAW                                 2000

12 rows selected.

```
* 데이터 입력

```sql
SQL> insert into ledger_emp values (106,12000);

1 row created.

SQL> commit;

Commit complete.
```

* Display the internal values of the first row of the chain.

```sql
SQL> COL "Chain date" FORMAT A1
SQL> COL "Chain ID" FORMAT 99999999
SQL> COL "Seq Num" FORMAT 99999999
SQL> COL "User Num" FORMAT 9999999
SQL> col "Chain HASH" format a60
SQL> SELECT ORABCTAB_CHAIN_ID$ "Chain ID", ORABCTAB_SEQ_NUM$ "Seq Num",
            to_char(ORABCTAB_CREATION_TIME$,'dd-Mon-YYYY hh-mi') "Chain date",
            ORABCTAB_USER_NUMBER$ "User Num", ORABCTAB_HASH$ "Chain HASH"
    FROM   ledger_emp
/
  2    3    4    5
 Chain ID   Seq Num Chain date        User Num Chain HASH
--------- --------- ----------------- -------- ------------------------------------------------------------
       12         1 20-Jan-2021 01-50      121 F5F3A3B7C225C6398F6E687769C2E868661F7D0A56066EAFA78AD7A8156E
                                               7DABBBF82F40035E0E5733D7D3E5D99E60F1DBA0683E45568AABEB357EAA
                                               227919E8


SQL>

```
* grant user 

```sql
SQL> GRANT insert ON ledger_emp TO hr;

Grant succeeded.

SQL>
```

* HR user
```sql
[oracle@db21c ~]$ sqlplus  hr/WElcome123##@PDB21

SQL*Plus: Release 21.0.0.0.0 - Production on Wed Jan 20 01:59:28 2021
Version 21.1.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.


Connected to:
Oracle Database 21c EE High Perf Release 21.0.0.0.0 - Production
Version 21.1.0.0.0

SQL> INSERT INTO  auditor.ledger_emp VALUES (106,24000);
COMMIT;
1 row created.

SQL>

Commit complete.

```
* auditor user

```sql
SQL> SELECT ORABCTAB_CHAIN_ID$ "Chain ID", ORABCTAB_SEQ_NUM$ "Seq Num",
  2                to_char(ORABCTAB_CREATION_TIME$,'dd-Mon-YYYY hh-mi') "Chain date",
              ORABCTAB_USER_NUMBER$ "User Num", ORABCTAB_HASH$ "Chain HASH",
              employee_id, salary
        FROM   ledger_emp
/
  3    4    5    6
 Chain ID   Seq Num Chain date        User Num Chain HASH                                                   EMPLOYEE_ID     SALARY
--------- --------- ----------------- -------- ------------------------------------------------------------ ----------- ----------
       12         1 20-Jan-2021 01-50      121 F5F3A3B7C225C6398F6E687769C2E868661F7D0A56066EAFA78AD7A8156E         106      12000
                                               7DABBBF82F40035E0E5733D7D3E5D99E60F1DBA0683E45568AABEB357EAA
                                               227919E8

       19         1 20-Jan-2021 01-59      120 715C03F5FE79D6FB8DC7CA7FA263DDAC6B01DD0A69B6A31E6E449D284D23         106      24000
                                               3AB9A0AB23EDC721521B735A19440F0C93341B05ABADDF9985D50AEFB313
                                               326C09A6

```

### Delete rows from the blockchain table
* Delete the row inserted by HR. 

```sql
SQL> DELETE FROM ledger_emp WHERE ORABCTAB_USER_NUMBER$ = 119;
DELETE FROM ledger_emp WHERE ORABCTAB_USER_NUMBER$ = 119
            *
ERROR at line 1:
ORA-05715: operation not allowed on the blockchain table


```

* DBMS_BLOCKCHAIN_TABLE.DELETE_EXPIRED_ROWS (delete rows that are outside the retention period)
```sql
SQL> SET SERVEROUTPUT ON
SQL> DECLARE
  NUMBER_ROWS NUMBER;
BEGIN
  DBMS_BLOCKCHAIN_TABLE.DELETE_EXPIRED_ROWS('AUDITOR','LEDGER_EMP', null, NUMBER_ROWS);
  DBMS_OUTPUT.PUT_LINE('Number of rows deleted=' || NUMBER_ROWS);
END;
/  2    3    4    5    6    7
Number of rows deleted=0

PL/SQL procedure successfully completed.

SQL>
SQL> TRUNCATE TABLE ledger_emp;
TRUNCATE TABLE ledger_emp
               *
ERROR at line 1:
ORA-05715: operation not allowed on the blockchain table


```

### Drop the blockchain table

* Drop Table

```sql
SQL> DROP TABLE ledger_emp;
DROP TABLE ledger_emp
           *
ERROR at line 1:
ORA-05723: drop blockchain table LEDGER_EMP not allowed

```

* Change the behavior of the table to allow a lower retention.

```sql
SQL> /
ALTER TABLE ledger_emp NO DROP UNTIL 1 DAYS IDLE
*
ERROR at line 1:
ORA-05732: retention value cannot be lowered


SQL> ALTER TABLE ledger_emp NO DROP UNTIL 40 DAYS IDLE;

Table altered.

```
### Check the validity of rows in the blockchain table

```sql
SQL> CREATE BLOCKCHAIN TABLE auditor.ledger_test (id NUMBER, label VARCHAR2(2))
      NO DROP UNTIL 1 DAYS IDLE
      NO DELETE UNTIL 5 DAYS AFTER INSERT
      HASHING USING "SHA2_512" VERSION "v1";  2    3    4
CREATE BLOCKCHAIN TABLE auditor.ledger_test (id NUMBER, label VARCHAR2(2))
*
ERROR at line 1:
ORA-05741: minimum retention time too low, should be at least 16 days


SQL> ed
Wrote file afiedt.buf

  1  CREATE BLOCKCHAIN TABLE auditor.ledger_test (id NUMBER, label VARCHAR2(2))
  2        NO DROP UNTIL 16 DAYS IDLE
  3        NO DELETE UNTIL 5 DAYS AFTER INSERT
  4*       HASHING USING "SHA2_512" VERSION "v1"
SQL> /
CREATE BLOCKCHAIN TABLE auditor.ledger_test (id NUMBER, label VARCHAR2(2))
*
ERROR at line 1:
ORA-05741: minimum retention time too low, should be at least 16 days


SQL> ed
Wrote file afiedt.buf

  1  CREATE BLOCKCHAIN TABLE auditor.ledger_test (id NUMBER, label VARCHAR2(2))
  2        NO DROP UNTIL 16 DAYS IDLE
  3        NO DELETE UNTIL 16 DAYS AFTER INSERT
  4*       HASHING USING "SHA2_512" VERSION "v1"
SQL> /

Table created.

SQL> GRANT insert ON auditor.ledger_test TO hr;

Grant succeeded.

SQL> CONNECT hr@PDB21
Enter password:  

Connected.

SQL> show user
USER is "HR"
SQL> INSERT INTO auditor.ledger_test VALUES (1,'A1');
1 row created.
SQL> commit;

Commit complete.

SQL> SET SERVEROUTPUT ON
SQL>
SQL> DECLARE
  2    row_count NUMBER;
  verify_rows NUMBER;
  instance_id NUMBER;
BEGIN
  FOR instance_id IN 1 .. 2 LOOP
    SELECT COUNT(*) INTO row_count FROM auditor.ledger_test WHERE ORABCTAB_INST_ID$=instance_id;
    DBMS_BLOCKCHAIN_TABLE.VERIFY_ROWS('AUDITOR','LEDGER_TEST', NULL, NULL,  3   instance_id, NULL, verify_rows);
    DBMS_OUTPUT.PUT_LINE('Number of rows verified in instance Id '|| instance_id || ' = '|| row_count);
  END LOOP;
END;
/ 10   11   12
Number of rows verified in instance Id 1 = 1
Number of rows verified in instance Id 2 = 0

PL/SQL procedure successfully completed.

SQL> show user
USER is "AUDITOR"


SQL> SQL> SELECT * FROM auditor.ledger_test;


        ID LA
---------- --
         1 A1



```
