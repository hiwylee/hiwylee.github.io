## 통게 정보 수집
### 기본 가이드 
* 스키마 레벨 통계 수집

```sql
exec dbms_stats.gather_schema_stats(ownname=>'SYS',degree=>4));
exec dbms_stats.gather_schema_stats(ownname=>'SYSTEM',degree=>4));
```
* Data Dictionary / fixed object  통계정보 생성

```sql
exec dbms_stats.gather_dictionary_stats(degree=>4);
exec dbms_stats.gather_fixed_objects_stats;
```

### stale 통계정보 재 수집 가이드 

#### STEP 1. 대상 확인
* 기준 : **변경이 10% 이상인 경우**  : ``ROUND ( (DELETES + UPDATES + INSERTS) / NUM_ROWS * 100) >= 10``
```sql
col OWNER format a20
col TABLE_NAME format a30
COL PERCENTAGE format 999,999

SELECT TABLES.OWNER, TABLES.TABLE_NAME,NUM_ROWS, 
ROUND((DELETES + UPDATES + INSERTS)/NUM_ROWS*100) PERCENTAGE
FROM DBA_TABLES TABLES, DBA_TAB_MODIFICATIONS MODIFICATIONS
WHERE TABLES.OWNER = MODIFICATIONS.TABLE_OWNER
AND TABLES.TABLE_NAME = MODIFICATIONS.TABLE_NAME AND NUM_ROWS > 0
AND ROUND ( (DELETES + UPDATES + INSERTS) / NUM_ROWS * 100) >= 10
ORDER BY 1,3,4 desc
/
```

#### STEP 2. 대상 SQL 자동 생성

```sql
set markup csv on quote off
set pagesize 0
set linesize 512
set head offset markup csv on quote off
set pagesize 0
set linesize 512

SELECT 'execute DBMS_STATS.GATHER_TABLE_STATS (OWNNAME => '''
     || TABLES.OWNER ||''', TABNAME =>'''|| TABLES.TABLE_NAME 
	 ||''', estimate_percent => dbms_stats.auto_sample_size, degree => DBMS_STATS.DEFAULT_DEGREE, GRANULARITY => ''ALL'', CASCADE => DBMS_STATS.AUTO_CASCADE);' AS SQL
FROM DBA_TABLES TABLES, DBA_TAB_MODIFICATIONS MODIFICATIONS
WHERE TABLES.OWNER = MODIFICATIONS.TABLE_OWNER
AND TABLES.TABLE_NAME = MODIFICATIONS.TABLE_NAME AND NUM_ROWS > 0
AND ROUND ( (DELETES + UPDATES + INSERTS) / NUM_ROWS * 100) >= 10  -- 데이터 변동량이 10% 이상인 것
ORDER BY 1 desc
/

set markup csv off
set head on 

```

### step 3 : 실행

```sql
execute DBMS_STATS.GATHER_TABLE_STATS (OWNNAME => 'SYS', TABNAME =>'WRM$_WR_CONTROL', estimate_percent => dbms_stats.auto_sample_size, degree => DBMS_STATS.DEFAULT_DEGREE, GRANULARITY => 'ALL', CASCADE => DBMS_STATS.AUTO_CASCADE);
execute DBMS_STATS.GATHER_TABLE_STATS (OWNNAME => 'SYS', TABNAME =>'USER$', estimate_percent => dbms_stats.auto_sample_size, degree => DBMS_STATS.DEFAULT_DEGREE, GRANULARITY => 'ALL', CASCADE => DBMS_STATS.AUTO_CASCADE);
```
