## downstream integrated capture

### Basic 
* [** Best Practices from Oracle Development's A‑Team**](https://www.ateam-oracle.com/oracle-goldengate-best-practice-goldengate-downstream-extract-with-oracle-data-guard)
* [Configuring Oracle GoldenGate OGG 11gR2 downstream integrated capture](https://gjilevski.com/2012/10/31/configuring-oracle-goldengate-ogg-11gr2-downstream-integrated-capture/)

* [Extracting Data in Oracle GoldenGate Integrated Capture Mode](https://www.oracle.com/technetwork/database/availability/8398-goldengate-integrated-capture-1888658.pdf)
* https://www.oracle-scn.com/oracle-goldengate-integrated-capture/

### Important MOS Notes
* Specific patches for Integrated Capture: 1411356.1
* Integrated Capture health check script 1448324.1
* OGG Best Practices: Configuring Downstream Integrated Capture 1485620.1
* Performance Tuning for OGG [1488668.1](https://mosemp.us.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=540428795909541&id=1488668.1&_adf.ctrl-state=nrjz6fd9l_229)

### 테스트 시나리오 
* 환경
  * source : 2 node rac db 11.2.0.2
  * mining : single db 12.2.0.1
  * target : 2 node RAC
 * 테스트 내용
   * Realtime downstream
   * standby redo log shipping delay
   * online redo log shipping
   * extract perf
   * apply perf
