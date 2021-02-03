
## GoldenGate for Big Data Workshop
#### Lab Overview
* [GoldenGate for Big Data Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=692&p210_type=3&session=100853554759047)
* Arhitecture
![Arhitecture](https://oracle.github.io/learning-library/data-management-library/goldengate/bigdata/introduction/images/image110_1.png)
* Labs
  * Lab1 : Replication from MySQL to MySQL 
  * Lab2 : Replication from MySQL to HDFS
  * Lab3 : Replication from MySQL to Hive 
  * Lab4 : Replication from MySQL to HBase
  * Lab5 : Replication from MySQL to Kafka 
  * Lab6 : Replication from MySQL to Cassandra 
  * Lab7 : Replication from MySQL to Oracle 
----

### Deploy GoldenGate for Big Data

*
```
sudo su - ggadmin

************************************************************************
*             Oracle GoldenGate for Big Data - Lab Menu                *
************************************************************************
*                                                                      *
* [1] Lab : Deploy GoldenGate for Big Data                             *
* [2] Lab : MySQL --> MySQL one-way replication                        *
* [3] Lab : MySQL --> HDFS (delimited text format )                    *
* [4] Lab : MySQL --> Hive (Avro format)                               *
* [5] Lab : MySQL --> HBase                                            *
* [6] Lab : MySQL --> Kafka (Json format)                              *
* [7] Lab : MySQL --> Cassandra                                        *
*                                                                      *
* [I] Auto-install OGG for Big Data                                    *
* [R] Lab Reset (Cleanup all procs & files)                            *
*                                                                      *
* [Q] Exit                                                             *
*                                                                      *
************************************************************************
Enter your menu choice [1-7, I, R, Q]: 1

```

```
***************************************************************************************************
*                         Installing Oracle GoldenGate for Big Data Lab                           *
***************************************************************************************************
*                                                                                                 *
* - GoldenGate for MySQL has been pre-installed in /u01/gg4mysql                                  *
*                                                                                                 *
* - To install GoldenGate for Big Data, execute the following steps in another window             *
*   1) cd /u01/gg4hadoop123010                                                                    *
*                                                                                                 *
* - The downloaded software has been copied to /u01/gg_binaries                                   *
*   2) tar -xvf /u01/gg_binaries/gg4hadoop123010/ggs_Adapters_Linux_x64.tar                       *
*                                                                                                 *
* - Connect to the GG command line interface (ggsci)                                              *
*   3) ./ggsci                                                                                    *
*                                                                                                 *
* - Run the following command to create the required sub-directories, then exit from ggsci        *
*   4) create subdirs                                                                             *
*   5) exit                                                                                       *
*                                                                                                 *
***************************************************************************************************

Press ENTER to return to the Lab Menu or Q to quit:q

```

* To install and configure GoldenGate

```bash
cd /u01/gg4hadoop123010
tar -xvf  /u01/gg_binaries/gg4hadoop123010/ggs_Adapters_Linux_x64.tar
```

* GoldenGate command line interface (ggsci) 

```
[ggadmin@quickstart gg4hadoop123010]$ ./ggsci

Oracle GoldenGate Command Interpreter
Version 12.2.0.1.160823 OGGCORE_OGGADP.12.2.0.1.0_PLATFORMS_161019.1437
Linux, x64, 64bit (optimized), Generic on Oct 19 2016 16:01:40
Operating system character set identified as UTF-8.

Copyright (C) 1995, 2016, Oracle and/or its affiliates. All rights reserved.



GGSCI (quickstart.cloudera) 1> info all

Program     Status      Group       Lag at Chkpt  Time Since Chkpt

MANAGER     STOPPED


GGSCI (quickstart.cloudera) 2>

```

* 

----
### Replication from MySQL to MySQL 

*  Architectue
![](https://oracle.github.io/learning-library/data-management-library/goldengate/bigdata/mysql-to-mysql/images/image200_1.png)

* 
```
uid=504(ggadmin) gid=504(ggadmin) groups=504(ggadmin),27(mysql),474(vboxsf),501(cloudera)
[ggadmin@quickstart labs]$ labmenu

```

```
***************************************************************************************************
*                     MySQL --> MySQL uni-directional replication Lab                             *
***************************************************************************************************
*                                                                                                 *
* - In this lab, you'll configure GG to capture from MySQL (database: ggsource) and               *
*   deliver to MySQL (database: ggtarget)                                                         *
*                                                                                                 *
* - Review the following files before running through the lab                                     *
*   1) cat /u01/gg4mysql/dirprm/create_mysql_gg_procs.oby                                         *
*   2) cat /u01/gg4mysql/dirprm/mgr.prm                                                           *
*   3) cat /u01/gg4mysql/dirprm/extmysql.prm                                                      *
*   4) cat /u01/gg4mysql/dirprm/pmpmysql.prm                                                      *
*   5) cat /u01/gg4mysql/dirprm/repmysql.prm                                                      *
*                                                                                                 *
* - Follow the steps in the Student Handbook to complete this lab                                 *
*                                                                                                 *
***************************************************************************************************

Press ENTER to return to the Lab Menu or Q to Quit:

```

```
[ggadmin@quickstart ~]$ cd /u01/gg4mysql/dirprm
```

* [ggadmin@quickstart dirprm]$ cat  create_mysql_extract.oby

```
-- dblogin sourcedb ggsource, userid ggdemo password oracle
-- delete extract extmysql
--add trandata ggsource.*
add extract extmysql, tranlog, begin now
add exttrail ./dirdat/et, extract extmysql, megabytes 10
```

* [ggadmin@quickstart dirprm]$ vi mgr.prm

```
port 8000
```
[ggadmin@quickstart dirprm]$
```

* [ggadmin@quickstart dirprm]$ cat extmysql.prm

```
extract extmysql

SETENV (MYSQL_UNIX_PORT="/var/lib/mysql/mysql.sock")

sourcedb ggsource, userid ggdemo, password oracle
exttrail ./dirdat/et

TRANLOGOPTIONS ALTLOGDEST "/var/lib/mysql/mysql-bin.index"

NOCOMPRESSUPDATES
NOCOMPRESSDELETES
GETUPDATEBEFORES

table ggsource.*;

```

* [ggadmin@quickstart dirprm]$ cat  /u01/gg4mysql/dirprm/pmpmysql.prm

```
extract pmpmysql

RMTHOST localhost, MGRPORT 8000

exttrail ./dirdat/rt

passthru

REPORTCOUNT EVERY 60 SECONDS, RATE

table ggsource.*;
[ggadmin@quickstart dirprm]$

```
*  cat /u01/gg4mysql/dirprm/repmysql.prm

```
replicat repmysql

SETENV (MYSQL_UNIX_PORT="/var/lib/mysql/mysql.sock")

targetdb ggtarget, userid ggdemo, password oracle
discardfile ./dirrpt/repmysql.dsc, purge

map ggsource.*, target ggtarget.*;
[ggadmin@quickstart dirprm]$

```
----
### Replication from MySQL to HDFS

*
```
```

----
### Replication from MySQL to Hive 

*
```
```

----
### Replication from MySQL to HBase

*
```
```

----
### Replication from MySQL to Kafka 

*
```
```

----
### Replication from MySQL to Cassandra 

*
```
```

----
### Replication from MySQL to Oracle 

*
```
```
