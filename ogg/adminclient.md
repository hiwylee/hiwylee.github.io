### OCI GG CMD LINE - adminclient

* [$OGG_HOME/bin/adminclient 사용](adminclient.md)

* connect 끝에 ! 가 있어야 함: The exclamation point (!) is very important. Without it, the command fails and returns an error.

```bash
 /u01/app/ogg/bin,
 ./adminclient
 connect <OCI-GoldenGate-deployment-url> as <OCI-GoldenGate-user> password <OCI-GoldenGate-password> !
 info all
 stats <extract-name>
 view messages
 purge exttrail <trail-file-name>
 ```
 
 ```
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
