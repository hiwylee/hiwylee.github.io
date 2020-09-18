## Trace 를 통해서 문제점 해결하는 방법
### Optimizer가 내부적인 비용 계산에 대한 Trace
* [10053 트레이스 파일](http://wiki.gurubee.net/pages/viewpage.action?pageId=3899776)
### 11.2.0.2 vs 19.8 비교시
* 1) 11.2.0.2 각 각 버전을 지정하여 trace 생성
```sql
alter session set optimizer_features_eneble='11.2.0.2';
alter session ser trace_file_indentifier='V11';
alter session set events '10053 trace name context fojrever, level 1';
 SQL> EXPLAIN PLAN FOR 
 @query.sql
 Explained.
 SQL> exit

```
* 2) 19.8 각 각 버전을 지정하여 trace 생성
```sql
alter session set optimizer_features_eneble='19.8.0.0';
alter session ser trace_file_indentifier='V19';
alter session set events '10053 trace name context fojrever, level 1';
 SQL> EXPLAIN PLAN FOR 
 @query.sql
 Explained.
 SQL> exit

```
* 3) 10053 내용 [ PARAMETERS /Bug Fix Control ] 각 각 추출
```
*************************************
  PARAMETERS WITH DEFAULT VALUES
  ******************************
  optimizer_mode_hinted               = false
  optimizer_features_hinted           = 0.0.0
  parallel_execution_enabled          = true
  parallel_query_forced_dop           = 0  
  ...
  중략
  ...
  *********************************
  Bug Fix Control Environment
  ***************************
  fix  4611850 = enabled
  ```
  
  4) 두 버전 별로 상이한 값들만 정리 (parameter and fiexed control)
  5) 19.8.0.0 환경에서 fix control 상태를 11.2.0.2 의 값으로 설정한 뒤 query 실행하여 정상적 플랜으로 나오는지 확인 
  * file name : x.txt

```bash
head x.txt
_fix_control xxxxx:0  
....
```  
  
  6) main run shell 준비 : 플랜에 FULL 이 나오는 경우 확인 
  
  ```bash
  cat x.sh
  
  sqlplus system/*** << EOF | egrep "PARM| 검색조건" | grep FULL
  alte session set current_schema=SCOTT;
  alter session set "$1"="$2";
  
  -- var cust_no varchar(12)
  -- exec cust_no= 1234;
  explain plan for
  @query.sql
  select * from table(dmbs_xplain.display);
  exit
  EOF
  ```
  
  7) runx.sh 
  
  ```bash
  while read param val ; do
     echo 
     echo "*** $param $val ***"
     echo
     sh x.sh $param $val
  done < x.sh
  ```
  
