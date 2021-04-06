## OGG 설치 ( Linux) 
### silent mode 설치하기
* download ogg : [위치](https://www.oracle.com/kr/middleware/technologies/goldengate-downloads.html)
* unzip ogg

```
[oracle@rac1 ogg]$ unzip 191004_fbo_ggs_Linux_x64_shiphome.zip
...
  inflating: fbo_ggs_Linux_x64_shiphome/Disk1/stage/sizes/oracle.oggcore.top.19.1.0.0.0.sizes.properties
  inflating: fbo_ggs_Linux_x64_shiphome/Disk1/stage/sizes/oracle.oggcore.top19.1.0.0.0ora11g.sizes.properties
  inflating: fbo_ggs_Linux_x64_shiphome/Disk1/stage/sizes/oracle.oggcore.top19.1.0.0.0ora12c.sizes.properties
  inflating: fbo_ggs_Linux_x64_shiphome/Disk1/stage/sizes/oracle.oggcore.top19.1.0.0.0ora18c.sizes.properties
  inflating: fbo_ggs_Linux_x64_shiphome/Disk1/stage/sizes/oracle.oggcore.top19.1.0.0.0ora19c.sizes.properties
  inflating: OGG-19.1.0.0-README.txt
  inflating: OGG_WinUnix_Rel_Notes_19.1.0.0.4.pdf

[oracle@rac1 ogg]$ ls -l
total 543548
-rw-r--r-- 1 oracle oinstall 556240981 Mar  2 09:05 191004_fbo_ggs_Linux_x64_shiphome.zip
-rw-r--r-- 1 oracle oinstall      1413 May 29  2019 OGG-19.1.0.0-README.txt
-rw-r--r-- 1 oracle oinstall    332523 Oct 21  2019 OGG_WinUnix_Rel_Notes_19.1.0.0.4.pdf
drwxr-xr-x 3 oracle oinstall      4096 Oct 18  2019 fbo_ggs_Linux_x64_shiphome
[oracle@rac1 ogg]$ cd fbo_ggs_Linux_x64_shiphome/
[oracle@rac1 fbo_ggs_Linux_x64_shiphome]$ cd Disk1/

```
* ogg directory 생성
*
```
[opc@rac1 app]$ id
uid=54322(opc) gid=54323(opc) groups=54323(opc)
[opc@rac1 app]$
[opc@rac1 app]$ pwd
/u01/app
[opc@rac1 app]$ sudo mkdir ogg
[opc@rac1 app]$ chown oracle:oinstall ogg
chown: changing ownership of 'ogg': Operation not permitted
[opc@rac1 app]$ sudo chown oracle:oinstall ogg
[opc@rac1 app]$ ls -la
total 32
drwxr-xr-x  8 root   oinstall 4096 Mar  2 09:25 .
drwxr-xr-x  5 root   oinstall 4096 Sep  2 12:45 ..
drwxr-xr-x  3 root   oinstall 4096 Sep  2 11:43 19.0.0.0
drwxr-xr-x  7 grid   oinstall 4096 Sep  2 12:47 grid
drwxr-xr-x  2 oracle oinstall 4096 Mar  2 09:25 ogg
drwxrwx---  5 grid   oinstall 4096 Feb 28 22:07 oraInventory
drwxr-xr-x  8 oracle oinstall 4096 Sep  2 12:22 oracle
drwxr-xr-x 12 root   root     4096 Jan 29 08:39 oracle.ahf

```

* 응답파일 수정하여 silent 모드로 설치하기 : vi response/oggcore.rsp
  * INSTALL_OPTION=ORA19c
  * SOFTWARE_LOCATION=/u01/app/ogg

```

#-------------------------------------------------------------------------------
# Specify the installation option.
# Specify ORA19c for installing Oracle GoldenGate for Oracle Database 19c or
#         ORA18c for installing Oracle GoldenGate for Oracle Database 18c or
#         ORA12c for installing Oracle GoldenGate for Oracle Database 12c or
#         ORA11g for installing Oracle GoldenGate for Oracle Database 11g
#-------------------------------------------------------------------------------
INSTALL_OPTION=ORA19c

#-------------------------------------------------------------------------------
# Specify a location to install Oracle GoldenGate
#-------------------------------------------------------------------------------
SOFTWARE_LOCATION=/u01/app/ogg
```

* ogg install
  * response file은 절대 경로를 주어야 됨.
```bash
[oracle@rac1 Disk1]$ ./runInstaller -silent -responsefile /home/oracle/ogg/fbo_ggs_Linux_x64_shiphome/Disk1/response/oggcore.rsp
Starting Oracle Universal Installer...

Checking Temp space: must be greater than 120 MB.   Actual 31051 MB    Passed
Checking swap space: must be greater than 150 MB.   Actual 15753 MB    Passed
Preparing to launch Oracle Universal Installer from /tmp/OraInstall2021-03-02_09-28-50AM. Please wait ...
$ [WARNING] [INS-75017] Cluster detected: Unable to determine if the specified software location is shared.
It is recommended to install Oracle GoldenGate software on local storage on each node in the cluster.
   CAUSE: One or more cluster nodes may be unreachable or the specified software location may not be accessible from one or more nodes.
   ACTION: Specify the software location on a shared storage.
You can find the log of this install session at:
 /u01/app/oraInventory/logs/installActions2021-03-02_09-28-50AM.log
Successfully Setup Software.
The installation of Oracle GoldenGate Core was successful.
Please check '/u01/app/oraInventory/logs/silentInstall2021-03-02_09-28-50AM.log' for more details.

[oracle@rac1 Disk1]$

```
* 패치적용

```
$ORACLE_HOME/OPatch/opatch  apply [patch dir]
```

* ogg install
```
[oracle@primary Disk1]$  ./runInstaller -silent -nowait -responseFile /home/oracle/ogg/fbo_ggs_Linux_x64_shiphome/Disk1/response/oggcore.rsp
Starting Oracle Universal Installer...

Checking Temp space: must be greater than 120 MB.   Actual 33913 MB    Passed
Checking swap space: must be greater than 150 MB.   Actual 8131 MB    Passed
Preparing to launch Oracle Universal Installer from /tmp/OraInstall2021-04-06_12-01-37PM. Please wait ...[oracle@primary Disk1]$ You can find the log of this install session at:
 /u01/app/oraInventory/logs/installActions2021-04-06_12-01-37PM.log

[oracle@primary Disk1]$
[oracle@primary Disk1]$ Successfully Setup Software.
The installation of Oracle GoldenGate Core was successful.
Please check '/u01/app/oraInventory/logs/silentInstall2021-04-06_12-01-37PM.log' for more details.

[oracle@primary Disk1]$
[oracle@primary Disk1]$ vi /u01/app/oraInventory/logs/installActions2021-04-06_12-01-37PM.log

[oracle@primary ~]$ vi .bashrc
[oracle@primary ~]$ export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
[oracle@primary ~]$ addpath /u01/app/oracle/ogg
[oracle@primary ~]$ ggsci

Oracle GoldenGate Command Interpreter for Oracle
Version 19.1.0.0.4 OGGCORE_19.1.0.0.0_PLATFORMS_191017.1054_FBO
Linux, x64, 64bit (optimized), Oracle 19c on Oct 17 2019 21:16:29
Operating system character set identified as UTF-8.

Copyright (C) 1995, 2019, Oracle and/or its affiliates. All rights reserved.


GGSCI (primary) 1>

```
