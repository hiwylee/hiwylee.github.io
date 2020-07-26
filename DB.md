## DB Upgrade 
* https://mikedietrichde.com/
### Upgrade : Sigle Source of Truth
* MOS Note: 742060.1 : Release Schedule of Current Database Releases
  * https://support.oracle.com/epmos/faces/DocumentDisplay?id=742060.1
* • MOS Note: 2285040.1 : Release Update Introduction and FAQ
  * https://support.oracle.com/epmos/faces/DocumentDisplay%3Fid=2285040.1
• MOS Note: 756671.1 : Master Note for Database Proactive Patch Program
  * https://support.oracle.com/epmos/faces/DocumentDisplay?id=756671.1
* MOS Note: 1962125.1 : Oracle Database - Overview of Database Patch Delivery Methods for 12.1.0.2 and lower
  * https://support.oracle.com/epmos/faces/DocumentDisplay?id=1962125.1
* MOS NOTE 2337415.1 : Oracle Database - Overview of Database Patch Delivery Methods for 12.2.0.1 and greater
  * https://support.oracle.com/epmos/faces/DocumentDisplay?id=2337415.1
*MOS Note: 2118136.2:  Assistant: Download Reference for Oracle Database/GI PSU, SPU(CPU), Bundle Patches, Patchsets and Base Releases
  * https://support.oracle.com/epmos/faces/DocumentDisplay?id=2118136.2
### Upgrade / Migrate / Consolidateto Oracle Database 19c - Mega Slide
* [Upgrade / Migrate / Consolidateto Oracle Database 19c](http://apex.oracle.com/pls/apex/f?p=202202:2:::::P2_SUCHWORT:upgrade19c)
## Oracle Database 20c
* Webcast - Oracle Database 20c New Features
  * https://otube.oracle.com/media/1_92bjlut1
* What’s New in Oracle Database 19c  
  * https://otube.oracle.com/media/0_lw4j7yvl
  * https://otube.oracle.com/media/Oracle+Database+19c+-+New+Features/0_75l8pb7c
  
##  Oracle Machine Learning for Python (OML4Py) AutoML

## Tuning
* [Real-World Performance](https://apexapps.oracle.com/pls/apex/f?p=44785:141:0::NO::P141_PAGE_ID,P141_SECTION_ID:119,870) 
* [Oracle Database Performance Tuning for Admins and Architects](https://www.youtube.com/watch?v=RsbHAaGCtM4)
* Wait Event
  [Oracle Wait Events](https://www.youtube.com/watch?v=6wSFqdSJPEI)
  * [Lunch n Learn Important Oracle Wait Events](https://www.youtube.com/watch?v=iqUEl5l0qlw)
  * [HOW ORACLE WAIT EVENT WORKS | By Dinesh Sharma](https://www.youtube.com/watch?v=RsbHAaGCtM4)
* AWR Report
  * [Troubleshooting a Complex Oracle Performance Issue](https://www.youtube.com/watch?v=hxy8sfrezYo)
  * [Analysis of a Couple AWR Reports](https://www.youtube.com/watch?v=xSXQ3EwU8t0)
  * [How to Read Oracle AWR Report | Oracle Automatic Workload Repository](https://www.youtube.com/watch?v=QPJL1fswbO4)
* [DBBT] Query Optimizer Overview
  * [Part 1](https://otube.oracle.com/media/%5BDBBT%5D+Query+Optimizer+Overview+part+1/0_6raiy7ku/112440841)
  * [Part 2](https://otube.oracle.com/media/%5BDBBT%5D+Query+Optimizer+Overview+part+2/0_kthct0nc/112440841)
## Oracle Database Backup and Recovery 
* [Oracle Database Backup and Recovery Session](https://www.youtube.com/playlist?list=PLJivLVlqh_a4OtPb-S80z_X6MevQNWmcG)
## RAC
* [Oracle RAC Videos](https://www.youtube.com/playlist?list=PLJivLVlqh_a6Xm2sT-plkW4Ii7EWvvAc4)
## Open Source
* MySQL
* PostgreSQL 
 * [PosrgreSQL](https://www.youtube.com/watch?v=TGuDmzzhq1Y)
* [NHN FORWARD 2019](https://www.youtube.com/watch?v=8Eb_n7JA1yA&list=PL42XJKPNDepZVLkCM4yEKmU4LHyXjzChy)
* [```NHN FORWARD 2019 : Oracle => MySQL 이관```](https://www.youtube.com/watch?v=DXu3nbWa4AA)

## EM Express
* [``Using EM Express``](https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Tasks/monitoringDB.htm)
```
$ . oraenv
ORACLE_SID = [oracle] ? orcl
The Oracle base has been set to /scratch/u01/app/oracle
$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Wed Mar 25 00:54:43 2019
Version 19.3.0.0.0

Copyright (c) 1982, 2019, Oracle.  All rights reserved.

Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.3.0.0.0

SQL>  

$ SQL> alter session set container=orclpdb;

Session altered.
SQL> exec DBMS_XDB_CONFIG.SETHTTPSPORT(5501)

PL/SQL procedure successfully completed.

SQL>  SELECT dbms_xdb_config.gethttpsport() from dual; 

DBMS_XDB_CONFIG.GETHTTPSPORT()
------------------------------
5501


```
* open port 5500,6200,1158

