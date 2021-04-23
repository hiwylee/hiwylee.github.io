### 엑사데이터 CoD 관련 확인

* 장착된 CPU 확인
```
*[root@krx8maceladm01 ~]# lscpu | egrep 'Model name|Socket|Thread|NUMA|CPU\(s\)'
CPU(s):                96
On-line CPU(s) list:   0-95
Thread(s) per core:    2
Socket(s):             2
NUMA node(s):          2
Model name:            Intel(R) Xeon(R) Platinum 8260 CPU @ 2.40GHz
NUMA node0 CPU(s):     0-23,48-71
NUMA node1 CPU(s):     24-47,72-95

[root@krx8maceladm01 ~]#
```
* CoD 확인

```
LIST DBSERVER [ name |  attribute_filters ]  [attribute_list]  [DETAIL]
```

```bash
$ su -
$ dbmcli

DBMCLI> LIST DBSERVER DETAIL
         name:                   krx8madb01
         bbuStatus:              normal
         coreCount:              48/48
         cpuCount:               96/96
         ...
         temperatureStatus:      normal
         upTime:                 18 days, 16:29
         msStatus:               running
         rsStatus:               running


```

```
DBMCLI> LIST DBSERVER attributes coreCount
         48/48 
```

* core count 48 = CPU_COUNT=96 : `` one physical core== 2 hyper threading  ``

* CoD 변경

```
$ su -



$ dbmcli
DBMCLI> alter dbserver pendingCoreCount=신규 테이블
DBMCLI> list dbserver attributes pendingCoreCount
서버 재기동
$ dbmcli
DBMCLI> list dbserver attributes coreCount
```

### 3 node rac CoD

```
DBMCLI> LIST DBSERVER attributes coreCount
```
* Example below from an Exadata X7-2, from 3 database compute nodes. The example below shows only 16 out of the total 48 physical cores are enabled.

```bash
[root@prod_node1 ~]# dbmcli
DBMCLI: Release  - Production on Wed Jul 24 00:06:08 GMT-00:00 2019 Copyright (c) 2007, 2016, Oracle and/or its affiliates. All rights reserved. 
DBMCLI> LIST DBSERVER attributes coreCount         
16/48
[root@prod_node2 ~]# dbmcli
DBMCLI: Release  - Production on Wed Jul 24 00:32:34 GMT 2019 Copyright (c) 2007, 2016, Oracle and/or its affiliates. All rights reserved.
DBMCLI> LIST DBSERVER attributes coreCount         
16/48                          
[root@prod_node3 ~]# dbmcli
DBMCLI: Release  - Production on Wed Jul 24 00:35:20 GMT 2019 Copyright (c) 2007, 2016, Oracle and/or its affiliates. All rights reserved.
DBMCLI> LIST DBSERVER attributes coreCount         
16/48
```

```
DBMCLI> help list dbserver

  Usage: LIST DBSERVER [<attribute_list>] [DETAIL]

  Purpose: Displays specified attributes for the DBSERVER.

  Arguments:
    <attribute_list>: The attributes that are to be displayed.
                      ATTRIBUTES {ALL | attr1 [, attr2]... }

  Options:
    [DETAIL]: Formats the display as an attribute on each line, with
              an attribute descriptor preceding each value.

  Examples:
    LIST DBSERVER attributes status, upTime
    LIST DBSERVER DETAIL

DBMCLI> LIST DBSERVER DETAIL
> ;
         name:                   krx8madb01
         bbuStatus:              normal
         coreCount:              48/48
         cpuCount:               96/96
         diagHistoryDays:        7
         fanCount:               16/16
         fanStatus:              normal
         httpsAccess:            ALL
         id:                     1951XLB063
         interconnectCount:      2
         interconnect1:          re0
         interconnect2:          re1
         ipaddress1:             192.168.10.10/22
         ipaddress2:             192.168.10.11/22
         kernelVersion:          4.14.35-1902.306.2.1.el7uek.x86_64
         locatorLEDStatus:       off
         makeModel:              Oracle Corporation ORACLE SERVER X8-2
         metricHistoryDays:      7
         msVersion:              OSS_20.1.4.0.0_LINUX.X64_201118
         powerCount:             2/2
         powerStatus:            normal
         releaseImageStatus:     success
         releaseVersion:         20.1.4.0.0.201118
         releaseTrackingBug:     32134924
         status:                 online
         temperatureReading:     21.0
         temperatureStatus:      normal
         upTime:                 1 days, 9:34
         msStatus:               running
         rsStatus:               running


```
