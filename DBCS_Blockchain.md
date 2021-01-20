## BLOCKCHAIN TABLE
### Simple Usage
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
    no drop until 1 days idle
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

    Col ID Column Name              Data Type                    Data Length
---------- ------------------------ ---------------------------- -----------
        12 ORABCTAB_SPARE$          RAW                                 2000

12 rows selected.

```
