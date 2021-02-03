
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
### [Replication from MySQL to MySQL](https://github.com/oracle/learning-library/blob/master/data-management-library/goldengate/bigdata/mysql-to-mysql/mysql-to-mysql.md) 

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
#### STEP 1: Explore GoldenGate Configuration

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


#### STEP 2: Start GoldenGate Processes
* Go to the GG Home for MySQL

```
[ggadmin@quickstart dirprm]$ cd /u01/gg4mysql
[ggadmin@quickstart gg4mysql]$
```

* Login to ggsci 

```
[ggadmin@quickstart gg4mysql]$ ./ggsci

Oracle GoldenGate Command Interpreter for MySQL
Version 12.2.0.1.1 OGGCORE_12.2.0.1.0_PLATFORMS_151211.1401
Linux, x64, 64bit (optimized), MySQL Enterprise on Dec 11 2015 16:23:51
Operating system character set identified as UTF-8.

Copyright (C) 1995, 2015, Oracle and/or its affiliates. All rights reserved.



GGSCI (quickstart.cloudera) 1> info all

Program     Status      Group       Lag at Chkpt  Time Since Chkpt

MANAGER     STOPPED

GGSCI (quickstart.cloudera) 3> start mgr
Manager started.

GGSCI (quickstart.cloudera) 4> info all

Program     Status      Group       Lag at Chkpt  Time Since Chkpt

MANAGER     RUNNING

```

* create extract, pump, replicat
```
GGSCI (quickstart.cloudera) 2> obey ./dirprm/create_mysql_gg_procs.oby

GGSCI (quickstart.cloudera) 3> add extract extmysql, tranlog, begin now

EXTRACT added.


GGSCI (quickstart.cloudera) 4> add exttrail ./dirdat/et, extract extmysql, megabytes 10

EXTTRAIL added.

GGSCI (quickstart.cloudera) 5>

GGSCI (quickstart.cloudera) 5> add extract pmpmysql, EXTTRAILSOURCE ./dirdat/et

EXTRACT added.


GGSCI (quickstart.cloudera) 6> add rmttrail ./dirdat/rt, extract pmpmysql, megabytes 10

RMTTRAIL added.

GGSCI (quickstart.cloudera) 7>

GGSCI (quickstart.cloudera) 7> add replicat repmysql, exttrail ./dirdat/rt nodbcheckpoint

REPLICAT added.


GGSCI (quickstart.cloudera) 8>

```
* start extractor

```
GGSCI (quickstart.cloudera) 8> start extmysql

Sending START request to MANAGER ...
EXTRACT EXTMYSQL starting


GGSCI (quickstart.cloudera) 9> info all

Program     Status      Group       Lag at Chkpt  Time Since Chkpt

MANAGER     RUNNING
EXTRACT     RUNNING     EXTMYSQL    00:01:21      00:00:06
EXTRACT     STOPPED     PMPMYSQL    00:00:00      00:01:26
REPLICAT    STOPPED     REPMYSQL    00:00:00      00:01:24


GGSCI (quickstart.cloudera) 10>

```

* Start pump
```

GGSCI (quickstart.cloudera) 10> start pmpmysql

Sending START request to MANAGER ...
EXTRACT PMPMYSQL starting


GGSCI (quickstart.cloudera) 11> info all

Program     Status      Group       Lag at Chkpt  Time Since Chkpt

MANAGER     RUNNING
EXTRACT     RUNNING     EXTMYSQL    00:00:00      00:00:06
EXTRACT     RUNNING     PMPMYSQL    00:00:00      00:00:02
REPLICAT    STOPPED     REPMYSQL    00:00:00      00:02:04

```
* start replicat

```
GGSCI (quickstart.cloudera) 12> start repmysql

Sending START request to MANAGER ...
REPLICAT REPMYSQL starting


GGSCI (quickstart.cloudera) 13> info all

Program     Status      Group       Lag at Chkpt  Time Since Chkpt

MANAGER     RUNNING
EXTRACT     RUNNING     EXTMYSQL    00:00:00      00:00:07
EXTRACT     RUNNING     PMPMYSQL    00:00:00      00:00:02
REPLICAT    RUNNING     REPMYSQL    00:00:00      00:00:02


```
### STEP 3:Load Data into Source Database

* loadsource

```
```

* stats repmysql total
```

GGSCI (quickstart.cloudera) 1> stats extmysql total

Sending STATS request to EXTRACT EXTMYSQL ...

Start of Statistics at 2021-02-03 02:30:05.

Output to ./dirdat/et:

Extracting from ggsource.dept to ggsource.dept:

*** Total statistics since 2021-02-03 02:29:38 ***
 Total inserts                               4.00
 Total updates                               0.00
 Total deletes                               0.00
 Total discards                              0.00
 Total operations                            4.00

Extracting from ggsource.emp to ggsource.emp:

*** Total statistics since 2021-02-03 02:29:38 ***
 Total inserts                              14.00
 Total updates                               0.00
 Total deletes                               0.00
 Total discards                              0.00
 Total operations                           14.00

Extracting from ggsource.salgrade to ggsource.salgrade:

*** Total statistics since 2021-02-03 02:29:38 ***
 Total inserts                               5.00
 Total updates                               0.00
 Total deletes                               0.00
 Total discards                              0.00
 Total operations                            5.00

End of Statistics.
```
* stats repmysql total

```
GGSCI (quickstart.cloudera) 2> stats repmysql total

Sending STATS request to REPLICAT REPMYSQL ...

Start of Statistics at 2021-02-03 02:30:17.

Replicating from ggsource.dept to ggtarget.dept:

*** Total statistics since 2021-02-03 02:29:42 ***
 Total inserts                               4.00
 Total updates                               0.00
 Total deletes                               0.00
 Total discards                              0.00
 Total operations                            4.00

Replicating from ggsource.emp to ggtarget.emp:

*** Total statistics since 2021-02-03 02:29:42 ***
 Total inserts                              14.00
 Total updates                               0.00
 Total deletes                               0.00
 Total discards                              0.00
 Total operations                           14.00

Replicating from ggsource.salgrade to ggtarget.salgrade:

*** Total statistics since 2021-02-03 02:29:42 ***
 Total inserts                               5.00
 Total updates                               0.00
 Total deletes                               0.00
 Total discards                              0.00
 Total operations                            5.00

End of Statistics.


GGSCI (quickstart.cloudera) 3>


```

----

### [Replication from MySQL to HDFS](https://github.com/oracle/learning-library/blob/master/data-management-library/goldengate/bigdata/mysql-to-hdfs/mysql-to-hdfs.md)

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


#### Alias

```bash
alias adminmenu='$CONFIG/admin_menu.sh'
alias casscount='clear; $GGCASS/run_count.sh'
alias cassselect='clear; $GGCASS/run_select.sh'
alias config='cd $CONFIG; ls -l'
alias consumetopic='cd $GGKAFKA;./run-consumer.sh'
alias counthbasetables='cd $GGHBASE;./count_tables.sh'
alias cqlsh='clear; $GGCASS/apache-cassandra-3.0.10/bin/cqlsh'
alias createcasskeyspace='clear; $CONFIG/create_cass_keyspace_for_gg.sh'
alias creategg='clear; $CONFIG/create_gg_procs.sh'
alias ddlsource='clear; $CONFIG/mysql_add_column.sh'
alias deletegg='clear; $CONFIG/delete_gg_procs.sh'
alias deletetopics='cd $GGKAFKA;./clear-topics.sh'
alias dmlsource='clear; $CONFIG/mysql_dml_source.sh'
alias dropcasskeyspace='clear; $CONFIG/drop_cass_keyspace_for_gg.sh'
alias drophbasetables='cd $GGHBASE;./drop_tables.sh'
alias gghadoop='cd $GGHADOOP;pwd'
alias ggmysql='cd $GGMYSQL;pwd'
alias ggscihadoop='cd $GGHADOOP; ./ggsci'
alias ggscimysql='cd $GGMYSQL; ./ggsci'
alias hdfscat='hdfs dfs -cat /user/ggtarget/hdfs/*/*'
alias hdfsls='hdfs dfs -ls /user/ggtarget/hdfs/*/*'
alias hdfsrm='hdfs dfs -rm -r /user/ggtarget/hdfs/*'
alias hivecat='hdfs dfs -cat /user/ggtarget/hive/*/*'
alias hivecatavsc='hdfs dfs -cat /user/ggtarget/hive/schema/*'
alias hivels='hdfs dfs -ls /user/ggtarget/hive/*/*'
alias hivelsavsc='hdfs dfs -ls /user/ggtarget/hive/schema/*'
alias hiverm='hdfs dfs -rm -r /user/ggtarget/hive/*'
alias hiveselect='hive -f $GGHIVE/select.hql'
alias infogg='clear; $CONFIG/info_gg.sh'
alias l.='ls -d .* --color=auto'
alias labmenu='$LABS/lab_menu.sh'
alias listhbasetables='cd $GGHBASE;./list_tables.sh'
alias ll='ls -lrt'
alias loadsource='clear; $CONFIG/mysql_load_source.sh'
alias ls='ls --color=auto'
alias mc='. /usr/libexec/mc/mc-wrapper.sh'
alias mysqlreset='clear; $CONFIG/mysql_reset_source_target_schema.sh'
alias mysqlselect='clear; $CONFIG/mysql_select_source_target.sh'
alias mysqlsource='mysql -u ggdemo -poracle -D ggsource'
alias mysqltarget='mysql -u ggdemo -poracle -D ggtarget'
alias mysqltruncsource='clear; $CONFIG/mysql_truncate_source.sh'
alias mysqltrunctarget='clear; $CONFIG/mysql_truncate_target.sh'
alias purgeggtargethadoopfiles='$CONFIG/purge_gg_target_hadoop_files.sh'
alias selecthbasetable='cd $GGHBASE;./scan_table.sh'
alias showtopics='cd $GGKAFKA;./show-topics.sh'
alias startcass='clear; sudo $GGCASS/apache-cassandra-3.0.10/bin/cassandra -f'
alias startgg='clear; $CONFIG/start_gg.sh; sleep 5; infogg'
alias startkafkabroker='cd $GGKAFKA;./start-kafka.sh'
alias statsgg='clear; $CONFIG/stats_gg.sh'
alias statsgghadoop='clear; $CONFIG/stats_gg_hadoop.sh'
alias statsggmysql='clear; $CONFIG/stats_gg_mysql.sh'
alias stopgg='clear; $CONFIG/stop_gg.sh; sleep 5; infogg'
alias vi='vim'
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
```
