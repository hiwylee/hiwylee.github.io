### DB CLOB Performace Tuning
---
* Basic Idea 
  * https://web.stanford.edu/dept/itss/docs/oracle/10gR2/appdev.102/b14302/ch_dba.htm](https://web.stanford.edu/dept/itss/docs/oracle/10gR2/appdev.102/b14302/ch_dba.htm)
  
```sql
create table image_items(
  image_id               number,-- constraint pl_rm primary key,
  image_title            varchar2(128),
  image_artist           varchar2(128),
  image_publisher        varchar2(128),
  image_description varchar2(1000),
  image_price            number(6,2),
  image_file_path varchar2(128),
  image_thumb_path varchar2(128),
  image_thumb            ordsys.ordimage,
  image_clip             ordsys.ordimage
)
--
-- physical properties of table
--
  -- physical attributes clause
  pctfree 35 storage (initial 30M next 400M pctincrease 0)
  
  -- LOB storage clause (applies to LOB column)  
  LOB (image_clip.source.localdata) 
      store as (disable storage in row nocache nologging chunk 32768)
```

```
SVRMGR> CREATE TABLESPACE MONTANA DATAFILE 'montana.tbs' SIZE 400M;
Statement processed.
SVRMGR> CREATE TABLE images (imageID INTEGER ,image ORDSYS.ORDImage)
     LOB (image.source.localData) STORE AS 
            (
            TABLESPACE MONTANA
            STORAGE (
                   INITIAL 100M
                   NEXT 100M
                   )
            CHUNK 24K
            NOCACHE NOLOGGING
            );
---
LOB Index and LOB_index_clause
PCTVERSION Option
CACHE or NOCACHE Option
LOGGING or NOLOGGING Option
CHUNK Option
INITIAL and NEXT Parameters
ENABLE | DISABLE STORAGE IN ROW Clause
```
```
