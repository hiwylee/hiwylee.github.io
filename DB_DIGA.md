## The Automatic Diagnostic Repository (ADR)
### Configuring the Fault Diagnosability Infrastructure
```sql
SQL> show parameter DIAGNOSTIC_DEST

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
diagnostic_dest                      string      /u01/app/oracle

```
* DIAGNOSTIC_DEST : $ORACLE_BASE or $ORACLE_HOME/diag
* ![ADR base structure](https://learning.oreilly.com/library/view/oracle-database-12c/9780071847445/f0135-01.jpg)
### ADR
* The database alert log
* The DDL log
*  The debug log
* Trace files
### Related Data Dictionary Views
* DBA_OUTSTANDING_ALERTS
* V$DIAG_INFO
* V$DIAG_CRITICAL_ERROR
* V$DATABASE_BLOCK_CORRUPTION
* V$CORRUPT_XID_LIST 
* V$HM_RUN
* Various V$HM_* views
