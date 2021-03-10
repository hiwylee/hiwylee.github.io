## Flashback enable 

```sql
SQL> startup mount
ORACLE instance started.

Total System Global Area 4966054560 bytes
Fixed Size                  9144992 bytes
Variable Size             889192448 bytes
Database Buffers         4060086272 bytes
Redo Buffers                7630848 bytes
Database mounted.
SQL> alter database archivelog;

Database altered.
SQL>
SQL> alter database open;
Database altered.
SQL>
SQL> archive log list;
Database log mode              Archive Mode
Automatic archival             Enabled
Archive destination            /u01/app/oracle/product/19c/dbhome_1/dbs/arch
Oldest online log sequence     21
Next log sequence to archive   23
Current log sequence           23
SQL>  alter database flashback on;

SQL> alter system set db_recovery_file_dest_size=20G scope=both sid='*';;

System altered.

SQL>  alter system set db_recovery_file_dest='/u01/app/oracle/fra/ORCL' scope=both sid='*';
System altered.

SQL>
SQL>  alter database flashback on ;
Database altered.
SQL>
