# Exadata Study Guide
* [OSAN Home](https://login.oracle.com/oamfed/idp/initiatesso?providerid=https://sso.netexam.com/sp)
## Exadata Value Proposition
## 문제 구간 분석 관련
* [Tool for Gathering I/O Resource Manager Metrics: metric_iorm.pl (Doc ID 1337265.1)](https://mosemp.us.oracle.com/epmos/faces/DocContentDisplay?_afrLoop=284124481059217&id=1337265.1&_afrWindowMode=0&_adf.ctrl-state=rqq1xmzzr_273)
* 문제를 확인할 수 있도록 특정 구간을 정해서 다음과 같이 수행
  
  ```bash
  ./metric_iorm.pl "where collectionTime > '2020-09-23T16:00:00+09:00' and collectionTime < '2020-09-23T17:00:00+09:00'" <<-- 시간은 알맞게 변경!!
  ```
  * 참고: ++ Tool for Gathering I/O Resource Manager Metrics: metric_iorm.pl (Doc ID 1337265.1)
* 모든 cell 노드에서 각각 sundiag 데이터를 수집.
  * SRDC - EEST Sundiag (Doc ID 1683842.1)
* IB 스위치에 대해서 다음을 수집
  * ++ SRDC - ES Infiniband Switch (Doc ID 1683903.1)
## command & config files
* cellcli
* dbmcli
* exacli / exadcli
* dcli
* ibhosts
* ibswitches
* group
  * /etc/dbs_group
  * /etc/cell_group
  * /etc/ib_group
  * /etc/all_group
* cell init params
  * /etc/oracle/cell/network-config/cellinit.ora
  * /etc/oracle/cell/network-config/cellip.ora
* dcli
```bash
dclid -g /etc/all_group -l root -k -s '-o StrickHostKeyChecking=no'
dclid -g /etc/ib_group -l root -k -s '-o StrickHostKeyChecking=no'
dclid -g /etc/all_group -l root date

```
* /etc/sysctl.config
  * Total Sga Max Size 
    * DB Usable MEM = 0.8 * Total Mem_Gib
    * Sum of Total SGA_MAX_SIZE = round(0.8 * DB Usable MEM) 
    * vm.nr_higgepages => ``(Sum of Total SGA_MAX_SIZE + 2) * 512``
    * grubby --args="transparent_hugepage=never" --update-kernel /boot/vmlinuz-3.10.-862.el7.x86_64
    * alter system set use_large_pages=only scope=spfile
  * PGA 
    * PAG_AGGREGATE_TARGET
    * PGA_AGGREGATE_LIMIT
    * Sum of Total PGA_AGGREGATE_LIMIT = round(0.2 * DB Usable MEM)
## install
* Oracle Exadata Deployment Assistant (OEDA)
* install.sh -cf client-mycluster.xml -s -l # Preparing the installation
* install.sh -cf client-mycluster.xml -s 2  # Verify ISO
* Step 3: User Creation
* Step 4:  Cell Connectivity
* Step 5:  Verify Infiniband
* Step 6:  Cell I/O Calibrate
* Step 7: Cell disks creation
* Step 8: Grid disks creation
* Step 9: GI installation
* Step 10: Initialize Cluster s/w - root.sh
* Step 11: Database Installation
* Step 12: Relink database with RDS 
* Step 13: Create ASM diskgroup
* Step 14: Database creation
* Step 15: Security fixes
* Step 16: Install Exachk
* Step 17: Install Summary
* Step 18: Rescure the machine

## Exadata Basic
* [Exadata Database Machine: All about X8M](https://www.youtube.com/watch?v=7HKHKExdR5I)
* [Demystify the Exadata installation by Fred Denis](https://www.youtube.com/watch?v=hoS5w_xBsf4)
* [Migrate Database To Exadata Using RMAN Duplicate](https://www.youtube.com/watch?v=UJH06IVPHE4)
* [Oracle Exadata System Software 19.1](https://www.youtube.com/watch?v=-5vCFhJ2wFY)
* [Oracle Exadata System Software 20.1](https://www.youtube.com/watch?v=Uf2ee_7C4Yo&t=3s)
### Exadata Basic Training
* DataSheet
  * [Exadata X8-2 Datasheet](https://www.oracle.com/technetwork/database/exadata/exadata-x8-2-ds-5444350.pdf)
  * [Exadata X8m-2 Datasheet](https://www.oracle.com/a/ocom/docs/engineered-systems/exadata/exadata-x8m-2-ds.pdf)
* [Cool Stuff for DBAs in Oracle Database 19c](https://www.youtube.com/watch?v=EVPNyL2vAVI)
* [Oracle Exadata X8 Overview](https://www.youtube.com/watch?v=szlfbBXoXYs)
* [All In on Exadata](https://www.youtube.com/watch?v=njymzhD0oHE)
* [Oracle Exadata X6: Technical Deep Dive - Architecture and Internals](https://www.youtube.com/watch?v=8UmNxrohsTQ&list=PLEVmh4UjbWxNRth74cbl6DZwa9m8X3UvZ)
* [Exadata Part 1](https://www.youtube.com/watch?v=CfNLB65w8Fc&list=PLEVmh4UjbWxNRth74cbl6DZwa9m8X3UvZ&index=2)
* [Exadata Part 2](https://www.youtube.com/watch?v=301EPKUdPyY&list=PLEVmh4UjbWxNRth74cbl6DZwa9m8X3UvZ&index=3)
* [Exadata Part 3](https://i.ytimg.com/vi/p-tM0MDmbqg/hqdefault.jpg?sqp=-oaymwEYCKgBEF5IVfKriqkDCwgBFQAAiEIYAXAB&rs=AOn4CLDWn39gKG7Hz7dao1x2vRyUFOlJzA)
## Exadata Spec
### Spec 비교
* [ Exadata X8-2 ]
  * ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fkxl0B%2Fbtqv15RP0RH%2FqOdKfAvtJ7nvJkKyZDMTQk%2Fimg.png)
* [ Exadata X7-2 ]
  * ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbm2KRs%2Fbtqv4PNQyBc%2FGXikGCbQVKzVR11j3sdYRK%2Fimg.png)
## Exadata Advanced
* Technical Deep Dive
* Ideal Database HW
* Smart System SW : OLTP / DW / Consolidation 측면 (https://www.youtube.com/watch?v=szlfbBXoXYs)
  * Offload SQL to Storage
  * InfiniBand Fabric
  * Smart Flash Cache, Log
  * Storage Indexes
  * Columner Flash Cache
  * Hybrid Columnar Compression
  * I/O Resouce Management
  * In-Memory Fault Tolerance
  * Exafusion Direct-to-Wire Protocol
  * Direct-to-Wire Protocol
* Automatic Management
