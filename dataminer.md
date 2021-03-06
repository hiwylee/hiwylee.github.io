# Data Miner Home
* https://www.oracle.com/database/technologies/datawarehouse-bigdata/dataminer.html
* https://github.com/oracle/oracle-db-examples/tree/master/machine-learning/odmr
* [User's Guide] (https://docs.oracle.com/en/database/oracle/sql-developer/19.1/dmrug/oracle-data-miner.html#GUID-4A79FAEE-1A30-42CA-9BF1-B24FD07FC667)
## 
* To enable the Data Mining option: 
```
Shut down the database.

srvctl stop database -d db_name
Stop the database service, OracleServiceSID, using the Services program in Control Panel.

Execute these commands.

cd ORACLE_HOME/bin
chopt enable oaa
Start the database service, Oracle ServiceSID, using the Services program in Control Panel.

Start up the database.

srvctl start database -d db_name
```
* sqldeveloper에서 repository를 생성하기 전에 수정이 필요한 사항
```sql
sqldeveloper\dataminer\scripts\installodmr.sql 에 시작부분에 아래 라인 추가.
alter session set "_ORACLE_SCRIPT"=true;
```
* User 생성
```
alter session set "_ORACLE_SCRIPT"=true;
drop user dmuser;
create user C##DMUSER identified by WelCome1234#_
default tablespace users;

grant connect,resource  to C##dmuser;
alter user C##dmuser quota UNLIMITED on users;
SELECT VALUE FROM database_compatible_level;

GRANT CREATE JOB TO dmuser;
GRANT CREATE MINING MODEL TO dmuser;        -- required for creating models
GRANT CREATE PROCEDURE TO dmuser;
GRANT CREATE SEQUENCE TO dmuser;
GRANT CREATE SESSION TO dmuser;
GRANT CREATE SYNONYM TO dmuser;
GRANT CREATE TABLE TO dmuser;
GRANT CREATE TYPE TO dmuser;
GRANT CREATE VIEW TO dmuser;
GRANT EXECUTE ON ctxsys.ctx_ddl TO dmuser;  -- required for text mining
GRANT SELECT ON data TO dmuser;  -- required for data that is not in your schema

```                                               
