### 엑사데이터 CoD 관련 확인
* CoD 확인

```
LIST DBSERVER [ name |  attribute_filters ]  [attribute_list]  [DETAIL]
```

```bash
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
