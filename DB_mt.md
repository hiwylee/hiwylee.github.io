## Oracle Multitenant Fundamentals
* [LiveLabs - Oracle Multitenant Fundamentals](https://oracle.github.io/learning-library/data-management-library/database/multitenant/workshops/freetier/?lab=lab-3-clone,-plug-drop#Step5:DropaPDB)
### Basic Info

```sql
SQL>
select
  'DB Name: '  ||Sys_Context('Userenv', 'DB_Name')||
  ' / CDB?: '     ||case
    when Sys_Context('Userenv', 'CDB_Name') is not null then 'YES'
      else  'NO'
      end||
  ' / Auth-ID: '   ||Sys_Context('Userenv', 'Authenticated_Identity')||
  ' / Sessn-User: '||Sys_Context('Userenv', 'Session_User')||
  ' / Container: ' ||Nvl(Sys_Context('Userenv', 'Con_Name'), 'n/a')
  "Who am I?"
  from Dual
  /

Who am I?
--------------------------------------------------------------------------------
DB Name: CDB1 / CDB?: YES / Auth-ID: SYS / Sessn-User: SYS / Container: CDB$ROOT

SQL>
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
SQL>

```

* Create PDB

```sql
QL> create pluggable database pdb2 admin user PDB_Admin identified by oracle;

Pluggable database created.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 PDB2                           MOUNTED
SQL>

SQL> alter session set container=PDB2;

Session altered.

SQL>
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         4 PDB2                           MOUNTED
SQL> alter pluggable database open read write;

Pluggable database altered.
SQL>
SQL> grant sysdba to pdb_admin;

Grant succeeded.

SQL> create tablespace users datafile size 20M autoextend on next 1M maxsize unlimited segment space management auto;
SQL>
Tablespace created.
SQL>

SQL> alter database default tablespace Users;


Database altered.
SQL>
SQL> grant create table, unlimited tablespace to pdb_admin;

Grant succeeded.


SQL> connect pdb_admin/oracle@localhost:1523/pdb2
Connected.
SQL>


```  
* Step 2: Clone a PDB

```sq;
SQL> ed
Wrote file afiedt.buf

  1* alter pluggable database pdb2 open read only force
SQL> /
alter
Pluggable database altered.

create pluggable database pdb3 from pdb2;

Pluggable database created.

SQL>
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 PDB2                           READ ONLY  NO
         5 PDB3                           MOUNTED
SQL>
  1* alter pluggable database pdb2 open force
SQL> /

Pluggable database altered.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 PDB2                           READ WRITE NO
         5 PDB3                           READ WRITE NO
SQL>
SQL> connect pdb_admin/oracle@localhost:1523/pdb2
Connected.
SQL> select * from my_tab;

    MY_COL
----------
         1


SQL> connect pdb_admin/oracle@localhost:1523/pdb3
Connected.
SQL> select * from my_tab;

    MY_COL
----------
         1

SQL>


```
* Step3: Unplug a pdb2

```sq;
SQL> connect sys/oracle@localhost:1523/cdb1 as sysdba
Connected.
SQL>
SQL>
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 PDB2                           READ WRITE NO
         5 PDB3                           READ WRITE NO
SQL> alter pluggable database pdb2 close immediate;

Pluggable database altered.

SQL> alter pluggable database pdb2 unplug into '/tmp/pdb2.xml';

Pluggable database altered.

SQL> drop pluggable database pdb2 keep datafiles;

Pluggable database dropped.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         5 PDB3                           READ WRITE NO
SQL>

```  
* Plug PDB3 into CDB2.
```sql
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         5 PDB3                           READ WRITE NO
SQL> create pluggable database pdb2 using '/tmp/pdb2.xml' move;

Pluggable database created.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         5 PDB3                           READ WRITE NO
         6 PDB2                           MOUNTED
SQL>

```
* tep 5: Drop a PDB

```sql
SQL> connect sys/oracle@localhost:1523/cdb1 as sysdba
Connected.
SQL>
SQL>
SQL>
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         5 PDB3                           READ WRITE NO
         6 PDB2                           MOUNTED
SQL> alter pluggable database pdb3 close immediate;

Pluggable database altered.

SQL> drop pluggable database pdb3 including datafiles;

Pluggable database dropped.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         6 PDB2                           MOUNTED
SQL>

```
* Step 6: Clone an Unplugged PDB

```sql
  1* alter pluggable database pdb2 open read only force
SQL> /

Pluggable database altered.

SQL> create pluggable daabase GOLDPDB from pdb2;


SQL> ed
Wrote file afiedt.buf

  1* create pluggable database GOLDPDB from pdb2
SQL> /
Pluggable database created.
SQL> alter pluggable database GOLDPDB open force;


Pluggable database altered.

SQL> SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 GOLDPDB                        READ WRITE NO
         6 PDB2                           READ ONLY  NO
SQL>
SQL> alter pluggable database GOLDPDB close immediate;

Pluggable database altered.

SQL> alter pluggable database GOLDPDB unplug into '/tmp/goldpdb.xml';

Pluggable database altered.

SQL>
SQL> ed
Wrote file afiedt.buf

  1* drop pluggable database GOLDPDB keep datafiles
SQL> /

Pluggable database dropped.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         6 PDB2                           READ WRITE NO
SQL>
-- cdb1 -> cdb2
SQL> connect sys/oracle@localhost:1524/cdb2 as sysdba
Connected.
SQL>
SQL> ed
Wrote file afiedt.buf

  1  begin
  2    if not
  3      Sys.DBMS_PDB.Check_Plug_Compatibility
  4  ('/tmp/goldpdb.xml')
  5    then
  6      Raise_Application_Error(-20000, 'Incompatible');
  7    end if;
  8* end;
SQL> /

PL/SQL procedure successfully completed.

SQL> ed
Wrote file afiedt.buf

  1  create pluggable database GOLDPDB1 as clone using '/tmp/goldpdb.xml'
  2  storage  (maxsize unlimited max_shared_temp_size unlimited)
  3* copy
SQL> /

Pluggable database created.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB2                           READ WRITE NO
         5 GOLDPDB1                       MOUNTED
SQL>
SQL> ed
Wrote file afiedt.buf

  1  create pluggable database GOLDPDB2 as clone using '/tmp/goldpdb.xml'
  2  storage  (maxsize unlimited max_shared_temp_size unlimited)
  3* copy
SQL> /

Pluggable database created.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB2                           READ WRITE NO
         5 GOLDPDB1                       MOUNTED
         6 GOLDPDB2                       MOUNTED
SQL>
SQL> ed
Wrote file afiedt.buf

  1* alter pluggable database all open
SQL> /

Pluggable database altered.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB2                           READ WRITE NO
         5 GOLDPDB1                       READ WRITE NO
         6 GOLDPDB2                       READ WRITE NO

SQL> ed
Wrote file afiedt.buf

  1  select PDB_Name "PDB Name", GUID
  2  from DBA_PDBs
  3* order by Creation_Scn
SQL> /

PDB Name             GUID
-------------------- --------------------------------
PDB$SEED             AE554B7545A21536E0530200000A98E9
PDB2                 AE557591FED21EB1E0530200000A95FC
GOLDPDB1             AF08486161FF2C26E0530200000A3BFE
GOLDPDB2             AF08486162012C26E0530200000A3BFE

SQL>

```
* Step 7: PDB Hot Clones

```sql
SQL> connect sys/oracle@localhost:1523/cdb1 as sysdba
Connected.
SQL>
SQL>
SQL>
SQL>
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         6 PDB2                           READ WRITE NO
SQL> create pluggable database oe admin user soe identified by soe role=(dba);
Pluggable database created.

SQL>
SQL> create pluggable database oe admin user soe identified by soe role=(dba);

Pluggable database created.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 OE                             MOUNTED
         6 PDB2                           READ WRITE NO
SQL> alter pluggable database oe open read write ;

Pluggable database altered.

SQL> alter session set container=oe
  2  ;

Session altered.

SQL> grant create session, create table to soe;

Grant succeeded.

SQL> alter user soe quota unlimited on system;

User altered.

SQL>
-- connect soe/soe@localhost:1523/oe

```

```bash
[oracle@workshop multitenant]$ cat  write-load.sh
#!/bin/sh
#
ORACLE_SID=CDB1
ORAENV_ASK=NO
. oraenv

#
echo ""
echo "  NOTE:"
echo "  To break out of this batch"
echo "  job, please issue CTL-C "
echo ""
echo "...sleeping 5 seconds"
echo ""
sleep 5

  sqlplus -S /nolog << EOF
  @truncate_sale_orders.sql
EOF

c=1
while [ $c -le 1000 ]
do
  sqlplus -S /nolog  << EOF
  @batch-orders.sql
  commit;
  @count-sales.sql
  @scn.sql
  @dbname.sql
EOF
sleep 1
(( c++))
done

[oracle@workshop multitenant]$

[oracle@workshop multitenant]$ ./write-load.sh
The Oracle base remains unchanged with value /u01/app/oracle

  NOTE:
  To break out of this batch
  job, please issue CTL-C

...sleeping 5 seconds
...
* Hot Clone (OE_DEV)  from OE
...sql
SQL> ed
Wrote file afiedt.buf

  1* create pluggable database oe_dev from oe@cdb1_link
SQL> /

Pluggable database created.
 
SQL> alter pluggable database oe_dev open read write;

Pluggable database altered.

SQL> connect soe/soe@localhost:1524/oe_dev
Connected.
SQL> select count(*) from sale_orders;

  COUNT(*)
----------
       790

SQL>


```
* Step 8: PDB Refresh

```sql
[oracle@workshop ~]$ sqlplus /nolog

SQL*Plus: Release 19.0.0.0.0 - Production on Sat Sep 12 05:26:48 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

SQL> connect sys/oracle@localhost:1524/cdb2 as sysdba
Connected.
SQL>
SQL>
SQL>
SQL> desc dba_db_links
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 OWNER                                     NOT NULL VARCHAR2(128)
 DB_LINK                                   NOT NULL VARCHAR2(128)
 USERNAME                                           VARCHAR2(128)
 HOST                                               VARCHAR2(2000)
 CREATED                                   NOT NULL DATE
 HIDDEN                                             VARCHAR2(3)
 SHARD_INTERNAL                                     VARCHAR2(3)
 VALID                                              VARCHAR2(3)
 INTRA_CDB                                          VARCHAR2(3)

SQL> select db_link from dba_db_links
  2  ;

DB_LINK
--------------------------------------------------------------------------------
CDB1_LINK
SYS_HUB

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB2                           READ WRITE NO
         5 GOLDPDB1                       READ WRITE NO
         6 GOLDPDB2                       READ WRITE NO
SQL> create pluggable database oe_refresh from oe@cdb1_link refresh mode manual;
SQL> alter pluggable database oe_refresh open read only;

Pluggable database altered.

SQL> conn soe/soe@localhost:1524/oe_refresh
Connected.
SQL> select count(*) from sale_orders;

  COUNT(*)
----------
      4480


SQL> conn sys/oracle@localhost:1524/oe_refresh as sysdba
Connected.
SQL> alter pluggable database oe_refresh close;

Pluggable database altered.

SQL> alter session set container=oe_refresh;

Session altered.

SQL> alter pluggable database oe_refresh refresh;

Pluggable database altered.

SQL> alter pluggable database oe_refresh open read only;

Pluggable database altered.

SQL> conn soe/soe@localhost:1524/oe_refresh
Connected.
SQL> select count(*) from sale_orders;

  COUNT(*)
----------
       220


```

* Step 9: PDB Relocation

```sql		
[oracle@workshop ~]$ sqlplus /nolog

SQL*Plus: Release 19.0.0.0.0 - Production on Sat Sep 12 05:41:22 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

SQL> connect sys/oracle@localhost:1523/cdb1 as sysdba
Connected.
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 OE                             READ WRITE NO
         6 PDB2                           READ WRITE NO
SQL>

SQL> conn sys/oracle@localhost:1524/cdb2 as sysdba;
Connected.
SQL>
SQL> alter system set local_listener='LISTCDB1' scope=BOTH;

System altered.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB2                           READ WRITE NO
         5 GOLDPDB1                       READ WRITE NO
         6 GOLDPDB2                       READ WRITE NO
SQL>
SQL> connect sys/oracle@localhost:1523/cdb2 as sysdba
Connected.
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB2                           READ WRITE NO
         5 GOLDPDB1                       READ WRITE NO
         6 GOLDPDB2                       READ WRITE NO
SQL> 

SQL> ed
Wrote file afiedt.buf

  1* create pluggable database oe_r from oe@cdb1_link relocate
SQL> /
create pluggable database oe_r from oe@cdb1_link relocate
*
ERROR at line 1:
ORA-65122: Pluggable database GUID conflicts with the GUID of an existing
container.


SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB2                           READ WRITE NO
         4 OE                             MOUNTED
         5 GOLDPDB1                       READ WRITE NO
         6 GOLDPDB2                       READ WRITE NO
SQL> alter pluggable database oe open read write;

Pluggable database altered.


SQL> alter pluggable database oe close force;

Pluggable database altered.

SQL> drop pluggable database oe including datafiles;

Pluggable database dropped.

SQL>  conn sys/oracle@localhost:1523/cdb1 as sysdba
Connected.
SQL>
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         6 PDB2                           READ WRITE NO
SQL>
SQL> ed
Wrote file afiedt.buf

  1* alter system set local_listener='LISTCDB2' scope=both
SQL> /

System altered.

SQL>

```