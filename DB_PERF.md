## SQL Tuning 
### Scripts
* https://techgoeasy.com/useful-scripts-oracle-database/
* https://oracle-base.com/dba/scripts
### Consideration
* Business Logic
* Data Desgin
* Application Design
* Change db Structure(Indexes)
* Tuning SQL
* Access Path - change to indexc
* Memory Allocation - Instance Tuning
### Hint
* pq_distribute
* opt_param
* leading
* swap_join_inputs
* pq_replicate
* no_gather_optimizer_statistics
```
INSERT /*+ pq_distribute(t none) opt_param('optimizer_adaptive_plans','false') */
...
SELECT * FROM (
	SELECT /*+ leading(f p j c) swap_join_inputs(c) swap_join_inputs(j)  swap_join_inputs(p)  pq_replicate(c) pq_replicate(j) pq_replicate(p) no_gather_optimizer_statistics pq_distribute(p none broadcast) */
..  
```
