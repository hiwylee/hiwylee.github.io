## [ Backup Oracle database to OCI Object storage.](https://www.oraclecloudadmin.com/2020/08/backup-oracle-database-to-oci-object.html)

### 참조 
* [ Backup Oracle database to OCI Object storage.](https://www.oraclecloudadmin.com/2020/08/backup-oracle-database-to-oci-object.html)
* [Backing Up a Database to Object Storage Using RMAN(https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Tasks/backingupOSrman.htm#prerequisites)
* oci authentication changed .
#### Installing the Backup Module on the DB System

```bash
[oracle@rat odbcs]$ cat install.sh
java -jar opc_install.jar -opcId 'oracleidentitycloudservice/wonyong.lee@oracle.com' -opcPass 'pPB7jSBHz(:D4HvzyWb}' -container DB_BACKUP -walletDir ~/wallet/ -libDir ~/lib/ -configfile ~/config -host https://swiftobjectstorage.ap-chuncheon-1.oraclecloud.com/v1/idx9wbxtnehn

[oracle@rat odbcs]$ sh install.sh
Oracle Database Cloud Backup Module Install Tool, build 12.2.0.1.0DBBKPCSBP_2018-06-12
Backups would be sent to container DB_BACKUP.
Oracle Database Cloud Backup Module wallet created in directory /home/oracle/wallet.
Oracle Database Cloud Backup Module initialization file /home/oracle/config created.
Downloading Oracle Database Cloud Backup Module Software Library from file opc_linux64.zip.
Download complete.
[oracle@rat odbcs]$

```

#### Configuring RMAN


```sql
[oracle@rat ~]$ rman target=/

Recovery Manager: Release 19.0.0.0.0 - Production on Tue Nov 24 18:32:15 2020
Version 19.9.0.0.0

Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.

connected to target database: PROD (DBID=468584496)

RMAN> show all
2> ;

using target database control file instead of recovery catalog
RMAN configuration parameters for database with db_unique_name PROD_YNY1HG are:
CONFIGURE RETENTION POLICY TO REDUNDANCY 1; # default
CONFIGURE BACKUP OPTIMIZATION OFF; # default
CONFIGURE DEFAULT DEVICE TYPE TO DISK;
CONFIGURE CONTROLFILE AUTOBACKUP ON;
CONFIGURE CONTROLFILE AUTOBACKUP FORMAT FOR DEVICE TYPE DISK TO '%F'; # default
CONFIGURE DEVICE TYPE DISK PARALLELISM 1 BACKUP TYPE TO BACKUPSET; # default
CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE DISK TO 1; # default
CONFIGURE ARCHIVELOG BACKUP COPIES FOR DEVICE TYPE DISK TO 1; # default
CONFIGURE CHANNEL DEVICE TYPE DISK FORMAT   '/u03/app/oracle/fast_recovery_area/PROD_YNY1HG/backups/rat_%U';
CONFIGURE MAXSETSIZE TO UNLIMITED; # default
CONFIGURE ENCRYPTION FOR DATABASE OFF; # default
CONFIGURE ENCRYPTION ALGORITHM 'AES128'; # default
CONFIGURE COMPRESSION ALGORITHM 'BASIC' AS OF RELEASE 'DEFAULT' OPTIMIZE FOR LOAD TRUE ; # default
CONFIGURE RMAN OUTPUT TO KEEP FOR 7 DAYS; # default
CONFIGURE ARCHIVELOG DELETION POLICY TO NONE; # default
CONFIGURE SNAPSHOT CONTROLFILE NAME TO '/u01/app/oracle/product/19.0.0/dbhome_1/dbs/snapcf_prod.f'; # default

RMAN>

```