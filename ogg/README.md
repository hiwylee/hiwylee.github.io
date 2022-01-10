## OGG 정보 모음
* [ogg 설치](ogg_install.md)
* [ogg_byte_order.md](ogg_byte_order.md)
* [ogg_cert.md](ogg_cert.md)
* [ogg_downstream_extract.md](ogg_downstream_extract.md)
* [Step by Step Golden Gate Installation-ogg_stepbystep.md](ogg_stepbystep.md)

### Oracle GoldenGate Best Practices
* [Oracle GoldenGate Performance Best Practices-Oracle Exadata Database Machine and Oracle MAA  ](ogg_basic.md)
* [Oracle GoldenGate Best Practices-GoldenGate Capture from a DataGuard with Cascaded Redo Logs](ogg_ds.md)
### Live Labs
*	[Replicating Data Using Oracle Cloud Infrastructure GoldenGate Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=797)
* [GoldenGate 19c Microservices](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=585)
* [Migrate an HR database and APEX application using GoldenGate](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=907)

### OGG Classic <--> OCI GG
* [Send Data from Oracle GoldenGate to OCI GoldenGate](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=851)
* [Send Data from OCI GoldenGate to Oracle GoldenGate](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=881)

### OGG LEVEL 300
* [GoldenGate 19c Microservices Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=585) 
*	[Get Started with Oracle GoldenGate Veridata Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=833&session=110083238267524)
*	[GoldenGate for Big Data Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?p180_id=692)
*	[oracle GoldenGate Stream Analytics Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/view-workshop?wid=669)

### OCI GG CMD LINE

* [$OGG_HOME/bin/adminclient 사용](adminclient.md)
 
 ```bash
 cd $OGG_HOME/bin
 ./adminclient
 OGG (not connected) 1> connect https://ggma.livelabs.oraclevcn.com:16000 as oggadmin password Welcome1 !
 using default deployment `Atlanta`
 OGG (https://ggma.livelabs.oraclevcn.com:16000/) 2> info all
 program Status Group Lag at Chkpt Time Since Chkpt
 
 ADMINSRVC RUNNING
 DISTSRVC RUNNING
 PMRVC RUNNING
 RECVSRVC RUNNING
 
 OGG (https://ggma.livelabs.oraclevcn.com:16000/) 3> HELP
 ....
 ```


