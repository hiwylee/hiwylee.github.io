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
* Deployment 생성/삭제

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
