### Autonomous Data Warehouse: Data Loading and Management Using SQL on the MovieStream Dataset

* [Important Tools for Everyone Using Oracle Autonomous Database Workshop](https://apexapps.oracle.com/pls/apex/dbpm/r/livelabs/workshop-attendee-2?p210_workshop_id=838&p210_type=3&session=118117143588109)

```sql
CREATE TABLE MOVIE_SALES_FACT
(ORDER_NUM NUMBER(38,0) NOT NULL,
DAY DATE,
DAY_NUM_OF_WEEK NUMBER(38,0),
DAY_NAME VARCHAR2(26),
MONTH VARCHAR2(12),
MONTH_NUM_OF_YEAR NUMBER(38,0),
MONTH_NAME VARCHAR2(26),
QUARTER_NAME VARCHAR2(26),
QUARTER_NUM_OF_YEAR NUMBER(38,0),
YEAR NUMBER(38,0),
CUSTOMER_ID NUMBER(38,0),
USERNAME VARCHAR2(26),
CUSTOMER_NAME VARCHAR2(250),
STREET_ADDRESS VARCHAR2(250),
POSTAL_CODE VARCHAR2(26),
CITY_ID NUMBER(38,0),
CITY VARCHAR2(128),
STATE_PROVINCE_ID NUMBER(38,0),
STATE_PROVINCE VARCHAR2(128),
COUNTRY_ID NUMBER(38,0),
COUNTRY VARCHAR2(126),
COUNTRY_CODE VARCHAR2(26),
CONTINENT VARCHAR2(128),
SEGMENT_NAME VARCHAR2(26),
SEGMENT_DESCRIPTION VARCHAR2(128),
CREDIT_BALANCE NUMBER(38,0),
EDUCATION VARCHAR2(128),
EMAIL VARCHAR2(128),
FULL_TIME VARCHAR2(26),
GENDER VARCHAR2(26),
HOUSEHOLD_SIZE NUMBER(38,0),
HOUSEHOLD_SIZE_BAND VARCHAR2(26),
WORK_EXPERIENCE NUMBER(38,0),
WORK_EXPERIENCE_BAND VARCHAR2(26),
INSUFF_FUNDS_INCIDENTS NUMBER(38,0),
JOB_TYPE VARCHAR2(26),
LATE_MORT_RENT_PMTS NUMBER(38,0),
MARITAL_STATUS VARCHAR2(26),
MORTGAGE_AMT NUMBER(38,0),
NUM_CARS NUMBER(38,0),
NUM_MORTGAGES NUMBER(38,0),
PET VARCHAR2(26),
PROMOTION_RESPONSE NUMBER(38,0),
RENT_OWN VARCHAR2(26),
YEARS_CURRENT_EMPLOYER NUMBER(38,0),
YEARS_CURRENT_EMPLOYER_BAND VARCHAR2(26),
YEARS_CUSTOMER NUMBER(38,0),
YEARS_CUSTOMER_BAND VARCHAR2(26),
YEARS_RESIDENCE NUMBER(38,0),
YEARS_RESIDENCE_BAND VARCHAR2(26),
AGE NUMBER(38,0),
AGE_BAND VARCHAR2(26),
COMMUTE_DISTANCE NUMBER(38,0),
COMMUTE_DISTANCE_BAND VARCHAR2(26),
INCOME NUMBER(38,0),
INCOME_BAND VARCHAR2(26),
MOVIE_ID NUMBER(38,0),
SEARCH_GENRE VARCHAR2(26),
TITLE VARCHAR2(4000),
GENRE VARCHAR2(26),
SKU NUMBER(38,0),
LIST_PRICE NUMBER(38,2),
APP VARCHAR2(26),
DEVICE VARCHAR2(26),
OS VARCHAR2(26),
PAYMENT_METHOD VARCHAR2(26),
DISCOUNT_TYPE VARCHAR2(26),
DISCOUNT_PERCENT NUMBER(38,1),
ACTUAL_PRICE NUMBER(38,2),
QUANTITY_SOLD NUMBER(38,0));

    BEGIN
    DBMS_CLOUD.COPY_DATA(
    table_name => 'MOVIE_SALES_FACT',
    file_uri_list => 'https://objectstorage.ap-tokyo-1.oraclecloud.com/n/dwcsprod/b/moviestream_data_load_workshop_20210709/o/d801_movie_sales_fact_m-201801.csv',
    format =>  '{"type":"csv","skipheaders":"1"}'
    );
    END;
    /

    SELECT
start_time,
update_time,
substr(to_char(update_time-start_time, 'hh24:mi:ss'),11) as duration,
status,
table_name,
rows_loaded,
logfile_table,
badfile_table
FROM user_load_operations
WHERE table_name = 'MOVIE_SALES_FACT'
ORDER BY 1 DESC, 2 DESC
FETCH FIRST 1 ROWS ONLY;

SELECT COUNT(*) FROM movie_sales_fact;
SELECT *
FROM copy$2_log
WHERE RECORD LIKE '%Data File%'ORDER BY 1;

truncate table MOVIE_SALES_FACT;

define uri_ms_oss_bucket = 'https://objectstorage.ap-tokyo-1.oraclecloud.com/n/dwcsprod/b/moviestream_data_load_workshop_20210709/o'
define csv_format_string = '{"type":"csv","skipheaders":"1"}'

BEGIN
DBMS_CLOUD.COPY_DATA (table_name => 'MOVIE_SALES_FACT',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_fact_m-*.csv',
format =>  '&csv_format_string'
);
END;
/

SELECT
start_time,
update_time,
substr(to_char(update_time-start_time, 'hh24:mi:ss'),11) as duration,
status,
table_name,
rows_loaded,
logfile_table,
badfile_table
FROM user_load_operations
WHERE table_name = 'MOVIE_SALES_FACT'
ORDER BY 1 DESC, 2 DESC
FETCH FIRST 1 ROWS ONLY;

SELECT * FROM COPY$7_LOG;
SELECT COUNT(*) FROM COPY$7_BAD;
SELECT COUNT(*) FROM movie_sales_fact;
SELECT *
FROM copy$7_log
WHERE RECORD LIKE '%Data File%'ORDER BY 1;

CREATE UNIQUE INDEX idx_msf_order_num ON MOVIE_SALES_FACT(order_num);
ALTER TABLE movie_sales_fact ADD primary KEY (order_num) USING INDEX idx_msf_order_num;

SELECT SUM(actual_price) FROM movie_sales_fact;

BEGIN
DBMS_CLOUD.COPY_DATA (
table_name => 'MOVIE_SALES_FACT',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_fact_m-201801.csv',
format => '&csv_format_string'
);
END;
/

SELECT SUM(actual_price) FROM movie_sales_fact;

SELECT
segment_name,
SUM(bytes)/1024/1024/1024 AS gb
FROM user_segments
WHERE segment_type='TABLE'
AND segment_name = 'MOVIE_SALES_FACT'
GROUP BY segment_name;

define uri_ms_oss_bucket = 'https://objectstorage.ap-tokyo-1.oraclecloud.com/n/dwcsprod/b/moviestream_data_load_workshop_20210709/o'
define csv_format_string = '{"type":"csv","skipheaders":"1"}'
define adj_column_names = '"ORDER_NUM" INTEGER,"COUNTRY" VARCHAR2(256),"DISCOUNT_PERCENT" NUMBER,"ACTUAL_PRICE" NUMBER';

BEGIN
dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_argentina_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_argentina.csv'
);END;
/

BEGIN
DBMS_CLOUD.VALIDATE_EXTERNAL_TABLE (table_name => 'MOVIE_FIN_ADJ_ARGENTINA_EXT');
END;
/

SELECT COUNT(*) FROM movie_fin_adj_argentina_ext;

SELECT
segment_name,
SUM(bytes)/1024/1024/1024 AS gb
FROM user_segments
WHERE segment_type='TABLE'
AND segment_name=upper('MOVIE_FIN_ADJ_ARGENTINA_EXT')
GROUP BY segment_name;

MERGE INTO movie_sales_fact a
    USING (
        SELECT order_num,
        discount_percent,
        actual_price
    FROM movie_fin_adj_argentina_ext) b
    ON ( a.order_num = b.order_num )
    WHEN MATCHED THEN
    UPDATE
    SET a.discount_percent = b.discount_percent,
    a.actual_price = b.actual_price;
    COMMIT;

  SELECT
SUM(actual_price)
FROM movie_sales_fact;

SELECT
segment_name,
SUM(bytes)/1024/1024/1024 AS gb
FROM user_segments
WHERE segment_type='TABLE'
AND segment_name='MOVIE_SALES_FACT'
GROUP BY segment_name;

BEGIN
dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_Austria_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_austria.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_belarus_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_belarus.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_brazil_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_brazil.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_canada_EXT',  
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_canada.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_chile_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_chile.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_china_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_china.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_egypt_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_egypt.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_finland_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_finland.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_france_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_france.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_germany_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_germany.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_greece_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_greece.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_hungary_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_hungary.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_india_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_india.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_indonesia_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_indonesia.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_israel_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_israel.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_italy_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_italy.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_japan_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_japan.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_jordan_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_jordan.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_kazakhstan_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_kazakhstan.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_kenya_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_kenya.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_madagascar_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_madagascar.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_malaysia_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_malaysia.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_mexico_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_mexico.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_mozambique_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_mozambique.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_netherlands_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_netherlands.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_new_zealand_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_new_zealand.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_pakistan_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_pakistan.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_paraguay_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_paraguay.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_peru_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_peru.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_poland_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_poland.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_portugal_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_portugal.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_romania_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_romania.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_russian_federation_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_russian_federation.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_saudi_arabia_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_saudi_arabia.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_serbia_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_serbia.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_singapore_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_singapore.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_somalia_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_somalia.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_south_korea_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_south_korea.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_thailand_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_thailand.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_turkey_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_turkey.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_ukraine_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_ukraine.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_united_kingdom_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_united_kingdom.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_united_states_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_united_states.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_uruguay_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_uruguay.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_uzbekistan_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_uzbekistan.csv');

dbms_cloud.create_external_table (
table_name => 'MOVIE_FIN_ADJ_venezuela_EXT',
format =>  '&csv_format_string',
column_list => '&adj_column_names',
file_uri_list => '&uri_ms_oss_bucket/d801_movie_sales_finance_adj_venezuela.csv');
END;
/

CREATE OR REPLACE PROCEDURE RUN_ADJ (letter_in IN VARCHAR2) AUTHID CURRENT_USER
IS
ddl_string VARCHAR2(4000);
BEGIN
ddl_string := 'MERGE INTO movie_sales_fact a USING
     (SELECT order_num, discount_percent, actual_price
         FROM movie_fin_adj_'||letter_in||'_ext)
     b ON ( a.order_num = b.order_num )
     WHEN MATCHED THEN UPDATE SET a.discount_percent = b.discount_percent,
     a.actual_price = b.actual_price';
EXECUTE IMMEDIATE ddl_string;
EXECUTE IMMEDIATE 'commit';
END;
/

BEGIN run_adj('austria'); END;
/
BEGIN run_adj('belarus'); END;
/
BEGIN run_adj('brazil'); END;
/
BEGIN run_adj('canada'); END;
/
BEGIN run_adj('chile'); END;
/
BEGIN run_adj('china'); END;
/
BEGIN run_adj('egypt'); END;
/
BEGIN run_adj('finland'); END;
/
BEGIN run_adj('france'); END;
/
BEGIN run_adj('germany'); END;
/
BEGIN run_adj('greece'); END;
/
BEGIN run_adj('hungary'); END;
/
BEGIN run_adj('india'); END;
/
BEGIN run_adj('indonesia'); END;
/
BEGIN run_adj('israel'); END;
/
BEGIN run_adj('italy'); END;
/
BEGIN run_adj('japan'); END;
/
BEGIN run_adj('jordan'); END;
/
BEGIN run_adj('kazakhstan'); END;
/
BEGIN run_adj('kenya'); END;
/
BEGIN run_adj('madagascar'); END;
/
BEGIN run_adj('malaysia'); END;
/
BEGIN run_adj('mexico'); END;
/
BEGIN run_adj('mozambique'); END;
/
BEGIN run_adj('netherlands'); END;
/
BEGIN run_adj('new_zealand'); END;
/
BEGIN run_adj('pakistan'); END;
/
BEGIN run_adj('paraguay'); END;
/
BEGIN run_adj('peru'); END;
/
BEGIN run_adj('poland'); END;
/
BEGIN run_adj('portugal'); END;
/
BEGIN run_adj('romania'); END;
/
BEGIN run_adj('russian_federation'); END;
/
BEGIN run_adj('saudi_arabia'); END;
/
BEGIN run_adj('serbia'); END;
/
BEGIN run_adj('singapore'); END;
/
BEGIN run_adj('somalia'); END;
/
BEGIN run_adj('south_korea'); END;
/
BEGIN run_adj('thailand'); END;
/
BEGIN run_adj('turkey'); END;
/
BEGIN run_adj('ukraine'); END;
/
BEGIN run_adj('united_kingdom'); END;
/
BEGIN run_adj('united_states'); END;
/
BEGIN run_adj('uruguay'); END;
/
BEGIN run_adj('uzbekistan'); END;
/
BEGIN run_adj('venezuela'); END;
/

SELECT
segment_name,
SUM(bytes)/1024/1024/1024 AS gb
FROM user_segments
WHERE segment_type='TABLE'
AND segment_name=upper('MOVIE_SALES_FACT')
GROUP BY segment_name;

```
