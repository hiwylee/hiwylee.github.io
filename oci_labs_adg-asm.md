###  Oracle Database Hybrid Active Data Guard Workshop

### STEP 2 : Stnady DB - ASM
---
### Manually Delete the standby Database Created by Tooling
* list datafile to delete and create pfile

```sql
SQL> set heading off linesize 999 pagesize 0 feedback off trimspool on
SQL> select 'asmcmd rm '||name from v$datafile union all select 'asmcmd rm '||name from v$tempfile union all select 'asmcmd rm '||member from v$logfile;
asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/system.261.1063135085
asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/sysaux.262.1063135139
asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/undotbs1.263.1063135165
asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/system.265.1063135303
asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/sysaux.266.1063135303
asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/undotbs1.267.1063135303
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/system.276.1063136557
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/sysaux.271.1063136571
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/undotbs1.272.1063136583
asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/users.274.1063136535
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/users.275.1063136537
asmcmd rm +DATA/ORCL_YNY1ZH/TEMPFILE/temp.264.1063135255
asmcmd rm +DATA/ORCL_YNY1ZH/BA0FEC6E998B2498E0530300000A0303/TEMPFILE/temp.268.1063135343
asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/TEMPFILE/temp.270.1063136605
asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_3.259.1063135221
asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_2.258.1063135221
asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_1.257.1063135221
SQL>
SQL> create pfile='/tmp/ORCL_yny1zh.pfile' from spfile;
SQL> exit;
Disconnected from Oracle Database 19c EE High Perf Release 19.0.0.0.0 - Production
Version 19.7.0.0.0
[oracle@dbstby .ssh]$
```
* collect the configuration of the database for future reference

``` sql
[oracle@dbstby ~]$ srvctl config database -d ORCL_yny1zh > /tmp/ORCL_yny1zh.config
[oracle@dbstby ~]$ cat /tmp/ORCL_yny1zh.config
Database unique name: ORCL_yny1zh
Database name: ORCL
Oracle home: /u01/app/oracle/product/19.0.0.0/dbhome_1
Oracle user: oracle
Spfile: +DATA/ORCL_YNY1ZH/PARAMETERFILE/spfile.269.1063135725
Password file:
Domain: sub01291310280.standbyvcn.oraclevcn.com
Start options: open
Stop options: immediate
Database role: PRIMARY
Management policy: AUTOMATIC
Server pools:
Disk Groups: RECO,DATA
Mount point paths:
Services:
Type: SINGLE
OSDBA group: dba
OSOPER group: dbaoper
Database instance: ORCL
Configured nodes: dbstby
CSS critical: no
CPU count: 0
Memory target: 0
Maximum memory: 0
Default network number for database services:
Database is administrator managed
```

* shutdown db 

```bash
[oracle@dbstby ~]$ srvctl stop database -d ORCL_yny1zh -o immediate
PRCC-1016 : ORCL_yny1zh was already stopped
[oracle@dbstby ~]$

```

* delete datafile

``` bash
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/system.261.1063135085
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/sysaux.262.1063135139
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/undotbs1.263.1063135165
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/system.265.1063135303
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/sysaux.266.1063135303
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/A32A6F1B654641A5E053C105F40A57F6/DATAFILE/undotbs1.267.1063135303
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/system.276.1063136557
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/sysaux.271.1063136571
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/undotbs1.272.1063136583
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/DATAFILE/users.274.1063136535
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/DATAFILE/users.275.1063136537
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/TEMPFILE/temp.264.1063135255
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA0FEC6E998B2498E0530300000A0303/TEMPFILE/temp.268.1063135343
[oracle@dbstby .ssh]$ asmcmd rm +DATA/ORCL_YNY1ZH/BA101347BDF4500AE0530300000ADC61/TEMPFILE/temp.270.1063136605
[oracle@dbstby .ssh]$ asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_3.259.1063135221
[oracle@dbstby .ssh]$ asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_2.258.1063135221
[oracle@dbstby .ssh]$ asmcmd rm +RECO/ORCL_YNY1ZH/ONLINELOG/group_1.257.1063135221

```

### Copy the Password File and wallet file to the standby
* Copy the Password File

```bash

[oracle@dbstby .ssh]$ scp oracle@primary:/u01/app/oracle/product/19c/dbhome_1/dbs/orapwORCL /tmp
orapwORCL   
```

* copy wallet file from primary (/u01/app/oracle/admin/ORCL/wallet)
```
```
* Switch to **grid** user, use asmcmd, replace ORCL_nrt1d4 with your standby db unique name, using capital letters in the directory names

```
[oracle@dbstby .ssh]$ exit
logout
[opc@dbstby .ssh]$ sudo su - grid
Last login: Sat Jan 30 07:02:15 UTC 2021
[grid@dbstby ~]$
[grid@dbstby ~]$ asmcmd
ASMCMD> pwdcopy --dbuniquename ORCL_yny1zh -f /tmp/orapwORCL +DATA/ORCL_YNY1ZH
ASMCMD-8022: unknown command 'pwdcopy' specified
ASMCMD> pwcopy --dbuniquename ORCL_yny1zh -f /tmp/orapwORCL +DATA/ORCL_YNY1ZH
copying /tmp/orapwORCL -> +DATA/ORCL_YNY1ZH/ORCL_YNY1ZH
ASMCMD-9453: failed to register password file as a CRS resource
ASMCMD>

```

* ASMCMD-9453: failed to register password file as a CRS resource then as the **oracle** user execute the following

```
[oracle@dbstby ~]$ id
uid=101(oracle) gid=1001(oinstall) groups=1001(oinstall),1002(dbaoper),1003(dba),1006(asmdba)
[oracle@dbstby ~]$ srvctl modify database -db ORCL_yny1zh -pwfile '+DATA/ORCL_yny1zh/orapwORCL_yny1zh'
[oracle@dbstby ~]$

```

* Verify the password file is registered correctly (as **oracle** user)

```
[oracle@dbstby ~]$ id
uid=101(oracle) gid=1001(oinstall) groups=1001(oinstall),1002(dbaoper),1003(dba),1006(asmdba)
[oracle@dbstby ~]$ srvctl config  database -db ORCL_yny1zh
Database unique name: ORCL_yny1zh
Database name: ORCL
Oracle home: /u01/app/oracle/product/19.0.0.0/dbhome_1
Oracle user: oracle
Spfile: +DATA/ORCL_YNY1ZH/PARAMETERFILE/spfile.269.1063135725
Password file: +DATA/ORCL_yny1zh/orapwORCL_yny1zh
Domain: sub01291310280.standbyvcn.oraclevcn.com
Start options: open
Stop options: immediate
Database role: PRIMARY
Management policy: AUTOMATIC
Server pools:
Disk Groups: RECO,DATA
Mount point paths:
Services:
Type: SINGLE
OSDBA group: dba
OSOPER group: dbaoper
Database instance: ORCL
Configured nodes: dbstby
CSS critical: no
CPU count: 0
Memory target: 0
Maximum memory: 0
Default network number for database services:
Database is administrator managed
[oracle@dbstby ~]$

```
### Configure Static Listeners

```sql
```
### TNS Entries for Redo Transport

```sql
```
### Instantiate the Standby Database

```sql
```
### Clear all online and standby redo logs

```sql
```
### Configure Data Guard broker
