## OGG
### Basic
* [FY2021 - Training, Immersion and Enablement for GoldenGate](https://confluence.oraclecorp.com/confluence/display/GGProducts/FY2021+-+Training%2C+Immersion+and+Enablement+for+GoldenGate)
* [Competitive Intelligence](https://salescentral.oracle.com/SCPortal/index.html?root=offeringDetails%2F50655)
* [GG Portal](https://database.us.oracle.com/database/f?p=781:2:128983707329089:::2:P2_ID:43721586308052390936481510980055600709)
* [GoldenGate on YouTube!](https://www.youtube.com/channel/UCQZN-1TrusmKNLgJbq5SxNQ)
### 경쟁사 비교
* https://www.scribd.com/document/334170859/Dell-Shareplex-vs-Oracle-GoldenGate-Competitive-Differentiation

### Distribute Transaction (XA)
* [Does Oracle Goldengate Extract Support Distributed Transactions? (Doc ID 1235986.1)](https://support.oracle.com/epmos/main/downloadattachmentprocessor?attachid=1456176.1%3A105&action=inline)
  * page 54.  ``Staring version 11.2.1, Oracle GoldenGate supports XA and PDML distributed transactions in integrated capture mode (but not in classic capture mode). ``
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
