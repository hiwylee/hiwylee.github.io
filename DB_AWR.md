## Oracle AWR report
### Perf Guide Portal - RAC Perfomance tuning with AWR/EM reports
* https://www.hhutzler.de/blog/rac-tuning-with-awr/#Tuning_Step_1_Avoid_sequences_by_using_a_JAVA_generated_sequence
### AWR report

```sql
@?/rdbms/admin/awrrpt.sql      -- basic AWR report
@?/rdbms/admin/awrsqrpt.sql    -- Standard SQL statement Report
@?/rdbms/admin/awrddrpt.sql    -- Period diff on current instance
@?/rdbms/admin/awrrpti.sql     -- Workload Repository Report Instance (RAC)
@?/rdbms/admin/awrgrpt.sql     -- AWR Global Report (RAC)
@?/rdbms/admin/awrgdrpt.sql    -- AWR Global Diff Report (RAC)
@?/rdbms/admin/awrinfo.sql     -- Script to output general AWR information
```

### Oracle Database Tips by Donald Burleson
See my notes on Reading Oracle AWR report and see the book Oracle Tuning: The Definitive Reference for a comprehensive treatment of AWR for Oracle tuning.  Also see these tips for Oracle AWR reports:

* [Oracle AWR SQL Tuning Scripts](http://www.dba-oracle.com/art_orafaq_awr_sql_tuning.htm)
* [Oracle AWR sysaux tablespace](http://www.fast-track.cc/t_awr_workload_sysaux_tablespaces.htm)
* [Interpreting RAC AWR reports](http://www.dba-oracle.com/t_rac_statspack_awr_report_tips.htm)
* [Oracle STATSPACK vs. AWR](http://www.fast-track.cc/t_statspack_awr.htm)
* [AWR script for physical disk reads](http://www.dba-oracle.com/art_orafaq_awr_disk_reads.htm)
* [Oracle transportable AWR snapshots](http://www.rampant-books.com/art_oracle_awr_transportable_snapshots.htm)
* [Oracle Creating an AWR Report](http://www.dba-oracle.com/oracle10g_tuning/t_oracle_creating_awr_report_awrrpt.htm)
* [Oracle AWR disk file statistics](http://www.praetoriate.com/t_awr_disk_file_statistics.htm)
