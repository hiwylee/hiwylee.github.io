# PACK 관련 정보 (enable & diable)

* http://wiki.gurubee.net/display/CORE/Home
```sql
CONTROL_MANAGEMENT_PACK_ACCESS is set to NONE:
```

* Diagnostic Pack Features
  * Automatic Workload Repository (AWR)
  * Automatic Database Diagnostic Monitor (ADDM)
  * Active Session History (ASH)
  * Performance Monitoring (database and host)
* Tuning Pack Features
  * SQL Access Advisor
  * SQL Tuning Advisor
  * Automatic SQL Tuning
  * SQL Tuning Sets
  * SQL Monitoring
  * Reorganize objects
* SQL Tuning Pack 사용여부 확인

```sql
prompt *******************************************************
prompt This script will show if the database is using AWR
prompt *******************************************************
 
select
   display_value
from
   v$parameter
where
   name = 'control_management_pack_access';
-- *******************************************************
-- This query goes into more detail on usage 
-- of the tuning pack
-- *******************************************************
col c1 heading 'Feature Name'     format a35
col c2 heading 'Detected|Usages'  format 999,999
col c3 heading 'Last|Usage|Date'  format a10
select 
   name              c1, 
   detected_usages   c2, 
   last_usage_date   c3
from 
   dba_feature_usage_statistics
where 
name in (
 'ADDM', 
 'Automatic SQL Tuning Advisor', 
 'Automatic Workload Repository', 
 'AWR Baseline', 
 'AWR Baseline Template', 
 'AWR Report', 
 'EM Performance Page', 
 'Real-Time SQL Monitoring', 
 'SQL Access Advisor', 
 'SQL Monitoring and Tuning pages', 
 'SQL Performance Analyzer', 
 'SQL Tuning Advisor', 
 'SQL Tuning Set (system)', 
 'SQL Tuning Set (user)'
)
order by name;
```
