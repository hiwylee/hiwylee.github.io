## OGG

### Blogger
* [DBA Genesis Support](https://www.support.dbagenesis.com/home/categories/oracle-golden-gate)
### How to Step by Step
#### [19c OGG 구성 테스트](https://unioneinc.tistory.com/64#)
*  사전 설정(SRC/TGT)
*  엔진설치(SRC/TGT)
  * 설치 파일 다운로드
    * 18c, 19c의 경우는 oracle.com 에서 다운로드 할 수 있다. 
    * 12c의 경우 suport.oracle.com -> 패치 및 업데이트 -> oracle software delivery cloud에서 검색하여 다운로드
  * 패치 다운로드 
  * rsp 수정
* ogg가 사용 할 유저 생성(SRC/TGT)
* (옵션)ddl문을 동기화 하기 위한 스크립트 실행(SRC/TGT)
* ogg configuration
  * EXTRACT 생성(SRC)
  * Datapump 설정(SRC)
  * Checkpoint table 설정 및 생성(TGT)
  * Replicat 생성(TGT)
  * OGG PROCESS START
  
### Basic
* [FY2021 - Training, Immersion and Enablement for GoldenGate](https://confluence.oraclecorp.com/confluence/display/GGProducts/FY2021+-+Training%2C+Immersion+and+Enablement+for+GoldenGate)
* [Competitive Intelligence](https://salescentral.oracle.com/SCPortal/index.html?root=offeringDetails%2F50655)
* [GG Portal](https://database.us.oracle.com/database/f?p=781:2:128983707329089:::2:P2_ID:43721586308052390936481510980055600709)
* [GoldenGate on YouTube!](https://www.youtube.com/channel/UCQZN-1TrusmKNLgJbq5SxNQ)
### 경쟁사 비교
* https://www.scribd.com/document/334170859/Dell-Shareplex-vs-Oracle-GoldenGate-Competitive-Differentiation
### DownStream Mode
* [Downstream Mode](ogg/ogg_downstream_extract.md)
### Distribute Transaction (XA)
* [Does Oracle Goldengate Extract Support Distributed Transactions? (Doc ID 1235986.1)](https://support.oracle.com/epmos/faces/SearchDocDisplay?_adf.ctrl-state=149gwwhowu_4&_afrLoop=988868350810293)
  *  ``Staring version 11.2.1, Oracle GoldenGate supports XA and PDML distributed transactions in integrated capture mode (but not in classic capture mode). ``
<!--
<pre>
  Required Patches
   – 11.2.0.3.x
       11.2.0.3 Database specific bundle patch for Integrated Extract 11.2.x
      (Doc ID 1411356.1)
       This is a REQUIRED bundled patch for 11.2.0.3 - Integrated Extract
      cannot run without having this OGG/RDBMS bundled patch installed.
       Recommended Patches
   – 11.2.0.4 and 12.1.0.1
       Oracle GoldenGate -- Oracle RDBMS Server Recommended Patches
      (Doc ID 1557031.1)
<pre>
-->
* [GoldenGate Support for XA (Doc ID 1565668.1)](https://support.oracle.com/epmos/faces/SearchDocDisplay?_adf.ctrl-state=149gwwhowu_4&_afrLoop=989464321166242)
  * Page 11. XA transactions on RAC are not supported using classic extract and is supported when using integrated extract.
  * However if you make sure all branches of XA goes to the same instance, then it is supported with classic extract. You can follow the below article to implement it.
```sql
connect / as sysdba
alter system set "_clusterwide_global_transactions"=false scope=spfile;
and restart all the nodes of the cluster.
```
  * This will ensure that ALL branches of XA goes to the same Oracle instance. However if the instance fails the whole XA transaction will roll back.
  * In addition  you also need to Use a singleton service like DTP, so all the connection will go to the same instance. Changing the previous parameter we are reverting to 10.2 behavior. It would be like:
 ```bash
   srvctl add service -d crm -s <service_name> -r RAC01 -a RAC02, RAC03
   ```
   ```sql
   EXECUTE DBMS_SERVICE.MODIFY_SERVICE(service_name=>'<service_name>', DTP=>TRUE);
   ```
   <pre>
  Required Patches
   – 11.2.0.3.x
       11.2.0.3 Database specific bundle patch for Integrated Extract 11.2.x
      (Doc ID 1411356.1)
       This is a REQUIRED bundled patch for 11.2.0.3 - Integrated Extract
      cannot run without having this OGG/RDBMS bundled patch installed.
       Recommended Patches
   – 11.2.0.4 and 12.1.0.1
       Oracle GoldenGate -- Oracle RDBMS Server Recommended Patches
      (Doc ID 1557031.1)
<pre>
