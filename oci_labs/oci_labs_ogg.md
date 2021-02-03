## GoldenGate 19c Microservices Workshop
* https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=585&p210_type=3&session=114317155690746

* OGG Micro Serivce 에서 Deployment GUI 사용을 위한 한경 설정
 * sshd 설정 추가 [탐조문서](https://noooop.tistory.com/entry/ssh-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-GUI-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-X11-forwardingX11-%ED%8F%AC%EC%9B%8C%EB%94%A9)

```bash
sudo vi /etc/ssh/sshd_config

X11Forwarding yes
AddressFamily inet
AllowTcpForwarding yes
X11Forwarding yes
X11DisplayOffset 10
X11UseLocalhost yes

$ sudo  systemctl restart sshd

```
* setEnv.sh

```
# Regular settings.
export TMP=/tmp
export TMPDIR=$TMP

export ORACLE_HOSTNAME=madgu-gg
export ORACLE_UNQNAME=orcl
export ORACLE_BASE=/opt/app/oracle
export ORACLE_HOME=$ORACLE_BASE/product/19.3.0/dbhome_1
export ORACLE_SID=orcl

export PATH=/usr/sbin:/usr/local/bin:$PATH
export PATH=$ORACLE_HOME/bin:$PATH

export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib

export ORA_INVENTORY=/opt/app/oraInventory


# Tomcat settings.
export JAVA_HOME=/opt/java/latest
export CATALINA_HOME=/opt/tomcat/latest
export CATALINA_BASE=/opt/config/instance1

```

* .bash_profile

```
export PATH
. ./setEnv.sh

export OGG_HOME=/opt/app/oracle/product/19.1.0/oggcore_1
export PATH=$PATH:$OGG_HOME/bin
export JAVA_HOME=/home/oracle/jdk1.8.0_221
export PATH=$PATH:$JAVA_HOME/bin
```
* add opc to oinstall group

```
oinstall:x:54321:oracle,opc
```

* XClient (MobiTerm) : Deployment 생성/삭제

``` bash
[opc@ggma-workshop-s01-2021-02-02-134339 Lab2]$ cd $OGG_HOME/bin
[opc@ggma-workshop-s01-2021-02-02-134339 bin]$ ./oggca.sh
```


* Basic Info

```
Database Accounts (sys/system, etc..): Welcome1
GoldenGate Users (c##ggate, ggate): ggate
GoldenGate Admin(oggadmin): Welcome1
```
### Setup of GoldenGate Microservices for Replication
#### STEP 1: Creating Deployments – Atlanta and Boston
* https://152.67.198.125:16000/
* .....................................................
