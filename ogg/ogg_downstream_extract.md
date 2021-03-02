## downstream integrated capture
* [Downstream Mining Configuration 예제-Realtime mode](https://docs.oracle.com/goldengate/c1230/gg-winux/GGODB/example-downstream-mining-configuration.htm#GGODB-GUID-41D56EB7-0C14-438C-8791-8F93CB0DCAF8)
### Basic 
* [Oracle GoldenGate 문서](https://docs.oracle.com/en/middleware/goldengate/index.html)
* [** Best Practices from Oracle Development's A‑Team**](https://www.ateam-oracle.com/oracle-goldengate-best-practice-goldengate-downstream-extract-with-oracle-data-guard)
* [Configuring Oracle GoldenGate OGG 11gR2 downstream integrated capture](https://gjilevski.com/2012/10/31/configuring-oracle-goldengate-ogg-11gr2-downstream-integrated-capture/)

* [Extracting Data in Oracle GoldenGate Integrated Capture Mode](https://www.oracle.com/technetwork/database/availability/8398-goldengate-integrated-capture-1888658.pdf)
* https://www.oracle-scn.com/oracle-goldengate-integrated-capture/

### Important MOS Notes
* Specific patches for Integrated Capture: 1411356.1
* Integrated Capture health check script 1448324.1
* OGG Best Practices: Configuring Downstream Integrated Capture 1485620.1
* Performance Tuning for OGG [1488668.1](https://mosemp.us.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=540428795909541&id=1488668.1&_adf.ctrl-state=nrjz6fd9l_229)

### 테스트 시나리오 
* 환경
  * source : 2 node rac db 11.2.0.2   // ogg 12.2.0.0
  * mining : single db 12.2.0.1        
  * target : 2 node RAC               // ogg 19.1.0.0
 * 테스트 내용
   * Realtime downstream
   * standby redo log shipping delay
   * online redo log shipping
   * extract perf
   * apply perf
### 테스트

### User
* ``primary DB``
  * user : ggadm1 /DB :  orcl  / ogg alias : ggadm1, logins as  ggadm1@orcl
* ``Mining DB``
  * user : ggadmcap   /DB :  db21c  / ogg alias : ggadmcap , logins as  ggadmcap@db21c
#### Source Database 준비 :-> primary : 1x2.xx.197,86
```
[oracle@db21c ~]$ env | grep SID
ORACLE_SID=DB0901
```
#### Mining Database 준비 : db21c :  1x0.xxx.x.213

* Prepare the Mining Database to Archive its Local Re

```sql
SYS@db21> startup mount;
alter databseORACLE instance started.

Total System Global Area 3.0602E+10 bytes
Fixed Size                 14423176 bytes
Variable Size            3758096384 bytes
Database Buffers         2.6776E+10 bytes
Redo Buffers               52682752 bytes
archievelog;Database mounted.
SYS@db21> alter database archivelog;

Database altered.

Elapsed: 00:00:00.00
SYS@db21> alter database open;

Database altered.

Elapsed: 00:00:07.80

SYS@db21> archive log list
Database log mode              Archive Mode
Automatic archival             Enabled
Archive destination            USE_DB_RECOVERY_FILE_DEST
Oldest online log sequence     14
Next log sequence to archive   16
Current log sequence           16

SYS@db21> show parameter db_recovery_file_dest

NAME                                 TYPE                   VALUE
------------------------------------ ---------------------- ------------------------------
db_recovery_file_dest                string                 /u03/app/oracle/fast_recovery_area
db_recovery_file_dest_size           big integer            250G

```

* arhive log 위치

```
[oracle@db21c DB21_KIX1T6]$ ls -l
total 18616
drwxr-x--- 15 oracle oinstall     4096 Feb 27 12:42 archivelog
drwxr-x---  3 oracle oinstall     4096 Jan 19 01:37 autobackup
-rw-r-----  1 oracle oinstall 19054592 Feb 27 13:18 control02.ctl
[oracle@db21c DB21_KIX1T6]$ cd /u03/app/oracle/fast_recovery_area/
[oracle@db21c fast_recovery_area]$ ls -l
total 8
drwxr-x--- 6 oracle oinstall 4096 Jan 19 02:29 CDB21
drwxr-x--- 4 oracle oinstall 4096 Jan 19 01:37 DB21_KIX1T6
[oracle@db21c fast_recovery_area]$ cd DB21_KIX1T6/
[oracle@db21c DB21_KIX1T6]$ ls -l
total 18616
drwxr-x--- 15 oracle oinstall     4096 Feb 27 12:42 archivelog
drwxr-x---  3 oracle oinstall     4096 Jan 19 01:37 autobackup
-rw-r-----  1 oracle oinstall 19054592 Feb 27 13:18 control02.ctl
[oracle@db21c DB21_KIX1T6]$

```


* set log_archive_dest_1 to archive local red & Enable log_archive_dest_1
```
SYS@db21> ALTER SYSTEM SET log_archive_dest_1='LOCATION=/u03/app/oracle/arc_dest/local VALID_FOR=(ONLINE_LOGFILE, PRIMARY_ROLE)';


```

* Prepare the Mining Database to Archive Redo Received in Standby Redo Logs from the Source Database

```sql
SYS@db21> ed
Wrote file afiedt.buf

  1*  alter system set log_archive_dest_2='LOCATION=/u03/app/oracle/sr1_orcl, VALID_FOR=(STANDBY_LOGFILE,PRIMARY_ROLE)'
SYS@db21> /

System altered.

Elapsed: 00:00:00.03
```

* Prepare the Source Database to Send Redo to the Mining Database
  *  Make sure that the source database is running with the required compatibility
  *  tnsname.ora
 
 ```
 db21_kix1t6 =
 (DESCRIPTION =
     (SDU=65536)
     (RECV_BUF_SIZE=134217728)
     (SEND_BUF_SIZE=134217728)
     (ADDRESS_LIST =
     (ADDRESS = (PROTOCOL = TCP)(HOST = db21)(PORT = 1521))
     )
     (CONNECT_DATA =
        (SERVER = DEDICATED)
         (SERVICE_NAME = db21_kix1t6.sub01190114250.oskvcn.oraclevcn.com)
        (UR=A)
     )
  )

 ```
  *  Set DG_CONFIG at the source database.

```sql
SQL> ed
Wrote file afiedt.buf

  1*   alter system set log_archive_config='dg_config=(ORCL,orcl_yny1zh,orcl_yny166, db21_kix1t6)';

System altered.

```
  *  Set up redo transport at the source database.
  
```sql
 ALTER  SYSTEM SET log_archive_dest_4='service="db21_kix1t6" ASYNC optional db_unique_name="db21_kix1t6" valid_for=(online_logfile,primary_roles)'
  2  /

System altered.
  
```
    
  *  Enable the downstream destination.
    
```sql
SQL> ALTER SYSTEM SET LOG_ARCHIVE_DEST_STATE_4=ENABLE;

System altered.

SQL>

```

### ogg 설정

#### primary DB
#### 마이닝 DB
* 참조문서 : https://m.blog.naver.com/xogstar/221804735194
#### target DB
