## 병렬처리  
### Exadata는 왜 Parallel 처리가 필요한가?
* Exadata의 가장 큰 장점중의 하나는 Smart scan을 하는 것임.
* ``Smart scan``은 Direct read가 필요한데 이를 하기 위해서는 ``parallel query``가 좋은 방법임.
* 병렬도(DOP)를 자동으로 하는 것보다 수동으로 관리하는 방법이 필요함
### Parallel Degree Policy
### 병렬 Query 및 병렬 DML 구현
* DoP(Degree of Parallelism) 갯수 선택
  * 테이블이나 인덱스 생성시 DoP 개수
  * parallel_threads_per_cpu * cpu_count * instance 개수로 계산됨 (2 * 16 * 2 = 64)
  * parallel_degree_limit=cpu
  * Hint
* Skew (병렬 프로세스의 스큐 처리)
  * SELECT DISTINCT은 매우 적은 값의 종류를 갖는 경우
  * Partition명 없이 Insert시 한 개의 Partition으로만 Insert하는 경우
* PQ Distribution
* 유형
  * Parallel Query
  * Parallel DML
  * Parallel DDL
* The Granules 
  * 병렬 처리 작업의 기본 단위를 Granule이라고 합
  * Block range granules(블록범위)
    * 실행시 동적으로 만들어짐
  * ``Partitions granules``(파티션)
    * 파티션 수에때라 정적으로 결정
    * 조건 : ``No. Of partition > parallel * _px_partition_scan_threshod `` 
      * threshod 기본값
        * _px_partition_scan_threshod=64
        * _px_partition_load_dist_threshod=64
* Producer Set -> Consumer Set 으로 Row DISTRIBUTION method
  * PARTITION : 행을 테이블 또는 인덱스의 분할을 기반으로 쿼리 서버에 매핑
  * HASH : 조인 키의 해시 함수를 사용하여 행을 쿼리 서버에 매핑
  * RANGE : 정렬 키 범위를 사용하여 행을 쿼리 서버에 매핑
  * ROUND-ROBIN : 행을 쿼리 서버에 무작위로 매핑
  * BROADCAST : 전체 테이블의 행을 각 쿼리 서버로 브로드 캐스트
  * QC (ORDER) : 실행 코디네이터는 입력을 순서대로 소비
  * QC (RANDOM) : 실행 코디네이터는 임의로 입력을 소비
* Parallel Partition Insert시 Skew 발생
  * Partition된 테이블에 Insert하는 경우, Select된 조건이 특정 Partition에만 들어간다는 것을 알 수 없기 때문에 하나의 Parallel process만 일하게 됨
   ```sql
   -- Partition KEY 값에 의해 분산되어 Serial하게 Insert됨
   INSERT /*+ APPEND PARALLEL(4) */ INTO GBA604S_T
   select /*+ FULL(a) PARALLEL(4) */ * from GBA604S a 
   where a.proc_ymd between :st_date and :ed_date;
   ```
     * 해결책
       * Insert시 파티션 지정 Partition
       ```sql
       INSERT /*+ APPEND PARALLEL(4)  */ INTO GBA604S_T PARTITION(R_201007)
       select /*+ FULL(a) PARALLEL(4) */ * from GBA604S a
       where a.proc_ymd between :st_date and :ed_date;
       ```
       * 받은 데이터를 분사하지 않거나 Random 하게 INSERT 
      ```sql
      --  PQ_DISTRIBUTE(T, NONE)  or PQ_DISTRIBUTE(T, RANDOM)
      INSERT /*+ APPEND PARALLEL(4) PQ_DISTRIBUTE(T, NONE) */ INTO GBA604S_T
      select /*+ FULL(a) PARALLEL(4) */ * from GBA604S a
      where a.proc_ymd between :st_date and :ed_date;
      ```
* Coordinator 위치 확인
  * ``Coordinator는 DML 명령문 위에`` 위치 해야 병렬 처리
* parallel query parameter
 ![pq params](img/exadata_pq.png)
### SQL 실행계획
* dbms_sqltune.report_sql_monitor
  * dbms_sqltune.report_sql_monitor 패키지는 반환되는 타입이 CLOB이기 때문에, 볼 때는 옵션(SESSION)에서 LONG ```SIZE를 10000000``` 이상으로 키워 놓아야 충분한 정보를 볼 수 있음. (상용 툴에서도 마찬가지 임)
   ```sql
     SQL> SET LONG 10000000
     SQL> SET LONGCHUNKSIZE 100000000
     SQL> SET LINESIZE 1000
     SQL> SET PAGESIZE 0
     SQL> SET TRIM ON
     SQL> SET TRIMSPOOL ON
     SQL> SET SQLBLANKLINE ON
     --
     SQL> SQL> select dbms_sqltune.report_sql_monitor(SQL_ID=>'...', REPORT_LEVEL=>'ALL', TYPE=>'TEXT') report from dual;

   
   ```
