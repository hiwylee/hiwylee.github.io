### 의약품사용정보조회 서비스
### 
* Base URL : 
  * http://apis.data.go.kr/B551182/msupUserInfoService
* 서버키
  * ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D
* 성분별지역별사용량목록조회(``getCmpnAreaList``)
> 인력 변수
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * 성분코드 gnlNmCd
  * 보험자구분 insupTp
  * 조제처방구분 cpmdPrscTp
  * 시도코드 cpmdPrscTp 
  * 시군구코드 siguCd
>  http://apis.data.go.kr/B551182/msupUserInfoService/getCmpnAreaList?ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D&numOfRows=10&pageNo=1&diagYm=201604&gnlNmCd=100701ACH&insupTp=0&cpmdPrscTp=01&sidoCd=110000&sgguCd=110023
  
* 성분별의료기관종별사용량목록조회(``getCmpnClList``) 
> 인력 변수
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * 성분코드 gnlNmCd
  * 보험자구분 insupTp
  * 조제처방구분 cpmdPrscTp
  * 시군구코드 siguCd
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
* 성분별상병별사용량목록조회    (``getCmpnSickList``) 
> 인력 변수
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * 성분코드 gnlNmCd
  * 보험자구분 insupTp
  * 조제처방구분 cpmdPrscTp
  * 시도코드 cpmdPrscTp 
  * 시군구코드 siguCd
  * ``요양기관그룹 clCd ``
  >  http://apis.data.go.kr/B551182/msupUserInfoService/getCmpnSickList?ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D&numOfRows=10&pageNo=1&diagYm=201604&gnlNmCd=100701ACH&insupTp=0&cpmdPrscTp=01
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
* 의약품코드정보목록조회(getMsupCdInfoList  > msupCdTp=4인 경우)"
> 인력 변수
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * 성분코드 gnlNmCd
  * 보험자구분 insupTp
  * 조제처방구분 cpmdPrscTp
>  http://apis.data.go.kr/B551182/msupUserInfoService/getMsupCdInfoList?ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D&numOfRows=10&pageNo=1&diagYm=201604&gnlNmCd=100701ACH&insupTp=0&cpmdPrscTp=01&sidoCd=110000&sgguCd=110023&ciCd=01
