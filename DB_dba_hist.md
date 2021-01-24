## dba_hist_sql_plan tips
* http://www.dba-oracle.com/oracle10g_tuning/t_dba_hist_sql_plan.htm
* http://www.rampant-books.com/book_0214_oracle_tuning_definitive_reference_3rd_ed.htm

### The dba_hist_sql_plan Table
```
The dba_hist_sql_plan table contains time-series data about each object, table, index, or view, involved in the query.  The important columns include the cost, cardinality, cpu_cost , io_cost  and temp_space required for the object.

 
The sample query below retrieves SQL statements which have high query execution cost identified by Oracle optimizer.
```
