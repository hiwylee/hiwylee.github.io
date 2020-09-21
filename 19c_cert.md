### 19c Cert

* [Certification Information for Oracle Database on IBM AIX on Power systems (Doc ID 1307544.1](]
#### Oracle RAC Technologies Certification Matrix for UNIX Platforms
* https://www.oracle.com/database/technologies/tech-generic-unix-new.html

#### 1. Oracle ASM 과 EMC SRDF Certified 정보 (SRDF Metro 포함)
* 2012 년 certi 된 것으로 보이는데 내부 사이트에서 cross checking 해 보겠습니다.
  * http://www.thestoragechap.co.uk/tscblog/2012/05/17/vplex-metro-and-oracle-rac-its-certified/
  * https://corporate.delltechnologies.com/en-us/newsroom/announcements/2012/05/20120517-04.htm
#### 2. E980, PEP, LPAR, ADG < 3노드 Primary[61/61/31] / 3노드 Standby[10/10/10] > 에 대한 금융권 구축 사례
#### 3. E980 에서 1TB 메모리 중 500GB 를 SGA(주로 Buffer Cache)에 할당 한 상태에서 DB 인스턴스 중단 시 전체 DB Freeze (Reconfiguration) 예상 시간 (40G Interconnect 기준)
------------------------------------------------------------------------------------------------------------------------------------
#### 4. IBM 으로 19c RAC 구성 시 PowerHA 적용/미적용 권고 (Best Practice)
##### 5. IBM 으로 19c RAC 구성 시 GPFS(Spectrum Scale) 적용/미적용 권고 (Best Practice) 및 ACFS 가 Oracle 의 Best Practice 여부
  * [IBM Spectrum Scale 5.0 is certified with Oracle Database 19c and Oracle RAC on AIX 7.1 and AIX 7.2](http://www-03.ibm.com/support/techdocs/atsmastr.nsf/WebIndex/FLASH10907)
  * [Oracle Real Application Clusters 19.0.0.0.0 is certified with IBM Spectrum Scale 5.0 on IBM AIX on POWER Systems (64-bit) 7.2](https://mosemp.us.oracle.com/epmos/faces/CertifyDrillDownNDetails?_adf.ctrl-state=16eowssuij_843&searchCtx=st%255EPRODUCT%257Cpa%255Epi%255E563_Oracle%2BReal%2BApplication%2BClusters%257Evi%255E880937%257Epln%255EAny%257E%257Cpb%255Epi%255E958_IBM%2BSpectrum%2BScale%257Epln%255EAny%257E%257C&drillDownCtx=st%255EANY%257Cpb%255Epi%255E958_IBM%2BSpectrum%2BScale%257E%257C&detailsCtx=st%255EANY%257Cpa%255Evi%255E880937%257Eplvi%255E556537%257E%257Cpb%255Evi%255E880096%257E%257C&_afrLoop=162381687824384)
    * Notes 
       * Oracle Real Application Clusters 19.0.0.0.0 with IBM Spectrum Scale 5.0
       * Minimum update level: TL5 SP4
       * Minimum RU level: 19.4
  * [Acceptable uses of the IBM Spectrum Scale (GPFS) file system include](https://mosemp.us.oracle.com/epmos/faces/SearchDocDisplay?_adf.ctrl-state=16eowssuij_843&_afrLoop=162746749387453#PURPOSE)
     * Oracle Database - Enterprise Edition - Version 11.2.0.4 to 12.2.0.1 [Release 11.2 to 12.2]
     * 1. Shared ORACLE_HOME directory for Oracle database installation
     * 2. Shared database files for tablespaces and other general database object containers
     * 3. Oracle Clusterware registry and membership files (i.e. Oracle Cluster Registry (OCR) and Vote Disks)*
       *  For Oracle Database 12cR2, Oracle only supports ASM/NFS for Grid OCR and Vote files. The 12.2 upgrade requires that these files are migrated to ASM. IBM Spectrum Scale will still be used for database files in this release.
------------------------------------------------------------------------------------------------------------------------------------

#### 5. IBM Spectrum Scale (GPFS)
<pre>
* For Oracle Database 12cR2, Oracle only supports ASM/NFS for Grid OCR and Vote files. 
  The 12.2 upgrade requires that these files are migrated to ASM. IBM Spectrum Scale will still be used for database files in this release.

SCOPE
Oracle Database Real Application Cluster - Enterprise Edition - Version 11.2.0.4 to 12.2.0.1
IBM Spectrum Scale - Version 4.1 and 4.2
IBM AIX Operating System -- Version 7.1 and 7.2

IBM PowerHA SystemMirror 7.1 with IBM AIX on POWER Systems (64-bit) 7.2
Internal Notes: (Not visible to customers)
</pre>
