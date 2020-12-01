### Oracle Exadata Smart Flash Cache in Depth
* https://www.informit.com/articles/article.aspx?p=2418151&seqNum=3
### Monitoring Exadata Smart Flash Cache
* Optimized Cell I/O Statistics

```sql
 
SELECT name, VALUE
  FROM v$mystat JOIN v$statname
      USING (statistic#)
 WHERE name IN ('cell flash cache read hits',
               'physical read requests optimized',
               'physical read total IO requests')


NAME                                             VALUE
---------------------------------------- -------------
physical read total IO requests                117,246
physical read requests optimized                58,916
cell flash cache read hits                      58,916
```

* Top Five Optimized I/O SQL Statements

```sql

SELECT sql_id,
       sql_text,
       optimized_phy_read_requests,
       physical_read_requests,
       optimized_hit_pct,
       pct_total_optimized
  FROM (  SELECT sql_id,
                 substr(sql_text,1,40) sql_text,
                 physical_read_requests,
                 optimized_phy_read_requests,
                 optimized_phy_read_requests * 100
                              / physical_read_requests
                    AS optimized_hit_pct,
                   optimized_phy_read_requests
                 * 100
                 / SUM (optimized_phy_read_requests)
                               OVER ()
                    pct_total_optimized,
                 RANK () OVER (ORDER BY
                                 optimized_phy_read_requests DESC)
                    AS optimized_rank
            FROM v$sql
           WHERE optimized_phy_read_requests > 0
        ORDER BY optimized_phy_read_requests DESC)
 WHERE optimized_rank <= 5
 

                  Optimized       Total Optimized Pct Total
SQL_ID              Read IO     Read IO   Hit Pct Optimized
--------------- ----------- ----------- --------- ---------
77kphjxam5akb       270,098     296,398     91.13     12.19
4mnz7k87ymgur       269,773     296,398     91.02     12.18
8mw2xhnu943jn       176,596     176,596    100.00      7.97
4xt8y8qs3gcca       117,228     117,228    100.00      5.29
bnypjf1kb37p1       117,228     117,228    100.00      5.29
```
