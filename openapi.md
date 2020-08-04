### 의약품사용정보조회 서비스
### 
* Base URL : 
  * http://apis.data.go.kr/B551182/msupUserInfoService
* 서버키
  * ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D
* 성분별지역별사용량목록조회(getCmpnAreaList)
> 인력 변수
  진료년월
  성분코드 gnlNmCd
  보험자구분 insupTp
  조제처방구분 cpmdPrscTp
  시도코드 cpmdPrscTp 
  시군구코드 110023
* 성분별의료기관종별사용량목록조회(getCmpnClList) 
> 인력 변수
  진료년월
  성분코드 gnlNmCd
  보험자구분 insupTp
  조제처방구분 cpmdPrscTp
  시도코드 cpmdPrscTp 
  시군구코드 110023
>  http://apis.data.go.kr/B551182/msupUserInfoService/getCmpnAreaList?ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D&numOfRows=10&pageNo=1&diagYm=201604&gnlNmCd=100701ACH&insupTp=0&cpmdPrscTp=01&sidoCd=110000&sgguCd=110023&ciCd=01

* 성분별상병별사용량목록조회    (getCmpnSickList) 
> 인력 변수
  진료년월
  성분코드 gnlNmCd
  보험자구분 insupTp
  조제처방구분 cpmdPrscTp
  시도코드 cpmdPrscTp 
  시군구코드 110023
* 의약품코드정보목록조회(getMsupCdInfoList  > msupCdTp=4인 경우)"
> 인력 변수
  진료년월
  성분코드 gnlNmCd
  보험자구분 insupTp
  조제처방구분 cpmdPrscTp
  시도코드 cpmdPrscTp 
  시군구코드 110023

