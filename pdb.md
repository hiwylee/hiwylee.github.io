## multitenant overview
* https://oracle-base.com/articles/12c/multitenant-overview-container-database-cdb-12cr1#multitenant-articles
### PDB TEST

* CREATE PDB
```SQL
SQL> ed
Wrote file afiedt.buf

  1* CREATE PLUGGABLE DATABASE pdb5 ADMIN USER pdb_adm IDENTIFIED BY Password1
SQL> /

Pluggable database created.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 PDB2                           MOUNTED
         5 PDB5                           MOUNTED
* key update

```
$ sudo su –
# dbcli list-databases
# dbcli update-tdekey -i <database_ID> -n <PDB_name> -p <OCI CONSOLE에서 넣은 sys 패스워드>
-- DBCS OCI: How to create a new PDB in an OCI CDB? (Doc ID 2438598.1)
-- support.oracle.com
```

* UNPLUG  PDB
```SQL
SQL> SQL> ed
Wrote file afiedt.buf

  1* ALTER PLUGGABLE DATABASE pdb5 UNPLUG INTO '/u01/backup/pdb5.pdb'
SQL> /

Pluggable database altered.

Wrote file afiedt.buf

  1* ALTER PLUGGABLE DATABASE pdb5 UNPLUG INTO '/u01/backup/pdb5.pdb'
SQL> /

Pluggable database altered.

SQL> host ls -l /u01/backup/pdb5.pdb
-rw-r--r-- 1 oracle asmadmin 120828938 Sep  1 10:55 /u01/backup/pdb5.pdb

SQL> DROP PLUGGABLE DATABASE pdb5 INCLUDING DATAFILES;

Pluggable database dropped.

SQL> SELECT name, open_mode
FROM   v$pdbs
ORDER BY name;  2    3

NAME                                     OPEN_MODE
---------------------------------------- ----------
PDB$SEED                                 READ ONLY
PDB1                                     READ WRITE
PDB2                                     MOUNTED

```
* Plugin PDB from ".pdb" Archive File

```sql
SQL> ed
Wrote file afiedt.buf

  1  DECLARE
  2    l_result BOOLEAN;
  3  BEGIN
  4    l_result := DBMS_PDB.check_plug_compatibility(
  5                  pdb_descr_file => '/u01/backup/pdb5.pdb',
  6                  pdb_name       => 'pdb5');
  7    IF l_result THEN
  8      DBMS_OUTPUT.PUT_LINE('compatible');
  9    ELSE
 10      DBMS_OUTPUT.PUT_LINE('incompatible');
 11    END IF;
 12* END;
 13  /
compatible

PL/SQL procedure successfully completed.
SQL>
SQL> ed
Wrote file afiedt.buf

  1* CREATE PLUGGABLE DATABASE pdb5 USING '/u01/backup/pdb5.pdb'
SQL> /

Pluggable database created.

SQL> alter pluggable database pdb5 open read write;
Pluggable database altered.

```
* Unplug PDB to ".xml" File
```sql
SQL> alter pluggable database pdb5 close;

Pluggable database altered.

SQL> alter pluggable database pdb5 unplug into '/u01/backup/pdb5.xml';

Pluggable database altered.
SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 PDB2                           MOUNTED
         6 PDB5                           MOUNTED
SQL> DROP PLUGGABLE DATABASE pdb5 KEEP DATAFILES;

Pluggable database dropped.
SQL> ed
Wrote file afiedt.buf

  1  DECLARE
  2    l_result BOOLEAN;
  3  BEGIN
  4    l_result := DBMS_PDB.check_plug_compatibility(
  5                  pdb_descr_file => '/u01/backup/pdb5.xml',
  6                  pdb_name       => 'pdb5');
  7    IF l_result THEN
  8      DBMS_OUTPUT.PUT_LINE('compatible');
  9    ELSE
 10      DBMS_OUTPUT.PUT_LINE('incompatible');
 11    END IF;
 12* END;
 13  /
compatible

PL/SQL procedure successfully completed.

PL/SQL procedure successfully completed.

SQL> create pluggable database pdb5 using '/u01/backup/pdb5.xml' nocopy tempfile reuse;

Pluggable database created.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 PDB2                           MOUNTED
         5 PDB5                           MOUNTED
SQL>

```

* Create PDB from pdb
```sql
SQL> ed
Wrote file afiedt.buf

  1* alter pluggable database pdb5 open read write
SQL> /
creat
Pluggable database altered.


SQL>
SQL>
SQL> create pluggable database pdb6 from pdb5;

Pluggable database created.

SQL> show pdbs

    CON_ID CON_NAME                       OPEN MODE  RESTRICTED
---------- ------------------------------ ---------- ----------
         2 PDB$SEED                       READ ONLY  NO
         3 PDB1                           READ WRITE NO
         4 PDB2                           MOUNTED
         5 PDB5                           READ WRITE NO
         6 PDB6                           MOUNTED

```
