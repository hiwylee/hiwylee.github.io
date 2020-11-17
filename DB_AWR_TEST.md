## RAC AWR Report 분석 연습
### 준비물
```
1. DBCS(RAC) 
2. RAT ( SPA & DB Replay )
2. Stress Tools - SwingBench
3. AWR script
```

### 테스트 시나리오

``` 
<<<< Database 1 >>>>>
1. DBCS Setup)
2. RAT 설정
3. Sample Schema Setup (SwingBench) : https://ittutorial.org/install-swingbench-2-6-and-set-up-order-entry-schema/
   - Scema 생성 : SOE
   - Invalid object : alter package soe.ORDERENTRY compile;
   - 통계 생성: exec dbms_stats.gather_schema_stats('SOE'); 
<Baseline>
4. Create Snapshot : http://www.dba-oracle.com/t_awr_snapshot_definition.htm
   - EXEC dbms_workload_repository.create_snapshot
5. Stress Test  
6. Snapshot Baseline 1 생성
  EXEC dbms_workload_repository.create_baseline -
     (  start_snap_id=>1109, end_snap_id=>1111, -
        baseline_name=>'EOM Baseline');
<Baseline with RAT>
7. Create Snapshot : http://www.dba-oracle.com/t_awr_snapshot_definition.htm
   - EXEC dbms_workload_repository.create_snapshot
8. Workload Capture   
8. Stress Test : 부하를 더 많이 줌.  
9. Snapshot Baseline 2 생성
10. expdp soe schema        
```
