# Oracle Machine Learn for SQL
### Home Page 
 * [Oracle Machine Learning](https://www.oracle.com/database/technologies/datawarehouse-bigdata/machine-learning.html)
 * [Oracle Machine Learning for SQL](https://www.oracle.com/database/technologies/datawarehouse-bigdata/oml4sql.html)
 * [Oracle Open World 2019: Oracle Machine Learning Presentation Downloads](https://blogs.oracle.com/machinelearning/oracle-open-world-2019%3a-oracle-machine-learning-presentation-downloads)
###
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
