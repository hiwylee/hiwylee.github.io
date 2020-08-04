# Open API (data.go.kr)
## HIRA
### 의약품사용정보조회 서비스
* Base URL : 
  * http://apis.data.go.kr/B551182/msupUserInfoService
* 서버키
  * ServiceKey=Ilwl21IL5bldm28%2FOjDimlevdf4vn3XKD8z5N6LireVUUjGTicqOl5oFqKYexzrcnUSysJATziLqvgQ2KIpwNA%3D%3D
---  
#### 성분별지역별사용량목록조회(``getCmpnAreaList``)
- URL : http://apis.data.go.kr/B551182/msupUserInfoService/getCmpnAreaList
> 인력 변수 (``전체 필수``)
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * ``성분코드 gnlNmCd`` - getMsupCdInfoList  > msupCdTp=4인 경우
  * ``보험자구분 insupTp`` - 0:전체, 4: 건강보험, 5: 의료급여, 7: 보훈
  * ``조제처방구분 cpmdPrscTp`` -  01:조제기준 , 02: 처방기준
  * ``시도코드 sidoCd ``
  * ``시군구코드 siguCd`` - 228
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
- URL : http://apis.data.go.kr/B551182/msupUserInfoService/getCmpnClList
> 인력 변수 (``전체 필수``)
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * ``성분코드 gnlNmCd`` - getMsupCdInfoList  > msupCdTp=4인 경우
  * ``보험자구분 insupTp`` - 0:전체, 4: 건강보험, 5: 의료급여, 7: 보훈
  * ``조제처방구분 cpmdPrscTp`` -  01:조제기준 , 02: 처방기준
  * ``시군구코드 siguCd`` - 228개
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
#### 성분별상병별사용량목록조회  (``getCmpnSickList``)  : ``에러``
- URL : http://apis.data.go.kr/B551182/msupUserInfoService/getCmpnSickList
> 인력 변수  (``전체 필수``)
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * ``성분코드 gnlNmCd`` - getMsupCdInfoList  > msupCdTp=4인 경우
  * ``보험자구분 insupTp`` - 0:전체, 4: 건강보험, 5: 의료급여, 7: 보훈
  * ``조제처방구분 cpmdPrscTp`` -  01:조제기준 , 02: 처방기준

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
####  의약품코드정보목록조회(getMsupCdInfoList  > msupCdTp=4인 경우)"  ``없음``
- URL : http://apis.data.go.kr/B551182/msupUserInfoService/getMsupCdInfoList
> 인력 변수
  * 서비스 인증키 ServiceKey
  * 한페이지결과수 numOfRows
  * 페이지 번호 pageNo
  * 진료년월 diagYm
  * ``성분코드 gnlNmCd`` - getMsupCdInfoList  > msupCdTp=4인 경우
  * ``보험자구분 insupTp`` - 0:전체, 4: 건강보험, 5: 의료급여, 7: 보훈
  * ``조제처방구분 cpmdPrscTp`` -  01:조제기준 , 02: 처방기준
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
- Sample URL  
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
## 식약처
###  의약품 특허정보(통합) 서비스
#### 의약품 특허정보 조회
* 의약품 성분명, 제품명, 허가업체 등 의약품 특허 정보를 목록으로 제공
* 활용승인 절차 개발단계 : 허용 / 운영단계 : 허용
* 신청가능 트래픽 1000000 / 운영계정은 활용사례 등록시 신청하면 트래픽 증가 가능
* 요청주소 http://apis.data.go.kr/1470000/MdcinPatentInfoService/getMdcinPatentInfoList
* 서비스URL http://apis.data.go.kr/1470000/MdcinPatentInfoService
* 서버키 : Fm4e4k6u%2Faw6gmlRwAZNteSJKphfGBeXcs1UQQfnN2mnyOVV9tO%2BwtjC9bnBcNhllDDjRWmcYkYixHUWDZfyyw%3D%3D
? 입력변수 (옵션)
  * 성분명(영)      ingr_eng_name
  * 제품명(영)      eng_name
  * 제품명(한)      kor_name
  * 페이지 번호      pageNo
  * 한 페이지 결과수   numOfRows   
> http://apis.data.go.kr/1470000/MdcinPatentInfoService/getMdcinPatentInfoList?serviceKey=Fm4e4k6u%2Faw6gmlRwAZNteSJKphfGBeXcs1UQQfnN2mnyOVV9tO%2BwtjC9bnBcNhllDDjRWmcYkYixHUWDZfyyw%3D%3D&numOfRows=3&pageNo=1

```xml
<response>
	<header>
		<resultCode>00</resultCode>
		<resultMsg>NORMAL SERVICE.</resultMsg>
	</header>
	<body>
	<numOfRows>2</numOfRows>
	<pageNo>1</pageNo>
	<totalCount>77552</totalCount>
	<items>
		<item>
			<INGR_ENG_NAME>Brigatinib</INGR_ENG_NAME>
			<INGR_KOR_NAME>브리가티닙</INGR_KOR_NAME>
			<ITEM_NAME_ENG>Alunbrig</ITEM_NAME_ENG>
			<ITEM_NAME_KOR>알룬브릭정180밀리그램(브리가티닙)</ITEM_NAME_KOR>
			<SELLING_CORP>한국다케다제약(주)</SELLING_CORP>
			<DOSAGE_FORM>필름코팅정</DOSAGE_FORM>
			<STRENGTH>180.0밀리그램</STRENGTH>
			<GROUPING_NO>421</GROUPING_NO>
			<PMS_EXP_DATE>-</PMS_EXP_DATE>
			<KOR_SUIT_YN/>
			<ITEM_SEQ>201804848</ITEM_SEQ>
			<PAGE_GB_NM>제품특허</PAGE_GB_NM>
			<PATENT_GB_CODE>기타</PATENT_GB_CODE>
			<DOMESTIC_INVN_NM>EGFR 단백질분해 표적화 키메라 분자 및 관련 사용 방법</DOMESTIC_INVN_NM>
			<PATENTEE/>
			<DOMESTIC_PATENT_NO/>
			<DOMESTIC_PATENT_STATUS>출원</DOMESTIC_PATENT_STATUS>
			<DOMESTIC_END_DATE/>
		</item>
		<item>
			<INGR_ENG_NAME>Brigatinib</INGR_ENG_NAME>
			<INGR_KOR_NAME>브리가티닙</INGR_KOR_NAME>
			<ITEM_NAME_ENG>Alunbrig</ITEM_NAME_ENG>
			<ITEM_NAME_KOR>알룬브릭정90밀리그램(브리가티닙)</ITEM_NAME_KOR>
			<SELLING_CORP>한국다케다제약(주)</SELLING_CORP>
			<DOSAGE_FORM/>
			<STRENGTH>90.0밀리그램</STRENGTH>
			<GROUPING_NO>421</GROUPING_NO>
			<PMS_EXP_DATE>-</PMS_EXP_DATE>
			<KOR_SUIT_YN/>
			<ITEM_SEQ>201804847</ITEM_SEQ>
			<PAGE_GB_NM>제품특허</PAGE_GB_NM>
			<PATENT_GB_CODE>기타</PATENT_GB_CODE>
			<DOMESTIC_INVN_NM>EGFR 단백질분해 표적화 키메라 분자 및 관련 사용 방법</DOMESTIC_INVN_NM>
			<PATENTEE/>
			<DOMESTIC_PATENT_NO/>
			<DOMESTIC_PATENT_STATUS>출원</DOMESTIC_PATENT_STATUS>
			<DOMESTIC_END_DATE/>
		</item>
	</items>
	</body>
</response>
```
### 의약품 제품 허가정보 서비스
* serviceKey=Fm4e4k6u%2Faw6gmlRwAZNteSJKphfGBeXcs1UQQfnN2mnyOVV9tO%2BwtjC9bnBcNhllDDjRWmcYkYixHUWDZfyyw%3D%3D
#### 의약품 제품 허가정보 상세 서비스 (getMdcinPrductItem)  
* 품목, 주성분, 제조원, 포장단위, 저장방법, 성상등의 품목정보와 허가일자, 허가번호 등의 허가정보 등의 허가받은 의약제품정보를 상세정보로 제공
* 활용승인 절차 개발단계 : 허용 / 운영단계 : 허용
* 신청가능 트래픽 1000000 / 운영계정은 활용사례 등록시 신청하면 트래픽 증가 가능
* 요청주소 http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService/getMdcinPrductItem 
> 입력변수
  * 품목명           item_name
  * 업체명           entp_name
  * 허가일자          item_permit_date
  * 업체허가번호        entp_no 
  * 페이지 번호        pageNo 
  * 한 페이지 결과수    numOfRows
  * 표준코드          bar_code
  * 품목기준코드        item_seq 
  * 변경일자시작일      start_change_date
  * 변경일자종료일      end_change_date
> http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService/getMdcinPrductItem?serviceKey=Fm4e4k6u%2Faw6gmlRwAZNteSJKphfGBeXcs1UQQfnN2mnyOVV9tO%2BwtjC9bnBcNhllDDjRWmcYkYixHUWDZfyyw%3D%3D&pageNo=1&numOfRows=1&
* ``결과가 너무 복잡하여 구조화 하기 어려움``
```xml
<response>
	<header>
		<resultCode>00</resultCode>
		<resultMsg>NORMAL SERVICE.</resultMsg>
	</header>
	<body>
		<numOfRows>1</numOfRows>
		<pageNo>1</pageNo>
		<totalCount>52353</totalCount>
		<items>
			<item>
				<ITEM_SEQ>195500002</ITEM_SEQ>
                ...
				<GBN_NAME>용법용량변경, 2015-12-17/효능효과변경, 2015-12-17/사용상주의사항변경(부작용포함), 2015-12-17/용법용량변경, 1995-01-01/효능효과변경, 1995-01-01/사용상주의사항변경(부작용포함), 1995-01-01</GBN_NAME>
				<TOTAL_CONTENT>1정 중 80밀리그램</TOTAL_CONTENT>
				<EE_DOC_DATA>
				<DOC title="효능효과" type="EE">
					<SECTION title="">
						<ARTICLE title="1. 다음 질환에서의 기침 : 기관지천식, 감기, 급•만성기관지염, 상기도염"/>
						<ARTICLE title="2. 비점막의 충혈·종창"/>
					</SECTION>
				</DOC>
				</EE_DOC_DATA>
				<UD_DOC_DATA>
				...
				</UD_DOC_DATA>
				<NB_DOC_DATA>
				...
				</NB_DOC_DATA>
				<PN_DOC_DATA/>
				<MAIN_ITEM_INGR>염산에페드린</MAIN_ITEM_INGR>
				<INGR_NAME>유당/옥수수전분/탈크/스테아린산마그네슘</INGR_NAME>
			</item>
		</items>
	</body>
</response>
```
#### 의약품 제품 허가정보 목록 서비스 (getMdcinPrductList)   
* 품목, 주성분, 제조원, 포장단위, 저장방법, 성상등의 품목정보와 허가일자, 허가번호 등의 허가정보 등의 허가받은 의약제품정보를 목록으로 제공
* 활용승인 절차 개발단계 : 허용 / 운영단계 : 허용
* 신청가능 트래픽 1000000 / 운영계정은 활용사례 등록시 신청하면 트래픽 증가 가능
* 요청주소 http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService/getMdcinPrductList?serviceKey=Fm4e4k6u%2Faw6gmlRwAZNteSJKphfGBeXcs1UQQfnN2mnyOVV9tO%2BwtjC9bnBcNhllDDjRWmcYkYixHUWDZfyyw%3D%3D&numOfRows=3&pageNo=1
> 입력변수 (전체 옵션)
  * 제품명             item_name
  * 업체명             entp_name
  * 업종               induty 
  * 품목일련번호            prdlst_Stdr_code 
  * 전문/일반구분코드_M58   spclty_pblc 
  * 품목허가번호            prduct_prmisn_no 
  * 페이지 번호             pageNo
  * 한 페이지 결과수       numOfRows 
* 서비스URL http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService
> 
```xml
<response>
	<header>
		<resultCode>00</resultCode>
		<resultMsg>NORMAL SERVICE.</resultMsg>
	</header>
	<body>
		<numOfRows>3</numOfRows>
		<pageNo>1</pageNo>
		<totalCount>53656</totalCount>
		<items>
			<item>
				<ITEM_SEQ>195500002</ITEM_SEQ>
				<ITEM_NAME>종근당염산에페드린정</ITEM_NAME>
				<ENTP_NAME>(주)종근당</ENTP_NAME>
				<ITEM_PERMIT_DATE>19550117</ITEM_PERMIT_DATE>
				<INDUTY>의약품</INDUTY>
				<PRDLST_STDR_CODE>195500002</PRDLST_STDR_CODE>
				<SPCLTY_PBLC>전문의약품</SPCLTY_PBLC>
				<PRDUCT_TYPE/>
				<PRDUCT_PRMISN_NO>7</PRDUCT_PRMISN_NO>
				<ITEM_INGR_NAME>염산에페드린</ITEM_INGR_NAME>
				<ITEM_INGR_CNT>1</ITEM_INGR_CNT>
				<PERMIT_KIND_CODE>허가</PERMIT_KIND_CODE>
				<CANCEL_DATE>20200101</CANCEL_DATE>
				<CANCEL_NAME>유효기간만료</CANCEL_NAME>
			</item>
			<item>
				<ITEM_SEQ>195500004</ITEM_SEQ>
				<ITEM_NAME>종근당아스피린정</ITEM_NAME>
				<ENTP_NAME>(주)종근당</ENTP_NAME>
				<ITEM_PERMIT_DATE>19550116</ITEM_PERMIT_DATE>
				<INDUTY>의약품</INDUTY>
				<PRDLST_STDR_CODE>195500004</PRDLST_STDR_CODE>
				<SPCLTY_PBLC>일반의약품</SPCLTY_PBLC>
				<PRDUCT_TYPE/>
				<PRDUCT_PRMISN_NO>9</PRDUCT_PRMISN_NO>
				<ITEM_INGR_NAME>아스피린</ITEM_INGR_NAME>
				<ITEM_INGR_CNT>1</ITEM_INGR_CNT>
				<PERMIT_KIND_CODE>허가</PERMIT_KIND_CODE>
				<CANCEL_DATE>20190101</CANCEL_DATE>
			<CANCEL_NAME>유효기간만료</CANCEL_NAME>
			</item>
			<item>
				<ITEM_SEQ>195500005</ITEM_SEQ>
				<ITEM_NAME>중외5%포도당생리식염액(수출명:5%DextroseinnormalsalineInj.)</ITEM_NAME>
				<ENTP_NAME>제이더블유중외제약(주)</ENTP_NAME>
				<ITEM_PERMIT_DATE>19550412</ITEM_PERMIT_DATE>
				<INDUTY>의약품</INDUTY>
				<PRDLST_STDR_CODE>195500005</PRDLST_STDR_CODE>
				<SPCLTY_PBLC>전문의약품</SPCLTY_PBLC>
				<PRDUCT_TYPE/>
				<PRDUCT_PRMISN_NO>792</PRDUCT_PRMISN_NO>
				<ITEM_INGR_NAME>포도당/염화나트륨</ITEM_INGR_NAME>
				<ITEM_INGR_CNT>2</ITEM_INGR_CNT>
				<PERMIT_KIND_CODE>신고</PERMIT_KIND_CODE>
				<CANCEL_DATE/>
				<CANCEL_NAME>정상</CANCEL_NAME>
			</item>
		</items>
	</body>
</response>
```
#### 의약품 제품 주성분 상세정보조회(getMdcinPrductIrdntItem)
* 품목, 주성분, 제조원, 포장단위, 저장방법, 성상등의 품목정보와 허가일자, 허가번호 등의 허가정보 등의 허가받은 의약제품 주성분 정보를 목록으로 제공
* 활용승인 절차 개발단계 : 허용 / 운영단계 : 허용
* 신청가능 트래픽 1000000 / 운영계정은 활용사례 등록시 신청하면 트래픽 증가 가능
* 요청주소 http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService/getMdcinPrductIrdntItem
> 입력변수
  * 업체허가번호       entrps_prmisn_no
  * 제품명(한글)       prduct 
  * 업체명           Entrps
  * 페이지 번호        pageNo 
  * 한 페이지 결과수    numOfRows
 
> http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService/getMdcinPrductIrdntItem?serviceKey=Fm4e4k6u%2Faw6gmlRwAZNteSJKphfGBeXcs1UQQfnN2mnyOVV9tO%2BwtjC9bnBcNhllDDjRWmcYkYixHUWDZfyyw%3D%3D&Entrps_prmisn_no=&Prduct=&Entrps=&pageNo=1&numOfRows=3&
```xml
<response>
	<header>
		<resultCode>00</resultCode>
		<resultMsg>NORMAL SERVICE.</resultMsg>
	</header>
	<body>
		<numOfRows>3</numOfRows>
		<pageNo>1</pageNo>
		<totalCount>174794</totalCount>
		<items>
			<item>
				<ENTRPS_PRMISN_NO>1459</ENTRPS_PRMISN_NO>
				<ENTRPS>(주)종근당</ENTRPS>
				<PRDUCT>종근당염산에페드린정</PRDUCT>
				<MTRAL_SN>1</MTRAL_SN>
				<MTRAL_CODE>M040420</MTRAL_CODE>
				<MTRAL_NM>염산에페드린</MTRAL_NM>
				<QNT>25</QNT>
				<ITEM_SEQ>195500002</ITEM_SEQ>
			</item>
			<item>
				<ENTRPS_PRMISN_NO>1459</ENTRPS_PRMISN_NO>
				<ENTRPS>(주)종근당</ENTRPS>
				<PRDUCT>종근당아스피린정</PRDUCT>
				<MTRAL_SN>1</MTRAL_SN>
				<MTRAL_CODE>M040355</MTRAL_CODE>
				<MTRAL_NM>아스피린</MTRAL_NM>
				<QNT>250</QNT>
				<ITEM_SEQ>195500004</ITEM_SEQ>
			</item>
			<item>
				<ENTRPS_PRMISN_NO>1302</ENTRPS_PRMISN_NO>
				<ENTRPS>제이더블유중외제약(주)</ENTRPS>
				<PRDUCT>중외5%포도당생리식염액(수출명:5%DextroseinnormalsalineInj.)</PRDUCT>
				<MTRAL_SN>1</MTRAL_SN>
				<MTRAL_CODE>M040702</MTRAL_CODE>
				<MTRAL_NM>포도당</MTRAL_NM>
				<QNT>50</QNT>
				<ITEM_SEQ>195500005</ITEM_SEQ>
			</item>
		</items>
	</body>
</response>
```
### 의약품 생산수입실적 서비스 (링크 다운로드 방식)

* https://nedrug.mfds.go.kr/pbp/CCBGA01/getItem?&openDataInfoSeq=8
