# Exadata Study Guide
* [OSAN Home](https://login.oracle.com/oamfed/idp/initiatesso?providerid=https://sso.netexam.com/sp)
## Exadata Value Proposition
## command 
* ibhosts
* ibswitches
* group
  * /etc/dbs_group
  * /etc/cell_group
  * /etc/ib_group
  * /etc/all_group
* dcli
```bash
dclid -g /etc/all_group -l root -k -s '-o StrickHostKeyChecking=no'
dclid -g /etc/ib_group -l root -k -s '-o StrickHostKeyChecking=no'
dclid -g /etc/all_group -l root date
```
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
