

To enable the Data Mining option: 

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
