## Exadata Compression: HCC
### 

### Test

* Samples Data

```sql
CREATE SEQUENCE MYSEQUENCE START WITH 1 INCREMENT BY 1 CACHE 100;

CREATE TABLE MY_DBAOBJECTS AS
SELECT MYSEQUENCE.NEXTVAL UNIQUE_OBJID, A.OBJECT_ID, A.DATA_OBJECT_ID,
       A.OWNER, A.OBJECT_NAME, A.SUBOBJECT_NAME, OBJECT_TYPE
FROM DBA_OBJECTS A;

DESC MY_DBAOBJECTS ;

-- DATA POPULATION, EXECUTE THIS MULTIPLE TIMES:
DECLARE
  I PLS_INTEGER := 0;
BEGIN
  FOR I IN 1 .. 50
LOOP
INSERT INTO MY_DBAOBJECTS
SELECT MYSEQUENCE.NEXTVAL UNIQUE_OBJID, A.OBJECT_ID, A.DATA_OBJECT_ID,
       A.OWNER, A.OBJECT_NAME, A.SUBOBJECT_NAME, OBJECT_TYPE
FROM DBA_OBJECTS A;
COMMIT;
END LOOP;
END;
/
```

* OLTP compression:

```sql
CREATE TABLE MY_DBAOBJECTS_OLTP_COMP (
   UNIQUE_OBJID CONSTRAINT MY_DBAOBJECTS_OLTP_COMP_PK PRIMARY KEY,
   OBJECT_ID, DATA_OBJECT_ID,OWNER, OBJECT_NAME, SUBOBJECT_NAME, OBJECT_TYPE)
COMPRESS FOR OLTP AS
SELECT * FROM MY_DBAOBJECTS;
```

* QUERY LOW compression

```sql
CREATE TABLE MY_DBAOBJECTS_QUERY_LOW (
   UNIQUE_OBJID CONSTRAINT MY_DBAOBJECTS_QUERY_LOW_PK PRIMARY KEY,
   OBJECT_ID, DATA_OBJECT_ID,OWNER, OBJECT_NAME, SUBOBJECT_NAME, OBJECT_TYPE)
COMPRESS FOR QUERY LOW AS
SELECT * FROM MY_DBAOBJECTS ;
```

* QUERY HIGH compression 
 
```sql
CREATE TABLE MY_DBAOBJECTS_QUERY_HIGH (
   UNIQUE_OBJID CONSTRAINT MY_DBAOBJECTS_QUERY_HIGH_PK PRIMARY KEY,
   OBJECT_ID, DATA_OBJECT_ID,OWNER, OBJECT_NAME, SUBOBJECT_NAME, OBJECT_TYPE)
COMPRESS FOR QUERY HIGH AS
SELECT * FROM MY_DBAOBJECTS ;
```


*ARCHIVE LOW compression
 
```sql
CREATE TABLE MY_DBAOBJECTS_ARCHIVE_LOW (
   UNIQUE_OBJID CONSTRAINT MY_DBAOBJECTS_ARCHIVE_LOW_PK PRIMARY KEY,
   OBJECT_ID, DATA_OBJECT_ID,OWNER, OBJECT_NAME, SUBOBJECT_NAME, OBJECT_TYPE)
COMPRESS FOR ARCHIVE LOW AS
SELECT * FROM MY_DBAOBJECTS ;
```

* ARCHIVE HIGH compression

```sql
CREATE TABLE MY_DBAOBJECTS_ARCHIVE_HIGH (
   UNIQUE_OBJID CONSTRAINT MY_DBAOBJECTS_ARCHIVE_HIGH_PK PRIMARY KEY,
   OBJECT_ID, DATA_OBJECT_ID,OWNER, OBJECT_NAME, SUBOBJECT_NAME, OBJECT_TYPE)
COMPRESS FOR ARCHIVE HIGH AS
SELECT * FROM MY_DBAOBJECTS ;
```
### 압축율 비교

* SQL 

```sql
select segment_name,sum(bytes)/1024/1024/1024 GB from user_segments where segment_type='TABLE' and segment_name=upper('&TABLE_NAME') group by segment_name;
```
```sql

SELECT 	A.type,  round(A.GB,2) GB,  round(A.GB/B.GB,2) RATE FROM (
	select 'NONE' as type , segment_name,sum(bytes)/1024/1024/1024 GB from user_segments where segment_type='TABLE' and segment_name=upper('MY_DBAOBJECTS') group by segment_name
	union all
	select 'OLTP' as type , segment_name,sum(bytes)/1024/1024/1024 GB from user_segments where segment_type='TABLE' and segment_name=upper('MY_DBAOBJECTS_OLTP_COMP') group by segment_name
	union all
	select 'QUERY LOW' as type , segment_name,sum(bytes)/1024/1024/1024 GB from user_segments where segment_type='TABLE' and segment_name=upper('MY_DBAOBJECTS_QUERY_LOW') group by segment_name
	union all
	select 'QUERY HIGH' as type , segment_name,sum(bytes)/1024/1024/1024 GB from user_segments where segment_type='TABLE' and segment_name=upper('MY_DBAOBJECTS_QUERY_HIGH') group by segment_name
	union all
	select 'ARCHIVE LOW' as type , segment_name,sum(bytes)/1024/1024/1024 GB from user_segments where segment_type='TABLE' and segment_name=upper('MY_DBAOBJECTS_ARCHIVE_LOW') group by segment_name
	union all
	select 'ARCHIVE HIGH' as type , segment_name,sum(bytes)/1024/1024/1024 GB from user_segments where segment_type='TABLE' and segment_name=upper('MY_DBAOBJECTS_ARCHIVE_HIGH') group by segment_name
) A, 
   (select 'NONE' as type , segment_name,sum(bytes)/1024/1024/1024 GB from user_segments where segment_type='TABLE' and segment_name=upper('MY_DBAOBJECTS') group by segment_name) B
;
```
  * ![ratio](https://learning.oreilly.com/library/view/oracle-exadata-experts/9780133824957/ch05.html)

* Compression Types and Compression Units

```sql
SELECT COUNT(*) FROM (
SELECT DISTINCT DBMS_ROWID.ROWID_RELATIVE_FNO(ROWID),
DBMS_ROWID.ROWID_BLOCK_NUMBER(ROWID) FROM MY_DBAOBJECTS_OLTP_COMP);
```

  * ![combines the results of the query to identify rows per CU, alongside physical space usage.](https://learning.oreilly.com/library/view/oracle-exadata-experts/9780133824957/graphics/05tab02.jpg)

#### HCC AND PERFORMANCE
* read versus write I/O ,  large versus small I/O
