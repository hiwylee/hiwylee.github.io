### 의약품사용정보조회 서비스
* Base URL : 
  * http://apis.data.go.kr/B551182/msupUserInfoService
* 서버키
  * ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D
---  
#### 성분별지역별사용량목록조회(``getCmpnAreaList``)
> 인력 변수 (``전체 필수``)
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * ``성분코드 gnlNmCd``
  * ``보험자구분 insupTp``
  * ``조제처방구분 cpmdPrscTp``
  * ``시도코드 cpmdPrscTp ``
  * ``시군구코드 siguCd``
>  http://apis.data.go.kr/B551182/msupUserInfoService/getCmpnAreaList?ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D&numOfRows=10&pageNo=1&diagYm=201604&gnlNmCd=100701ACH&insupTp=0&cpmdPrscTp=01&sidoCd=110000&sgguCd=110023
```xml
<response>
<header>
<resultCode>00</resultCode>
<resultMsg>NORMAL SERVICE.</resultMsg>
</header>
<body>
<items>
<item>
<diagYm>201604</diagYm>
<gnlNmCd>100701ACH</gnlNmCd>
<gnlNmCdNm>acebrophylline</gnlNmCdNm>
<insupTpCd>4</insupTpCd>
<msupUseAmt>6954711</msupUseAmt>
<sgguCd>110023</sgguCd>
<sgguCdNm>광진구</sgguCdNm>
<sidoCd>110000</sidoCd>
<sidoCdNm>서울</sidoCdNm>
<totUseQty>33152</totUseQty>
</item>
<item>
<diagYm>201604</diagYm>
<gnlNmCd>100701ACH</gnlNmCd>
<gnlNmCdNm>acebrophylline</gnlNmCdNm>
<insupTpCd>5</insupTpCd>
<msupUseAmt>351007</msupUseAmt>
<sgguCd>110023</sgguCd>
<sgguCdNm>광진구</sgguCdNm>
<sidoCd>110000</sidoCd>
<sidoCdNm>서울</sidoCdNm>
<totUseQty>1666</totUseQty>
</item>
</items>
<numOfRows>10</numOfRows>
<pageNo>1</pageNo>
<totalCount>2</totalCount>
</body>
</response>
```
#### 성분별의료기관종별사용량목록조회(``getCmpnClList``) 
> 인력 변수 (``전체 필수``)
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * ``성분코드 gnlNmCd``
  * ``보험자구분 insupTp``
  * ``조제처방구분 cpmdPrscTp``
  * ``시군구코드 siguCd``
  * ``요양기관그룹 clCd ``
>  http://apis.data.go.kr/B551182/msupUserInfoService/getCmpnClList?ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D&numOfRows=10&pageNo=1&diagYm=201604&gnlNmCd=100701ACH&insupTp=0&cpmdPrscTp=01&sidoCd=110000&sgguCd=110023&clCd=01
```xml
<response>
<header>
<resultCode>00</resultCode>
<resultMsg>NORMAL SERVICE.</resultMsg>
</header>
<body>
<items>
<item>
<clCdNm>상급종합병원</clCdNm>
<diagYm>201604</diagYm>
<gnlNmCd>100701ACH</gnlNmCd>
<gnlNmCdNm>acebrophylline</gnlNmCdNm>
<insupTpCd>4</insupTpCd>
<msupUseAmt>122808</msupUseAmt>
<sgguCd>110023</sgguCd>
<sgguCdNm>광진구</sgguCdNm>
<sidoCd>110000</sidoCd>
<sidoCdNm>서울</sidoCdNm>
<totUseQty>731</totUseQty>
</item>
</items>
<numOfRows>10</numOfRows>
<pageNo>1</pageNo>
<totalCount>1</totalCount>
</body>
</response>
```
#### 성분별상병별사용량목록조회  (``getCmpnSickList``) 
> 인력 변수  (``전체 필수``)
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * ``성분코드 gnlNmCd``
  * ``보험자구분 insupTp``
  * ``조제처방구분 cpmdPrscTp``

  >  http://apis.data.go.kr/B551182/msupUserInfoService/getCmpnSickList?ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D&numOfRows=10&pageNo=1&diagYm=201604&gnlNmCd=100701ACH&insupTp=0&cpmdPrscTp=01
```xml

<OpenAPI_ServiceResponse>
<cmmMsgHeader>
<errMsg>SERVICE ERROR</errMsg>
<returnAuthMsg>SERVICE_ACCESS_DENIED_ERROR</returnAuthMsg>
<returnReasonCode>20</returnReasonCode>
</cmmMsgHeader>
</OpenAPI_ServiceResponse>
  ```
####  의약품코드정보목록조회(getMsupCdInfoList  > msupCdTp=4인 경우)"
> 인력 변수
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * 성분코드 gnlNmCd
  * 보험자구분 insupTp
  * 조제처방구분 cpmdPrscTp
>  http://apis.data.go.kr/B551182/msupUserInfoService/getMsupCdInfoList?ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D&numOfRows=10&pageNo=1&diagYm=201604&gnlNmCd=100701ACH&insupTp=0&cpmdPrscTp=01&sidoCd=110000&sgguCd=110023&ciCd=01
---  

### 약가기준정보조회서비스
* Base URL : 
  * http://apis.data.go.kr/B551182/dgamtCrtInfoService
* 서버키
  * ServiceKey=Fm4e4k6u%2Faw6gmlRwAZNteSJKphfGBeXcs1UQQfnN2mnyOVV9tO%2BwtjC9bnBcNhllDDjRWmcYkYixHUWDZfyyw%3D%3D

#### 약가기준정보조회서비스(getDgamtList)"
  * 서비스 인증키 ServiceKey : (1)
  * 한페이지결과수 numOfRows   (1) 
  * 페이지 번호 pageNo         (1) 
  * 약품코드 mdsCd             (0..1) 
  * 품목명  itmNm              (0..1) 
  * 제업체명 mnfEntpNm         (0..1) 
  * ``주의 : 약품코드, 품목명, 제업체명 셋 중하나는 필수``
> Sample URL  
>  http://apis.data.go.kr/B551182/dgamtCrtrInfoService/getDgamtList?ServiceKey=Fm4e4k6u%2Faw6gmlRwAZNteSJKphfGBeXcs1UQQfnN2mnyOVV9tO%2BwtjC9bnBcNhllDDjRWmcYkYixHUWDZfyyw%3D%3D&numOfRows=10&pageNo=1&mdsCd=G03900131
```xml
<response>
<header>
<resultCode>00</resultCode>
<resultMsg>NORMAL SERVICE.</resultMsg>
</header>
<body>
<items>
<item>
<adtStaDd>20050401</adtStaDd>
<chgAfMdsCd>G09900011</chgAfMdsCd>
<gnlNmCd>250401ATB</gnlNmCd>
<injcPthNm>내복</injcPthNm>
<itmNm>레스피렌정</itmNm>
<mdsCd>G03900131</mdsCd>
<meftDivNo>222</meftDivNo>
<mnfEntpNm>건일제약</mnfEntpNm>
<mxCprc>0</mxCprc>
<nomNm>1</nomNm>
<optCpmdImplTpNm>향정신성의약품</optCpmdImplTpNm>
<payTpNm>삭제</payTpNm>
<sbstPsblTpNm>동등+대조(동등)</sbstPsblTpNm>
<spcGnlTpNm>전문</spcGnlTpNm>
<unit>정</unit>
</item>
</items>
<numOfRows>10</numOfRows>
<pageNo>1</pageNo>
<totalCount>1</totalCount>
</body>
</response>
```
### 의약품 제품 허가정보 서비스
#### 의약품 제품 허가정보 상세 서비스
* 품목, 주성분, 제조원, 포장단위, 저장방법, 성상등의 품목정보와 허가일자, 허가번호 등의 허가정보 등의 허가받은 의약제품정보를 상세정보로 제공
* 활용승인 절차 개발단계 : 허용 / 운영단계 : 허용
* 신청가능 트래픽 1000000 / 운영계정은 활용사례 등록시 신청하면 트래픽 증가 가능
* 요청주소 http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService/getMdcinPrductItem
* 서비스URL http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService
#### 의약품 제품 허가정보 목록 서비스
* 품목, 주성분, 제조원, 포장단위, 저장방법, 성상등의 품목정보와 허가일자, 허가번호 등의 허가정보 등의 허가받은 의약제품정보를 목록으로 제공
* 활용승인 절차 개발단계 : 허용 / 운영단계 : 허용
* 신청가능 트래픽 1000000 / 운영계정은 활용사례 등록시 신청하면 트래픽 증가 가능
* 요청주소 http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService/getMdcinPrductList
* 서비스URL http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService

#### 의약품 제품 주성분 상세 조회  서비스
품목, 주성분, 제조원, 포장단위, 저장방법, 성상등의 품목정보와 허가일자, 허가번호 등의 허가정보 등의 허가받은 의약제품 주성분 정보를 목록으로 제공
활용승인 절차 개발단계 : 허용 / 운영단계 : 허용
신청가능 트래픽 1000000 / 운영계정은 활용사례 등록시 신청하면 트래픽 증가 가능
요청주소 http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService/getMdcinPrductIrdntItem
서비스URL http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService
