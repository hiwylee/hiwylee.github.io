## OCI Database Management Service
### Youtube
* [OCI Database Management Service](https://www.youtube.com/playlist?list=PLMmWFDsrq69FISRPkH6p471HZjffhcYiB)

### Prerequisite 
* Dynamic group
```
Instances that meet the criteria defined by any of these rules will be included in the dynamic group.
Row Header
All {instance.compartment.id = 'ocid1.compartment.oc1..aaaaaaaaac74c5vfzs6kmaqti67rqnpzfop4zrtp7uuqaekkxhhysmm3rqla'}
```

* Management Agent : key 생성
* Agent 설치 및 설정
```
[opc@ctrl .ssh]$ ./db21c.sh
Last login: Mon Mar 29 08:22:27 2021 from 140.238.8.213
[opc@db21c ~]$ wget https://objectstorage.ap-chuncheon-1.oraclecloud.com/p/AFcYjeVx7-h5ZeDFQU8F-xekbPD_a0L9trzaLJnCq2yL8wRegK6ZIkG-YgQa-R6s/n/idx9wbxtnehn/b/DBSecLab/o/oracle.mgmt_agent.rpm
--2021-06-13 17:48:44--  https://objectstorage.ap-chuncheon-1.oraclecloud.com/p/AFcYjeVx7-h5ZeDFQU8F-xekbPD_a0L9trzaLJnCq2yL8wRegK6ZIkG-YgQa-R6s/n/idx9wbxtnehn/b/DBSecLab/o/oracle.mgmt_agent.rpm
Resolving objectstorage.ap-chuncheon-1.oraclecloud.com (objectstorage.ap-chuncheon-1.oraclecloud.com)... 134.70.132.2
Connecting to objectstorage.ap-chuncheon-1.oraclecloud.com (objectstorage.ap-chuncheon-1.oraclecloud.com)|134.70.132.2|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 41971204 (40M) [application/octet-stream]
Saving to: 'oracle.mgmt_agent.rpm'

100%[=====================================================================>] 41,971,204  49.6MB/s   in 0.8s

2021-06-13 17:48:45 (49.6 MB/s) - 'oracle.mgmt_agent.rpm' saved [41971204/41971204]

[opc@db21c ~]$ --2021-06-14 02:15:11--  https://objectstorage.ap-chuncheon-1.oraclecloud.com/p/AFcYjeVx7-h5ZeDFQU8F-xekbPD_a0L9trzaLJnCq2yL8wRegK6ZIkG-YgQa-R6s/n/idx9wbxtnehn/b/DBSecLab/o/oracle.mgmt_agent.rpm^C
[opc@db21c ~]$
[opc@db21c ~]$
[opc@db21c ~]$ ls -la
total 41928
drwx------ 4 opc  opc      4096 Jun 13 17:48 .
drwxr-xr-x 5 root root     4096 Jan 19 01:34 ..
-rw------- 1 opc  opc      2736 Mar 29 08:23 .bash_history
-rw-r--r-- 1 opc  opc        18 Nov 22  2019 .bash_logout
-rw-r--r-- 1 opc  opc       193 Nov 22  2019 .bash_profile
-rw-r--r-- 1 opc  opc       231 Nov 22  2019 .bashrc
-rw-r--r-- 1 opc  opc       172 Apr  1  2020 .kshrc
drwx------ 2 opc  opc      4096 Jan 19 01:29 .ssh
-rw------- 1 opc  opc       803 Feb  7 04:12 .viminfo
-rw-rw-r-- 1 opc  opc    921600 Feb 21 13:33 coet_1010._NICEtar.tar
-rw-rw-r-- 1 opc  opc  41971204 Jun 13 17:14 oracle.mgmt_agent.rpm
drwxrwxr-x 2 opc  opc      4096 Feb  7 04:12 pga
[opc@db21c ~]$ sudo rpm  -ivh oracle.mgmt_agent.rpm
Preparing...                          ################################# [100%]
Checking pre-requisites
        Checking if any previous agent service exists
        Checking if OS has systemd or initd
        Checking available disk space for agent install
        Checking if /opt/oracle/mgmt_agent directory exists
        Checking if 'mgmt_agent' user exists
        Checking Java version
                JAVA_HOME is not set or not readable to root
                Trying default path /usr/bin/java
                Java version: 1.8.0_271 found at /usr/bin/java
        Checking agent version
Updating / installing...
   1:oracle.mgmt_agent-210528.1918-1  ################################# [100%]

Executing install
        Unpacking software zip
        Copying files to destination dir (/opt/oracle/mgmt_agent)
        Initializing software from template
        Creating 'mgmt_agent' daemon
        Agent Install Logs: /opt/oracle/mgmt_agent/installer-logs/installer.log.0

        Setup agent using input response file (run as any user with 'sudo' privileges)
        Usage:
                sudo /opt/oracle/mgmt_agent/agent_inst/bin/setup.sh opts=[FULL_PATH_TO_INPUT.RSP]

Agent install successful

[opc@db21c ~]$ sudo vi  /opt/oracle/mgmt_agent/input.rsp
[opc@db21c ~]$ cat /opt/oracle/mgmt_agent/input.rsp
cat: /opt/oracle/mgmt_agent/input.rsp: Permission denied
[opc@db21c ~]$ sudo cat /opt/oracle/mgmt_agent/input.rsp
ManagementAgentInstallKey=Mi4wLGFwLWNodW5jaGVvbi0xLG9jaWQxLnRlbmFuY3kub2MxLi5hYWFhYWFhYWxjc3NmZWFtdGplYndxbnFxam5xejZybnhsNXhzdDR1ZXhoYjVsN3hjZ2o1NG9pcjZocXEsb2NpZDEubWFuYWdlbWVudGFnZW50aW5zdGFsbGtleS5vYzEuYXAtY2h1bmNoZW9uLTEuYW1hYWFhYWFqZTVoYmNxYW9qbGs0eXN3aHduamxkNXM3b3ZmN3N1dnB5cHdienFsdGk3c283dGJ3cjJhLElGTUMwbkpsR1N4NEZhSWMtYTVkNGVjcnVpUWxPQVFZV0NkeTNPUVE=
CredentialWalletPassword=OracleWelcome123##
[opc@db21c ~]$ sudo /opt/oracle/mgmt_agent/agent_inst/bin/setup.sh opts=/opt/oracle/mgmt_agent/input.rsp

Executing configure

        Parsing input response file
        Validating install key
        Generating communication wallet
        Generating security artifacts
        Registering Management Agent

Starting agent...
Agent started successfully


Agent setup completed and the agent is running.
In the future agent can be started by directly running: sudo systemctl start mgmt_agent

Please make sure that you delete /opt/oracle/mgmt_agent/input.rsp or store it in secure location.
```
