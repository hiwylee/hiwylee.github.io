# Oracle Machine Learn for SQL
### Home Page 
 * [Oracle Machine Learning](https://www.oracle.com/database/technologies/datawarehouse-bigdata/machine-learning.html)
 * [Oracle Machine Learning for SQL](https://www.oracle.com/database/technologies/datawarehouse-bigdata/oml4sql.html)
 * [Oracle Open World 2019: Oracle Machine Learning Presentation Downloads](https://blogs.oracle.com/machinelearning/oracle-open-world-2019%3a-oracle-machine-learning-presentation-downloads)
###
 * [OOW 2019 Downloads](https://connor-mcdonald.com/2019/09/24/all-the-openworld-2019-downloads/)
   * [DEV3042 Automated Machine Learning - Data Scientist in 6 Weeks!](https://static.rainfocus.com/oracle/oow19/sess/1552945733705001C6r5/PF/DEV3042%20Automated%20Machine%20Learning%20NEW%20Code%20One%20Dark%20template%20V6_1568390471670001CvFt.pdf)
   * [Using Machine Learning and Oracle Autonomous Database to Target Your Best Customers](https://static.rainfocus.com/oracle/oow19/sess/1553783924808001MRSF/PF/THT4738%20Using%20Machine%20Learning%20and%20Oracle%20Autonomous%20Database%20to%20Target%20Your%20Best%20Customers%20New%20Light%20Template%20V5_1568302075354001iOrC.pdf)
   * [Machine Learning for DBAs](https://static.rainfocus.com/oracle/oow19/sess/1554221123407001tb1Z/PF/THT4914%20The%20Changing%20Role%20of%20the%20DBA_Machine%20Learning%20for%20DBAs%20New%20Template_Light%20V5_1568301164932001ieQo.pdf)
   *[Fraud Detection with Oracle
Autonomous Data Warehouse and
Oracle Machine Learning](https://static.rainfocus.com/oracle/oow19/sess/1551389139454001eEik/PF/TUT1351%20Fraud%20Detection%20with%20Oracle%20Autonomous%20Data%20Warehouse%20and%20Oracle%20Machine%20Learning%20New%20Light%20Template%20V5_1568300810992001gKTX.pdf)
 * [Oracle's Machine Learning:   Newest Features, Use Cases and Road Map](https://www.oracle.com/technetwork/database/options/advanced-analytics/oaaomloverviewnewfeaturesroadmap-5462726.pdf)
 * [``A Simple Guide to Oracle’s Machine Learning and Advanced Analytics``](https://blogs.oracle.com/machinelearning/a-simple-guide-to-oracle%e2%80%99s-machine-learning-and-advanced-analytics)
 * [Oracle Data Mining  12c](https://www.oracle.com/database/technologies/advanced-analytics/odm.html)
### Oracle Data Mining (19c) 문서 
 * [Oracle Advanced Analytics in the Data Warehousing section](https://docs.oracle.com/en/database/oracle/oracle-database/19/data-warehousing.html)
   * Oracle Machine Learning for SQL API Guide :  [HTML](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmapi/index.html) / [PDF](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmapi/oracle-machine-learning-sql-api-guide.pdf)
   * Oracle Machine Learning for SQL Concepts : [HTML](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmcon/index.html) / [PDF](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmcon/oracle-machine-learning-sql-concepts.pdf)
   * Oracle Machine Learning for SQL User's Guide : [HTML](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/index.html) / [PDF](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/oracle-machine-learning-sql-users-guide.pdf)
 * [Get Started with Oracle Data Miner User Interface](Get Started with Oracle Data Miner User Interface)
 * [User's Guide]https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/data-mining-SQL.html)
   * [Highlights of the Data Mining API](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/data-mining-API-highlights.html#GUID-7D00AFBD-EDED-418C-81FB-576A83CA9536)
   * [Example: Targeting Likely Candidates for a Sales Promotion](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/ex-targeting-candidates-sales-promotion.html#GUID-022BC694-E8B9-4686-A6E5-583C06B04E57)
   * [Example: Analyzing Preferred Customers](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/ex-analyzing-preferred-customers.html#GUID-9E0276FD-40E0-4053-9CA6-1FC51397BEEE)
   * [Example: Segmenting Customer Data](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/ex-segmenting-customer-data.html#GUID-AF8605CF-286F-4979-B0EC-A61189D17887)
   * [Example : Building an ESA Model with a Wiki Dataset](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/ex-building-ESA-model-wiki.html#GUID-1F7836F8-E053-4426-BFDD-7DC8064ACA2D)
### OBE (Miner)
* Using Logistic Regression Models (GLM) to Predict Customer Affinity
  - https://www.oracle.com/webfolder/technetwork/tutorials/obe/db/12c/r1/dm/dm_41/ODM12c-17-2_FeaSelGen.html  

### 유용한 링크
* https://www.oracle.com/database/technologies/advanced-analytics/odm-techniques-algorithms.html
* Data Mining Sample Programs: https://docs.oracle.com/database/121/DMPRG/GUID-1F15B394-549B-4CE0-B658-2A9E15DFFBC8.htm#DMPRG715
* Building Model : https://docs.oracle.com/cd/B28359_01/datamine.111/b28131/models_building.htm#BCGFAJIB
* Feature Extraction : https://docs.oracle.com/cd/B28359_01/datamine.111/b28131/models_deploying.htm#BABHCGHH
* [dbms_data_mining and dbms_data_mining _transform Tips](http://www.dba-oracle.com/t_packages_dbms_data_mining_transform.htm)
### [Controlling Access to Mining Models and Data](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/controlling-access-mining-models-data.html#GUID-FC029CBC-788B-41C8-A386-B34200C88885)
* Creating a Data Mining User
```SQL
-Creating a Database User 
CREATE USER dmuser IDENTIFIED BY password
       DEFAULT TABLESPACE USERS
       TEMPORARY TABLESPACE TEMP
       QUOTA UNLIMITED ON USERS;
Commit;
- Privileges Required for Data Mining
GRANT CREATE MINING MODEL TO dmuser;
GRANT CREATE SESSION TO dmuser;
GRANT CREATE TABLE TO dmuser;
GRANT CREATE VIEW TO dmuser;
GRANT EXECUTE ON CTXSYS.CTX_DDL TO dmuser;

GRANT SELECT ON sh.customers TO dmuser;

```
###
* [Exporting and Importing Mining Models](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/exporting-importing-mining-models.html#GUID-0A1878F3-36A7-47EB-B555-BD0FDA66BC23)
* [Database Tuning Considerations for Data Mining](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/installing-configuring-db-data-mining.html#GUID-0CBD0CE0-4F16-4DD9-A0F0-BE1AB57DCE28)
  * Understand the Database tuning considerations for Data Mining.

    DBAs managing production databases that support Oracle Data Mining must follow standard administrative practices as described in Oracle Database Administrator’s Guide.

    Building data mining models and batch scoring of mining models tend to put a DSS-like workload on the system. Single-row scoring tends to put an OLTP-like workload on the system.

    Database memory management can have a major impact on data mining. The correct sizing of Program Global Area (PGA) memory is very important for model building, complex queries, and batch scoring. From a data mining perspective, the System Global Area (SGA) is generally less of a concern. However, the SGA must be sized to accommodate real-time scoring, which loads models into the shared cursor in the SGA. In most cases, you can configure the database to manage memory automatically. To do so, specify the total maximum memory size in the tuning parameter MEMORY_TARGET. With automatic memory management, Oracle Database dynamically exchanges memory between the SGA and the instance PGA as needed to meet processing demands.

    Most data mining algorithms can take advantage of parallel execution when it is enabled in the database. Parameters in INIT.ORA control the behavior of parallel execution.

### Samples
* Data Mining Sample Programs
```bash
> cd $ORACLE_HOME/rdbms/demo
> ls dm*.sql
dmaidemo.sql      dmkmdemo.sql    dmsvddemo.sql              
dmardemo.sql      dmnbdemo.sql    dmsvodem.sql    
dmdtdemo.sql      dmnmdemo.sql    dmsvrdem.sql               
dmdtxvlddemo.sql  dmocdemo.sql    dmtxtnmf.sql                      
dmemdemo.sql      dmsh.sql        dmtxtsvm.sql
dmglcdem.sql      dmshgrants.sql                          
dmglrdem.sql      dmstardemo.sql                          
dmhpdemo.sql      dmsvcdem.sql

```
* Models Created by the Sample Programs
```sql
SELECT mining_function, algorithm, model_name FROM user_mining_models
    ORDER BY mining_function;
 
MINING_FUNCTION                ALGORITHM                      MODEL_NAME
------------------------------ ------------------------------ -------------------
ASSOCIATION_RULES              APRIORI_ASSOCIATION_RULES      AR_SH_SAMPLE
CLASSIFICATION                 GENERALIZED_LINEAR_MODEL       GLMC_SH_CLAS_SAMPLE
CLASSIFICATION                 SUPPORT_VECTOR_MACHINES        T_SVM_CLAS_SAMPLE
CLASSIFICATION                 SUPPORT_VECTOR_MACHINES        SVMC_SH_CLAS_SAMPLE
CLASSIFICATION                 SUPPORT_VECTOR_MACHINES        SVMO_SH_CLAS_SAMPLE
CLASSIFICATION                 NAIVE_BAYES                    NB_SH_CLAS_SAMPLE
CLASSIFICATION                 DECISION_TREE                  DT_SH_CLAS_SAMPLE
CLUSTERING                     EXPECTATION_MAXIMIZATION       EM_SH_CLUS_SAMPLE
CLUSTERING                     O_CLUSTER                      OC_SH_CLUS_SAMPLE
CLUSTERING                     KMEANS                         KM_SH_CLUS_SAMPLE
CLUSTERING                     KMEANS                         DM_STAR_CLUSTER
FEATURE_EXTRACTION             SINGULAR_VALUE_DECOMP          SVD_SH_SAMPLE
FEATURE_EXTRACTION             NONNEGATIVE_MATRIX_FACTOR      NMF_SH_SAMPLE
FEATURE_EXTRACTION             NONNEGATIVE_MATRIX_FACTOR      T_NMF_SAMPLE
REGRESSION                     SUPPORT_VECTOR_MACHINES        SVMR_SH_REGR_SAMPLE
REGRESSION                     GENERALIZED_LINEAR_MODEL       GLMR_SH_REGR_SAMPLE
```
* The Data Mining Sample Data
```sql
SH.CUSTOMERS 
SH.SALES 
SH.PRODUCTS 
SH.SUPPLEMENTARY_DEMOGRAPHICS
SH.COUNTRIES 
```
* The Data Mining Sample Data
---
|View Name	|Description|
|:---|:---|
|MINING_DATA     |      Joins and filters data|
|MINING_DATA_BUILD_V | Data for building models|
|MINING_DATA_TEST_V | Data for testing models|
|MINING_DATA_APPLY_V |Data to be scored|
|MINING_BUILD_TEXT|Data for building models that include text|
|MINING_TEST_TEXT|Data for testing models that include text|
|MINING_APPLY_TEXT|Data, including text columns, to be scored|
|MINING_DATA_ONE_CLASS_V|Data for anomaly detection|

### TYPICAL STEP.
* model build
```sql
 
  -- model build
  IF (v_drop = 'TRUE') THEN -- delete any existing model?
    BEGIN
      DBMS_DATA_MINING.DROP_MODEL('&MODEL_4', TRUE);
    EXCEPTION WHEN OTHERS THEN
      NULL; -- ignore if no existing model to drop
    END;
  END IF;
  DBMS_DATA_MINING.CREATE_MODEL(
    model_name          => '&MODEL_4',
    mining_function     => DBMS_DATA_MINING.CLASSIFICATION,
    data_table_name     => v_data_usage,
    case_id_column_name => '"'||v_caseid||'"',
    target_column_name  => '"'||v_target||'"',
    settings_table_name => v_build_setting,
    xform_list          => v_xlst);
```
* confusion matrix
```sql
 -- confusion matrix

 DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX (
    accuracy                    => v_accuracy,
    apply_result_table_name     => v_apply_data,
    target_table_name           => v_test_data,
    case_id_column_name         => '"'||v_caseid||'"',
    target_column_name          => '"'||v_target||'"',
    confusion_matrix_table_name => v_confusion_matrix,
    score_column_name           => 'PREDICTION',
    score_criterion_column_name => 'PROBABILITY',
    score_criterion_type        => 'PROBABILITY');

```
* average accuracy
```sql
 -- average accuracy
  v_sql := 
    'INSERT INTO '||v_test_metric||' (METRIC_NAME, METRIC_NUM_VALUE)
    WITH
    a as
      (SELECT a.actual_target_value, sum(a.value) recall_total
         FROM '||v_confusion_matrix||' a
         group by a.actual_target_value)
      ,
    b as
      (SELECT count(distinct b.actual_target_value) num_recalls
         FROM '||v_confusion_matrix||' b)
      ,
    c as
      (SELECT c.actual_target_value, value
         FROM '||v_confusion_matrix||' c
         where actual_target_value = predicted_target_value)
      ,
    d as
      (SELECT NVL(sum(c.value/GREATEST(0.0001, a.recall_total)), 0) tot_accuracy
         FROM a, c
         where a.actual_target_value = c.actual_target_value(+))
    SELECT ''AVG_ACCURACY'', d.tot_accuracy/GREATEST(0.0001, b.num_recalls) * 100 avg_accuracy
    FROM b, d';
  execSQL(v_sql);

```
* predictive confidence
```sql
  -- predictive confidence
  v_sql := 
    'INSERT INTO '||v_test_metric||' (METRIC_NAME, METRIC_NUM_VALUE)
    WITH
    a as
      (SELECT a.actual_target_value, sum(a.value) recall_total
         FROM '||v_confusion_matrix||' a
         group by a.actual_target_value)
      ,
    b as
      (SELECT count(distinct b.actual_target_value) num_classes
         FROM '||v_confusion_matrix||' b)
      ,
    c as
      (SELECT c.actual_target_value, value
         FROM '||v_confusion_matrix||' c
         WHERE actual_target_value = predicted_target_value)
      ,
    d as
      (SELECT NVL(sum(c.value/a.recall_total), 0) tot_accuracy
         FROM a, c
         WHERE a.actual_target_value = c.actual_target_value(+))
    SELECT ''PREDICTIVE_CONFIDENCE'', GREATEST(0, ((1 - (1 - d.tot_accuracy/GREATEST(0.0001, b.num_classes)) / GREATEST(0.0001, ((b.num_classes-1)/GREATEST(0.0001, b.num_classes)))) * 100))
    FROM b, d';

```
* lift for each target 
```sql
  -- targets for test results 
  v_sql := 
    'SELECT /*+ NO_PARALLEL */ "'||v_target||'" as prediction FROM 
    ( 
      SELECT "'||v_target||'", 
      RANK() OVER (ORDER BY count("'||v_target||'") DESC) "Rank" 
      FROM '||v_test_data||'  
      GROUP BY "'||v_target||'" 
    ) 
    WHERE rownum <= 5'; 

  FOR i IN 1..v_targets.COUNT LOOP 
    -- lift for each target 
    v_lift := generateUniqueName; 
    DBMS_DATA_MINING.COMPUTE_LIFT ( 
      apply_result_table_name   => v_apply_data, 
      target_table_name         => v_test_data, 
      case_id_column_name       => v_caseid, 
      target_column_name        => '"'||v_target||'"', 
      lift_table_name           => v_lift, 
      positive_target_value     => v_targets(i), 
      score_column_name         => 'PREDICTION', 
      score_criterion_column_name => 'PROBABILITY', 
      num_quantiles             => 100, 
      score_criterion_type      => 'PROBABILITY'); 
    recordOutput('10154', 'TKECP_MD', 'ClassificationBuildNode', '10152', '&MODEL_3', 'Support Vector Machine', v_lift, 'TABLE', v_target||'='||v_targets(i), 'Lift Result'); 
  END LOOP; 
```
* roc for each target (only binary target support) 
```sql 
-- roc for each target (only binary target support) 
  IF (v_targets.COUNT <= 2) THEN 
    FOR i IN 1..v_targets.COUNT LOOP 
      v_roc := generateUniqueName; 
      DBMS_DATA_MINING.COMPUTE_ROC ( 
        roc_area_under_curve        => v_area_under_curve, 
        apply_result_table_name     => v_apply_data, 
        target_table_name           => v_test_data, 
        case_id_column_name         => v_caseid, 
        target_column_name          => '"'||v_target||'"', 
        roc_table_name              => v_roc, 
        positive_target_value       => v_targets(i), 
        score_column_name           => 'PREDICTION', 
        score_criterion_column_name => 'PROBABILITY'); 
      recordOutput('10154', 'TKECP_MD', 'ClassificationBuildNode', '10152', '&MODEL_3', 'Support Vector Machine', v_roc, 'TABLE', v_target||'='||v_targets(i), 'ROC Result'); 
      recordOutput('10154', 'TKECP_MD', 'ClassificationBuildNode', '10152', '&MODEL_3', 'Support Vector Machine', v_area_under_curve, 'SCALAR', v_target||'='||v_targets(i), 'ROC Area Under Curve'); 
    END LOOP; 
  END IF; 
```
