## Database trace 

se trace 

2



3

### 실행 SQO을 트레이스

```sql
select sid from v$mystat where rownum=1;
col sid format 9999
col username format a10
col program format a40
col service_name format a20
set linesize 100
select sid, username, program, service_name from v$session where username='SH';
  SID USERNAME   PROGRAM                                  SERVICE_NAME
----- ---------- ---------------------------------------- --------------------
  190 SH         sqlplus@rac1 (TNS V1-V3)                 fan

```

```sql

```

