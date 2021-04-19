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
DBMCLI> LIST DBSERVER attributes coreCount,cpuCount
         48/48   96/96
```
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
