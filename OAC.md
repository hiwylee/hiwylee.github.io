## OAC
* [excel upload limits : 250 MB and the data column limit for a single file is 250 columns.](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/add-spreadsheets-data-sets-acubi.html#GUID-7A93A9DD-17EE-4BE5-86CB-615095919314)
### Oracle Data Gateway
* [Oracle Data Gateway 5.4.0 Download](https://www.oracle.com/middleware/technologies/oac-downloads.html)
* [Oracle Data Gateway Document](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acabi/typical-workflow-connecting-premise-data-sources.html)
### OAC Data Sync
* [Download](https://www.oracle.com/middleware/technologies/oac-downloads.html)
* [Document](https://download.oracle.com/otn/java/cloud-service/OACDataSync_2_6_Documentation.pdf?AuthParam=1586435835_2b5176e367f254703d0651663f805410)
* [OBE-Loading Data Using Oracle Analytics Cloud Data Sync](https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/oac_bi/loading_data_datasync/datasync_loading.html)
* install procudere
```
unzip OACDataSync_2_6_1.zip
cd OACDataSync_2_6_1

edit config.bat
set JAVA_HOME="C:\Program Files\Java\jdk1.8.0_231"

datasync.bat
```
* 사용자 롤 추가 : OAC console ->  users and roles -> Manage Application Roles : BI Advanced Content Author/  BI Dataload Author / DV Content Author 
