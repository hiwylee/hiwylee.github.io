# 
* [``**Using EM Express**``](https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Tasks/monitoringDB.htm)
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

