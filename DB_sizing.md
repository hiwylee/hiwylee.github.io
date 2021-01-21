## Analysis of AWR stats & Sizing   - Working on...
### AWR Miner
* https://github.com/tmuth/AWR-Miner
* [How to generate AWR miner report — oracle-tech](https://www.doag.org/formes/pubfiles/8474039/2016-DB-Maris_Elsins-Mining_the_AWR_v2__Trend_Analysis-Manuskript.pdf)
### CPU
* AAS = DB Time / CLock Time
* Load Profile - DB Time/ per Sec < OCPU 보다 적을 것


### I/O ( per sec )
* IOPS / sec  -  ASM redundancy (high/normal)
1) Read IOPS : physical read total IO requests	: 11,074.00 
2) Write IOPS : physical write total IO requests	: 442.45 
3) total = Read IOPS +  ( 3 * Write IOPS or  2 * Write IOPS)

* Bandwidth -  ASM redundancy (high/normal)
1) Read Bandwidth : physical read total bytes	 : 662,871,118.16  
2) Write Bandwidth :physical write total bytes	 : 263,697,731.26 
3) total = Read IOPS +  ( 3 (high) * Write Write or  2(normal) * Write Write)

* Latency 
1) ..
