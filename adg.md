## Active Data Guard using Data Guard Broker

* https://oracle-base.com/articles/19c/data-guard-setup-using-broker-19c
```sh
"/tmp/initcdb1_stby.ora"

*.db_name='cdb1'
mkdir -p /u01/app/oracle/oradata/ORCL/pdbseed
mkdir -p /u01/app/oracle/oradata/ORCL/pdb1
mkdir -p /u01/app/oracle/fast_recovery_area/ORCL
mkdir -p /u01/app/oracle/admin/ORCL/adumpquit

orapwd file=/u01/app/oracle/product/19c/dbhome_1/dbs/orapwORCL password=Password1 entries=10

export ORACLE_SID=ORCL
[oracle@workshop2 admin]$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Tue Sep 1 13:55:32 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

Connected to an idle instance.

SQL> startup nomount pfile='/tmp/initORCL.ora';
ORACLE instance started.

Total System Global Area  381677696 bytes
Fixed Size                  8896640 bytes
Variable Size             314572800 bytes
Database Buffers           50331648 bytes
Redo Buffers                7876608 bytes
SQL>

```
* Duplicate Database 
```sql
rman TARGET sys/Password1@ORCL AUXILIARY sys/Password1@ORCL_stby
RMAN>
DUPLICATE TARGET DATABASE
  FOR STANDBY
  FROM ACTIVE DATABASE
  DORECOVER
  SPFILE
    SET db_unique_name='ORCL_STBY' COMMENT 'Is standby'
  NOFILENAMECHECK;
```


