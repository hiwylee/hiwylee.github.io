
## Oracle Cloud Infrastructure: Reserved Public IP Addresses
### 유튜브
* [create  reserve public ip](https://www.youtube.com/watch?v=9_7KaGGVmUA)

### 문서
* [Reserved Public IPs: Using the Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#To4)

### 생성 및 적용 요약
* 순서
  * 공용 ip 예약
    * 경로: Networking -> IP Management -> Public IPs
  * 인스턴스 생성
  * Private VNIC ip address -> No Public IP 설정 저장 (``기존 ip 를 해제해야 예약된 ip 사용 가능``)
  * Private VNIC ip address -> Reserved public IP 설정

```
1) create compartment >
2) Select compartment
3) create Reserved public ip
   Path : Networking->  IP Management -> Public IPs
   - Create 4 Reserve public IP Address 

4) Create instance
   ....
5) goto Compute -> Instances-> Instance details   
   Select Attached VNICs  
   Select Primary VNIC
     -> SELECT [IPv4 Addresses]
	    ... EDIT
		1) Select No public IP : ip를 해제해야 reserve ip 를 사용할 수 있음.
		 click update
	-> SELECT [IPv4 Addresses] again
        choose :  Reserved public IP 
		         -> Select Existing Reserved IP Address
				 -> pick a ip 
```		
   
