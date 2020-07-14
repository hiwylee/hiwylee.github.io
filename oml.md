# Oracle Machine Learn for SQL
### Home Page 
 * [Oracle Machine Learning](https://www.oracle.com/database/technologies/datawarehouse-bigdata/machine-learning.html)
 * [Oracle Machine Learning for SQL](https://www.oracle.com/database/technologies/datawarehouse-bigdata/oml4sql.html)
 * [Oracle Open World 2019: Oracle Machine Learning Presentation Downloads](https://blogs.oracle.com/machinelearning/oracle-open-world-2019%3a-oracle-machine-learning-presentation-downloads)
### OBE (Miner)
* Using Logistic Regression Models (GLM) to Predict Customer Affinity
  - https://www.oracle.com/webfolder/technetwork/tutorials/obe/db/12c/r1/dm/dm_41/ODM12c-17-2_FeaSelGen.html  

### 유용한 링크
* https://www.oracle.com/database/technologies/advanced-analytics/odm-techniques-algorithms.html
* Data Mining Sample Programs: https://docs.oracle.com/database/121/DMPRG/GUID-1F15B394-549B-4CE0-B658-2A9E15DFFBC8.htm#DMPRG715
* Building Model : https://docs.oracle.com/cd/B28359_01/datamine.111/b28131/models_building.htm#BCGFAJIB
* Feature Extraction : https://docs.oracle.com/cd/B28359_01/datamine.111/b28131/models_deploying.htm#BABHCGHH
* [dbms_data_mining and dbms_data_mining _transform Tips](http://www.dba-oracle.com/t_packages_dbms_data_mining_transform.htm)

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
|||
|View Name	|Description|
|MINING_DATA     |      Joins and filters data|
