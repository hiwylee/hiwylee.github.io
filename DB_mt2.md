## Oracle Multitenant Fundamentals 2
* [LiveLabs - Oracle Multitenant Fundamentals](https://oracle.github.io/learning-library/data-management-library/database/multitenant/workshops/freetier/?lab=lab-4-application-containers#Step8:PDBRefresh)
### Application Containers
#### Step 1: Instant SaaS
* Create and open the master application root.

```sql
SQL*Plus: Release 19.0.0.0.0 - Production on Sat Sep 12 06:03:08 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

SQL> connect sys/oracle@localhost:1523/cdb1 as sysdba
Connected.
SQL> conn system/oracle@localhost:1523/cdb1;
Connected.
SQL> ed
Wrote file afiedt.buf

  1* create pluggable database wmStore_Master as application container admin user wm_admin identified by oracle
SQL> /

Pluggable database created.

SQL> alter pluggable database wmStore_Master open;


Pluggable database altered.


```
* Define the application master.

```sql
SQL> conn system/oracle@localhost:1523/wmStore_Master;
Connected.
SQL>
SQL> alter pluggable database application wmStorer begin install '1.0';
  
Pluggable database altered.
SQL> create user wmStore_Admin identified by oracle container=all

User created.

SQL> grant create session, dba to wmStore_Admin;

Grant succeeded.

SQL> create tablespace wmStore_TBS datafile size 100M autoextend on next 10M maxsize 200M;

Tablespace created.

SQL> alter user wmStore_Admin default tablespace wmStore_TBS;

User altered.


SQL> connect wmStore_Admin/oracle@localhost:1523/wmStore_Master;
Connected.
SQL> create table wm_Products
-- sharing = extended data
(Row_GUID         raw(16)           default Sys_GUID()                      primary key
,Name             varchar2(30)                                    not null  unique
)
;   

Table created.

SQL> create table wm_Orders
-- sharing = metadata
(Row_GUID         raw(16)           default Sys_GUID()                      primary key
,Order_Number     number(16,0)      generated always as identity  not null  unique
,Order_Date       date         2         default   current_date        not null
,Campaign_ID      raw(16)
)
;  

Table created.



SQL> create table wm_Campaigns
-- sharing = data
(Row_GUID         raw(16)           default Sys_GUID()                      primary key
,Name             varchar2(30)                                    not null  unique
)
;  

Table created.

SQL> alter table wm_Orders add constraint wm_Orders_F1
foreign key (Campaign_ID)
references wm_Campaigns(Row_GUID)
disable
;   
Table altered.

SQL>

create table wm_Order_Items
-- sharing = metadata
(Row_GUID         raw(16)                    default Sys_GUID()           primary key 
,Order_ID         raw(16)           not null
,Item_Num         number(16,0)      not null
,Product_ID       raw(16)           not null
,Order_Qty        number(16,0)      not null
)
;
alter table wm_Order_Items add constraint wm_Order_Items_F1 
foreign key (Order_ID)
references wm_Orders(Row_GUID)
disable
;
alter table wm_Order_Items add constraint wm_Order_Items_F2 
foreign key (Product_ID)
references wm_Products(Row_GUID)
disable
;
alter table wm_Order_Items add constraint wm_Order_Items_F2 
foreign key (Product_ID)
references wm_Products(Row_GUID)
disable
;
create or replace view wm_Order_Details
-- sharing = metadata
(Order_Number
,Campaign_Name
,Item_Num
,Product_Name
,Order_Qty
) as
select o.Order_Number
,      c.Name
,      i.Item_Num
,      p.Name
,      i.Order_Qty
from wm_Orders o
join wm_Order_Items i
on  i.Order_ID = o.Row_GUID
join wm_Products p
on   i.Product_ID = p.Row_GUID
left outer join wm_Campaigns c
on  o.Campaign_ID = c.Row_GUID
;
insert into wm_Campaigns (Row_GUID, Name) values ('01', 'Locals vs Yokels');

insert into wm_Campaigns (Row_GUID, Name) values ('02', 'Black Friday 2016');

insert into wm_Campaigns (Row_GUID, Name) values ('03', 'Christmas 2016');

insert into wm_Products (Row_GUID, Name) values ('01', 'Tornado Twisted');

insert into wm_Products (Row_GUID, Name) values ('02', 'Muskogee Magic');

insert into wm_Products (Row_GUID, Name) values ('03', 'Root 66 Beer Float');

insert into wm_Products (Row_GUID, Name) values ('04', 'Yokie Dokie Okie Eggnog');
commialtet;
SQL> alter pluggable database application wmStorer end install '1.0'
SQL> /

Pluggable database altered.

```
* Create the application seed.

```sql
SQL> conn system/oracle@localhost:1523/wmStore_Master;
Connected.
SQL>create pluggable database as seed admin user wm_admin identified by oracle
SQL> /

Pluggable database created.

SQL> connect sys/oracle@localhost:1523/wmStore_Master as SysDBA
Connected.
SQL>
alter pluggable database wmStore_Master$Seed open
SQL> /

Pluggable database altered.

SQL>

```
* Sync the seed with the application wmStore.

```sql

SQL> conn system/oracle@localhost:1523/wmStore_Master$Seed;
Connected.
SQL> alter pluggable database application wmStorer sync
SQL> /

Pluggable database altered.
```

* Provision the application databases for the 4 stores.

```sql
SQL> conn system/oracle@localhost:1523/wmStore_Master;
Connected.

SQL> ed
Wrote file afiedt.buf

    select P.Con_ID                 c1
    ,      P.Name                   c2
    ,      P.CON_UID                c3
    ,      P.Restricted             c4
    ,      P.Open_Mode              c5
    ,      P.Application_Root       c6
    ,      P.Application_PDB        c7
    ,      P.Application_Seed       c8
    ,      P.Application_Root_Clone c9
    ,      P.Proxy_PDB              c10
    ,      AC.Name                  c11
    from v$PDBs P
    left outer join v$PDBs AC
    on AC.Con_ID = P.Application_Root_Con_ID
    order by P.Name
    ,        nvl(AC.Name,P.Name)
    ,        P.Application_Root desc
    ,        P.Application_Seed desc
    ,        P.Name
SQL> /

Sat Sep 12                                                                                                                                               page    1
                                                                                  PDBs in CDB CDB1

Con ID PDB Name                            Con UID Restricted? Open Mode  Root? App PDB? Seed? Root Clone? Proxy? App Container Name
------ ------------------------------ ------------ ----------- ---------- ----- -------- ----- ----------- ------ ------------------------------
     8 CALIFORNIA                       1698289146 NO          READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
    10 NYC                              1581866043 NO          READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
     2 PDB$SEED                         2131469164 NO          READ ONLY  NO    NO       NO    NO          NO
     3 PDB1                             1902349605 NO          READ WRITE NO    NO       NO    NO          NO
     6 PDB2                             2520575836 NO          READ WRITE NO    NO       NO    NO          NO
     9 TAHOE                             353897558 NO          READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
     7 TULSA                             186289129 NO          READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
     4 WMSTORE_MASTER                   2383393305 NO          READ WRITE YES   NO       NO    NO          NO
     5 WMSTORE_MASTER$SEED              2430369725 NO          READ WRITE NO    YES      YES   NO          NO     WMSTORE_MASTER

9 rows selected.

SQL>

SQL> show user
USER is "SYSTEM"
SQL>
SQL> alter session set container=wmStore_Master;

Session altered.

SQL> connect wmStore_Admin/oracle@localhost:1523/wmStore_Master;
Connected.
SQL>
SQL> alter session set container = Tulsa;

Session altered.

SQL> alter session set container = CDB$Root;
ERROR:
ORA-01031: insufficient privileges


SQL> connect wm_admin/oracle@localhost:1523/Tulsa;
Connected.
SQL> alter session set container = Tulsa;

Session altered.

SQL> connect wm_admin/oracle@localhost:1523/California;
Connected.
SQL> alter session set container = Tulsa;
ERROR:
ORA-01031: insufficient privileges


SQL> @Lab2_Queries.sql
....
Proxy? Order Qty
------ ---------
Yokels     1,274
Locals     1,189

SQL>
SQL> set echo off

***********************************************************************************
Press [Enter] to continue...



```
#### Step 3: Upgrade from v1 to v2
* Create the upgrade of the pluggable databases.

```sql
SQL> conn system/oracle@localhost:1523/wmStore_Master;
Connected.
SQL>
SQL> alter pluggable database application wmStorer begin upgrade '1.0' to '2.0';

Pluggable database altered.

SQL> connect wmStore_Admin/oracle@localhost:1523/wmStore_Master
Connected.
SQL> alter table wm_Products add
(Local_Product_YN char(1)           default 'Y'                   not null
)
;  2    3    4

Table altered.

SQL> alter table wm_Products add constraint Local_Product_Bool
check (Local_Product_YN in ('Y','N'))
;  2    3

Table altered.

SQL> create or replace view wm_Order_Details
-- sharing = metadata
(Order_Number
,Campaign_Name
,Item_Num
,Product_Name
,Local_Product_YN
,Order_Qty
) as
  2    3    4    5    6    7    8    9   10  select o.Order_Number
 11  ,      c.Name
,      i.Item_Num
,      p.Name
 12   13   14  ,      p.Local_Product_YN
,      i.Order_Qty
 15   16  from wm_Orders o
join wm_Order_Items i
 17   18  on  i.Order_ID = o.Row_GUID
join wm_Products p
on   i.Product_ID = p.Row_GUID
left outer join wm_Campaigns c
on  o.Campaign_ID = c.Row_GUID
; 19   20   21   22   23

View created.

SQL> update wm_Products
set Local_Product_YN = 'N'
where Name in
('Tornado Twisted'
,'Muskogee Magic'
,'Root 66 Beer Float'
,'Yokie Dokie Okie Eggnog'
)
;  2    3    4    5    6    7    8    9

4 rows updated.

SQL> commit;

Commit complete.

SQL> alter pluggable database application wmStorer end upgrade
SQL> /

Pluggable database altered.

SQL>

```
* Apply the upgrade to Tulsa/California/Tahoe

```sql
SQL> connect system/oracle@localhost:1523/Tulsa
Connected.
SQL> alter pluggable database application wmStorer sync;

Pluggable database altered.


SQL> connect system/oracle@localhost:1523/Tulsa
Connected.
SQL> alter pluggable database application wmStorer sync;

Pluggable database altered.

SQL> connect system/oracle@localhost:1523/Tahoe
Connected.
SQL> alter pluggable database application wmStorer sync;

Pluggable database altered.

SQL> connect system/oracle@localhost:1523/California
Connected.
SQL> alter pluggable database application wmStorer sync;

Pluggable database altered.

SQL>


```
* Take a look at a pluggable the upgrade was applied to.

```sql
SQL>
SQL> column Row_GUID noprint
column Name             format a30 heading "Product Name"
column Local_Product_YN format a14 heading "Local Product?"SQL> SQL>
SQL>

SQL>
SQL> define Franchise = "Tulsa"
SQL> ttitle "Products in Franchise &Franchise"
SQL> set echo on
SQL> connect wmStore_Admin/oracle@localhost:1523/Tulsa
Connected.
SQL> desc wm_Products
 Name                                                                                                  Null?    Type
 ----------------------------------------------------------------------------------------------------- -------- --------------------------------------------------------------------
 ROW_GUID                                                                                              NOT NULL RAW(16)
 NAME                                                                                                  NOT NULL VARCHAR2(30)
 LOCAL_PRODUCT_YN                                                                                      NOT NULL CHAR(1)

SQL> select *
from wm_Products
;  

Sat Sep 12                                                                                                                                               page    1
                                                                            Products in Franchise Tulsa

Product Name                   Local Product?
------------------------------ --------------
Tornado Twisted                N
Muskogee Magic                 N
Root 66 Beer Float             N
Yokie Dokie Okie Eggnog        N
Amariller Chiller              Y
Wichita Witchcraft             Y
St Louis Blueberry             Y
Arkansas Riviera               Y

8 rows selected.

SQL> set echo off
SQL>

```
* Look at a pluggable that the upgrade was not applied to and look at the table definitions and data compared to one that was upgraded.

```sql
SQL> define Franchise = "NYC"
SQL> ttitle "Products in Franchise &Franchise"
SQL> set echo on
SQL> connect wmStore_Admin/oracle@localhost:1523/NYC
Connected.
SQL> desc wm_Products
 Name                                                                                                  Null?    Type
 ----------------------------------------------------------------------------------------------------- -------- --------------------------------------------------------------------
 ROW_GUID                                                                                              NOT NULL RAW(16)
 NAME                                                                                                  NOT NULL VARCHAR2(30)

SQL> select *
from wm_Products
;  

Sat Sep 12                                                                                                                                               page    1
                                                                             Products in Franchise NYC

Product Name
------------------------------
Manhattan Madness
Lady Liberty Lemonade
Empire Statemint
Big Apple Pie
Tornado Twisted
Muskogee Magic
Root 66 Beer Float
Yokie Dokie Okie Eggnog

8 rows selected.

SQL> set echo off
SQL>

```
#### Step 4: Containers Queries
*  cross-container aggregation capability – containers() queries

```sql

SQL> connect wmStore_Admin/oracle@localhost:1523/wmStore_Master
Connected.
SQL>
SQL>
SQL>
SQL>
SQL>
SQL> column c1 format a30       heading "Franchise"
SQL> column c2 format 9999999   heading "Order #"
SQL> column c3 format a30       heading "Campaign"
SQL> column c4 format 999999    heading "Item #"
column c5 format a30       heading "Product"
column c6 format 9,999     heading "Qty"
SQL> SQL> SQL> column c7 format 9,999,999 heading "Num Orders"
SQL>
SQL>
SQL>
SQL> break on c1 on c3 on c5
SQL> column c4 noprint
SQL> ttitle "Products (in Tulsa and NYC)"
SQL> set echo on
SQL>
SQL> select con$name c1
,      Name     c5
from containers(wm_Products)
where con$name in ('TULSA','NYC')
order by 1
,        2
;  2    3    4    5    6    7

Sat Sep 12                                                                                                                                               page    1
                                                                            Products (in Tulsa and NYC)

Franchise                      Product
------------------------------ ------------------------------
NYC                            Big Apple Pie
                               Empire Statemint
                               Lady Liberty Lemonade
                               Manhattan Madness
                               Muskogee Magic
                               Root 66 Beer Float
                               Tornado Twisted
                               Yokie Dokie Okie Eggnog
TULSA                          Amariller Chiller
                               Arkansas Riviera
                               Muskogee Magic
                               Root 66 Beer Float
                               St Louis Blueberry
                               Tornado Twisted
                               Wichita Witchcraft
                               Yokie Dokie Okie Eggnog

16 rows selected.

SQL> ttitle "Order Counts Per Campaign (Across All Franchises)"
SQL> set echo on
SQL> select con$name      c1
,      Campaign_Name c3
,      count(*)      c7
from containers(wm_Order_Details)
group by con$name
,        Campaign_Name
order by 1
,        3 desc
,        2
;  2    3    4    5    6    7    8    9   10

Sat Sep 12                                                                                                                                               page    1
                                                                 Order Counts Per Campaign (Across All Franchises)

Franchise                      Campaign                       Num Orders
------------------------------ ------------------------------ ----------
CALIFORNIA                     Locals vs Yokels                      526
                               Black Friday 2016                     493
                               Christmas 2016                        422
NYC                            Black Friday 2016                     350
                               Locals vs Yokels                      319
                               Christmas 2016                        316
TAHOE                          Black Friday 2016                     389
                               Christmas 2016                        378
                               Locals vs Yokels                      372
TULSA                          Locals vs Yokels                      526
                               Black Friday 2016                     493
                               Christmas 2016                        422

12 rows selected.

SQL> set echo off
SQL> ttitle "Order Volume Per Product (Across All Franchises)"
SQL> set echo on
SQL> select con$name      c1
,      Product_Name  c5
,      count(*)      c7
from containers(wm_Order_Details)
group by con$name
,        Product_Name
order by 1
,        3 desc
,        2
;  2    3    4    5    6    7    8    9   10

Sat Sep 12                                                                                                                                               page    1
                                                                  Order Volume Per Product (Across All Franchises)

Franchise                      Product                        Num Orders
------------------------------ ------------------------------ ----------
CALIFORNIA                     Golden State of Mind                  198
                               Yokie Dokie Okie Eggnog               187
                               Muskogee Magic                        183
                               Surf Sup                              179
                               Fog City Mister                       178
                               Root 66 Beer Float                    178
                               Tornado Twisted                       177
                               Fresno Fro-Yo                         161
NYC                            Root 66 Beer Float                    133
                               Tornado Twisted                       129
                               Manhattan Madness                     126
                               Muskogee Magic                        124
                               Big Apple Pie                         123
                               Yokie Dokie Okie Eggnog               121
                               Lady Liberty Lemonade                 115
                               Empire Statemint                      114
TAHOE                          Tornado Twisted                       157
                               Emerald Baydream                      153
                               Ski Bum                               150
                               Keep Tahoe Blueberry                  149
                               Muskogee Magic                        144
                               Yokie Dokie Okie Eggnog               143
                               Fresh Pow Wow                         125
                               Root 66 Beer Float                    118
TULSA                          Amariller Chiller                     198
                               Yokie Dokie Okie Eggnog               187
                               Muskogee Magic                        183
                               Arkansas Riviera                      179
                               Tornado Twisted                       178
                               Wichita Witchcraft                    178
                               St Louis Blueberry                    177
                               Root 66 Beer Float                    161

32 rows selected.

SQL> set echo off
SQL>

```
#### Step 5: Application Root Clones and Compatibility

```sql
SQL> connect system/oracle@localhost:1523/cdb1
Connected.
SQL> set linesize 180
SQL> column c0  noprint new_value            CDB_Name
column c1  heading "Con ID"             format 99
SQL> SQL> column c2  heading "PDB Name"           format a30
column c3  heading "Con UID"            format 99999999999
column c4  heading "Restricted?"        format a11
column c5  heading "Open Mode"          format a10
column c6  heading "Root?"        SQL>       format a5
column c7  heading "App PDB?"           format a8
column c8  heading "Seed?"              format a5
column c9  heading "Root Clone?"        format a11
column c10 heading "Proxy?"             format a6
SQL> SQL> SQL> SQL> SQL> SQL> SQL> SQL> column c11 heading "App Container Name" format a30
SQL> set termout off
SQL> set termout off
SQL> select Sys_Context('Userenv', 'CDB_Name') c0
from dual
;  2    3

Sat Sep 12                                                                                                                                               page    1
                                                                             Products in Franchise NYC




SQL> ttitle "PDBs in CDB &CDB_Name"
SQL> set termout on
SQL> ed
Wrote file afiedt.buf

  1  select P.Con_ID                 c1
  2  ,      P.Name                   c2
  3  ,      P.CON_UID                c3
  4  ,      P.Restricted             c4
  5  ,      P.Open_Mode              c5
  6  ,      P.Application_Root       c6
  7  ,      P.Application_PDB        c7
  8  ,      P.Application_Seed       c8
  9  ,      P.Application_Root_Clone c9
 10  ,      P.Proxy_PDB              c10
 11  ,      AC.Name                  c11
 12  from v$PDBs P
 13  left outer join v$PDBs AC
 14  on AC.Con_ID = P.Application_Root_Con_ID
 15  order by P.Name
 16  ,        nvl(AC.Name,P.Name)
 17  ,        P.Application_Root desc
 18  ,        P.Application_Seed desc
 19* ,        P.Name
SQL> /

Sat Sep 12                                                                                                                                               page    1
                                                                                  PDBs in CDB CDB1

Con ID PDB Name                            Con UID Open Mode  Root? App PDB? Seed? Root Clone? Proxy? App Container Name
------ ------------------------------ ------------ ---------- ----- -------- ----- ----------- ------ ------------------------------
     8 CALIFORNIA                       1698289146 READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
    12 F2383393305_3_1                  3137180141 READ WRITE YES   YES      NO    YES         NO     WMSTORE_MASTER
    10 NYC                              1581866043 READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
     2 PDB$SEED                         2131469164 READ ONLY  NO    NO       NO    NO          NO
     3 PDB1                             1902349605 READ WRITE NO    NO       NO    NO          NO
     6 PDB2                             2520575836 READ WRITE NO    NO       NO    NO          NO
     9 TAHOE                             353897558 READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
     7 TULSA                             186289129 READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
     4 WMSTORE_MASTER                   2383393305 READ WRITE YES   NO       NO    NO          NO
     5 WMSTORE_MASTER$SEED              2430369725 READ WRITE NO    YES      YES   NO          NO     WMSTORE_MASTER

10 rows selected.

SQL> conn system/oracle@localhost:1523/wmStore_Master;
Connected.
SQL> ed
Wrote file afiedt.buf

  1  -- NYC is still version 1.0
  2* alter pluggable database application wmStorer set compatibility version '2.0';
SQL> /
alter pluggable database application wmStorer set compatibility version '2.0';
                                                                             *
ERROR at line 2:
ORA-00933: SQL command not properly ended


SQL> ed
Wrote file afiedt.buf

  1  -- NYC is still version 1.0
  2* alter pluggable database application wmStorer set compatibility version '2.0'
SQL> /
-- NYC is still version 1.0
*
ERROR at line 1:
ORA-65340: invalid application compatibility version


SQL> column CON_UID               heading "Con UID"          format 999999999999
column APP_NAME              heading "Application Name" format a20          truncate
column APP_ID                heading "App ID"           format 99999
SQL> SQL> SQL> column APP_VERSION           heading "Version"          format a7
column APP_STATUS            heading "Status"           format a12
column APP_ID                noprintSQL> SQL>
SQL>
SQL>
SQL> select * from DBA_App_PDB_Status;

Sat Sep 12                                                                                                                                               page    1
                                                                                  PDBs in CDB CDB1

      Con UID Application Name     Version Status
------------- -------------------- ------- ------------
   2430369725 WMSTORER             1.0     NORMAL
   1581866043 WMSTORER             1.0     NORMAL
    353897558 WMSTORER             2.0     NORMAL
   1698289146 WMSTORER             2.0     NORMAL
    186289129 WMSTORER             2.0     NORMAL

SQL> conn system/oracle@localhost:1523/NYC;
Connected.
SQL> alter pluggable database application wmStorer sync;

Pluggable database altered.

SQL>
SQL> conn system/oracle@localhost:1523/wmStore_Master$Seed
Connected.
SQL> alter pluggable database application wmStorer sync;

Pluggable database altered.

SQL> conn system/oracle@localhost:1523/wmStore_Master
Connected.
SQL> alter pluggable database application wmStore set compatibility version '2.0';
alter pluggable database application wmStore set compatibility version '2.0'
*
ERROR at line 1:
ORA-65217: application WMSTORE does not exist


SQL> ed
Wrote file afiedt.buf

  1* alter pluggable database application wmStorer set compatibility version '2.0'
SQL> /

Pluggable database altered.

SQL> conn system/oracle@localhost:1523/cdb1
Connected.
SQL> set linesize 180
SQL> column c0  noprint new_value            CDB_Name
column c1  heading "Con ID"             format 99
column c2  heading "PDB Name"           format a30
SQL> SQL> SQL> column c3  heading "Con UID"            format 99999999999
column c4  heading "Restricted?"        format a11
SQL> SQL> column c5  heading "Open Mode"          format a10
column c6  heading "Root?"              format a5
column c7  heading "App PDB?"           format a8
column c8  heading "Seed?"              format a5
column c9  heading "Root Clone?"        format a11
column c10 heading "Proxy?"             format a6
SQL> SQL> SQL> SQL> SQL> SQL> column c11 heading "App Container Name" format a30
SQL>
SQL>
SQL> set termout off
SQL> select Sys_Context('Userenv', 'CDB_Name') c0
from dual
;  2    3

Sat Sep 12                                                                                                                                               page    1
                                                                                  PDBs in CDB CDB1




SQL> ttitle "PDBs in CDB &CDB_Name"
SQL> set termout on
SQL> select P.Con_ID                 c1
,      P.Name                   c2
,      P.CON_UID                c3
,      P.Restricted             c4
,      P.Open_Mode              c5
,      P.Application_Root       c6
  2    3    4    5    6    7  ,      P.Application_PDB        c7
,      P.Application_Seed       c8
  8    9  ,      P.Application_Root_Clone c9
,      P.Proxy_PDB              c10
,      AC.Name                  c11
from v$PDBs P
left outer join v$PDBs AC
on AC.Con_ID = P.Application_Root_Con_ID
 10   11   12   13   14   15  order by P.Name
,        nvl(AC.Name,P.Name)
,        P.Application_Root desc
,        P.Application_Seed desc
,        P.Name
; 16   17   18   19   20

Sat Sep 12                                                                                                                                               page    1
                                                                                  PDBs in CDB CDB1

Con ID PDB Name                            Con UID Open Mode  Root? App PDB? Seed? Root Clone? Proxy? App Container Name
------ ------------------------------ ------------ ---------- ----- -------- ----- ----------- ------ ------------------------------
     8 CALIFORNIA                       1698289146 READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
    10 NYC                              1581866043 READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
     2 PDB$SEED                         2131469164 READ ONLY  NO    NO       NO    NO          NO
     3 PDB1                             1902349605 READ WRITE NO    NO       NO    NO          NO
     6 PDB2                             2520575836 READ WRITE NO    NO       NO    NO          NO
     9 TAHOE                             353897558 READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
     7 TULSA                             186289129 READ WRITE NO    YES      NO    NO          NO     WMSTORE_MASTER
     4 WMSTORE_MASTER                   2383393305 READ WRITE YES   NO       NO    NO          NO
     5 WMSTORE_MASTER$SEED              2430369725 READ WRITE NO    YES      YES   NO          NO     WMSTORE_MASTER

9 rows selected.

    
```
#### Step 6: Expansion Beyond Single CDB and Application Root Replicas
* Connect to CDB2 & a datbase link to CDB1 

```sql
[oracle@workshop ~]$ sqlplus /nolog

SQL*Plus: Release 19.0.0.0.0 - Production on Sat Sep 12 12:57:27 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

SQL> connect system/oracle@localhost:1524/cdb2
Connected.
SQL> create public database link cdb1_dblink connect to system identified by oracle using 'localhost:1523/cdb1';

Database link created.

SQL>

```
* Create and open the Application Root Replicas (ARRs).

```sql
SQL> create pluggable database wmStore_International as application container from wmStore_Master@CDB1_DBLink;

Pluggable database created.

SQL> create pluggable database wmStore_West as application container from wmStore_Master@CDB1_DBLink;

Pluggable database created.

SQL> alter pluggable database all open;

Pluggable database altered.

SQL>

```
* Create the CDB$Root-level DB Link to CDB2.

```sql
SQL> connect system/oracle@localhost:1523/cdb1
Connected.
SQL> create public database link CDB2_DBLink connect system identifed by oracle using 'localhost:1524/cdb2';
create public database link CDB2_DBLink connect system identifed by oracle using 'localhost:1524/cdb2'
                                                *
ERROR at line 1:
ORA-00946: missing TO keyword


SQL> ed
Wrote file afiedt.buf

  1* create public database link CDB2_DBLink connect to system identifed by oracle using 'localhost:1524/cdb2'
SQL> /
create public database link CDB2_DBLink connect to system identifed by oracle using 'localhost:1524/cdb2'
                                                          *
ERROR at line 1:
ORA-00954: missing IDENTIFIED keyword


SQL> ed
Wrote file afiedt.buf

  1* create public database link CDB2_DBLink connect to system identified by oracle using 'localhost:1524/cdb2'
SQL> /

Database link created.

```
* Create and open Proxy PDBs for the Application Root Replicas.

```sql
SQL> select db_link from dba_db_links;

DB_LINK
--------------------
SYS_HUB

SQL> show user
USER is "SYSTEM"
SQL> create public database link CDB2_DBLink connect to system identified by oracle using 'localhost:1524/cdb2';

Database link created.

SQL> create pluggable database wmStore_international_Proxy as proxy from wmStore_international@CDB2_DBLink;

Pluggable database created.

SQL> create pluggable database wmStore_West_Proxy
as proxy from wmStore_West@CDB2_DBLink;  2
Pluggable database created.

SQL>
```

* Synchronize the ARRs via their proxies.

```sql
SQL> conn sys/oracle@localhost:1523/wmStore_International_Proxy as sysdba
Connected.

SQL> alter pluggable database application wmStorer sync;

Pluggable database altered.

SQL> conn sys/oracle@localhost:1523/wmStore_West_Proxy as sysdba
Connected.
SQL>
SQL>  alter pluggable database application wmStorer sync;

Pluggable database altered.

SQL>

```
* Create and open the Application Seed PDBs wmStore_International and sync it with Application wmStore.

```sql

SQL> conn sys/oracle@localhost:1523/wmStore_West_Proxy as sysdba
Connected.
SQL>
SQL>
SQL>
SQL>
SQL>
SQL>  alter pluggable database application wmStorer sync;

Pluggable database altered.

SQL> conn system/oracle@localhost:1524/wmStore_International
Connected.
SQL>
SQL>
SQL> create pluggable database as seed admin user ww_admin identified by oracle;

Pluggable database created.

SQL> conn sys/oracle@localhost:1524/wmStore_International as SysDBA
Connected.
SQL>
SQL> alter pluggable database wmStore_international$Seed open;

Pluggable database altered.

SQL> connect system/oracle@localhost:1524/wmStore_International$Seed
Connected.
SQL> alter pluggable database application wmStorer sync;

Pluggable database altered.

SQL>

```
* Create and open the Application Seed PDBs for wmStore_West and sync it with Application wmStore.

```sql
SQL> conn system/oracle@localhost:1524/wmStore_West
Connected.
SQL> 
SQL> create pluggable database  as seed admin user ww_admin identified by oracle;

Pluggable database created.

SQL>
SQL> connect sys/oracle@Localhost:1524/wmStore_West as sysdba
Connected.
SQL> alter pluggable database wmStore_West$Seed open;

Pluggable database altered.
SQL> connect system/oracle@localhost:1524/wmStore_West$Seed;
Connected.
SQL> alter pluggable database application wmStorer sync;

Pluggable database altered.
SQL>

```
* Connect to the wmStore_International Application Root Replica (ARR) and create a database link from that ARR to the CDB of the Master Root.

```sql
SQL> connect system/oracle@localhost:1524/wmStore_International
Connected.
SQL> create public database link DCB1_DBLink connect to system identified by oracle using 'localhost:1523/cdb1';

Database link created.

SQL>

```
* Provision Application PDBs for the UK, Denmark and France franchises.

```sql
SQL> create pluggable database UK admin user ww_amdin identified by oracle;

Pluggable database created.

SQL> Wrote file afiedt.buf

  1* create pluggable database Denmark  admin user ww_amdin identified by oracle
SQL> /

Pluggable database created.

SQL> ed
Wrote file afiedt.buf

  1* create pluggable database France  admin user ww_amdin identified by oracle
SQL> /
Pluggable database created.

SQL>
```
* Connect to the wmStore_West Application Root Replica (ARR) and create a database link from that ARR to the CDB of the Master Root.

```sql
SQL> connect system/oracle@localhost:1524/wmStore_West
Connected.
SQL> create public database link DCB1_DBLink connect to system identified by oracle using 'localhost:1523/cdb1';

Database link created.

SQL> create pluggable database Santa_Monica
admin user wm_admin identified by oracle;
  3  /

Pluggable database created.

SQL> create pluggable database Japan
admin user wm_admin identified by oracle;  2
/

Pluggable database created.

SQL> 
```
* Switch to the container root and open all of the pluggable databases.

```sql
SQL> alter session set container=CDB$ROOT;

Session altered.

SQL> alter pluggable database all open;

Pluggable database altered.

SQL>

```
* Create franchise-specific data.

```sql
SQL> @Franchise_Data_Lab6
....
SQL> -- Products for franchise Santa_Monica


1 row created.

1 row created.

1 row created.

1 row created.

Commit complete.

PL/SQL procedure successfully completed.

SQL>

```


#### Step 7: Durable Location Transparency

```sql

```
#### Step 8: Data Sharing

```sql

```
#### Step Step 9: Application Patches

```sql

```
#### Step 10: DBA Views

```sql
SQL> select system/oracle@localhost:1523/cdb1
SQL> select P.Con_ID             c1
,      P.PDB_Name           c2
,      P.PDB_ID             c3
,      P.CON_UID            c4
,      P.Status             c5
,      P.Application_Root   c6
  2    3    4    5    6    7  ,      P.Application_PDB    c7
,      P.Application_Seed   c8
,      P.Application_Clone  c9
,      P.Is_Proxy_PDB       c10
,      AC.PDB_Name          c11
from DBA_PDBs P
  8    9   10   11   12   13  left outer join DBA_PDBs AC
on AC.Con_ID = P.Application_Root_Con_ID
order by 6 desc
,        9
,        8 desc
 14   15   16   17   18  ,        10 desc
,        7 desc
,        2
,        8
; 19   20   21   22

Sat Sep 12                                                                                                                                                                 page    1
                                                                        Products Visible in Franchise Tulsa

Con ID PDB Name                          Con UID Status     Root? App PDB? Seed? Root Clone? Proxy? App Container Name
------ ------------------------------ ---------- ---------- ----- -------- ----- ----------- ------ ------------------------------
     4 WMSTORE_MASTER                 ########## NORMAL     YES   NO       NO    NO          NO
    14 F2383393305_3_2                ########## NORMAL     YES   YES      NO    YES         NO     WMSTORE_MASTER
     5 WMSTORE_MASTER$SEED            ########## NORMAL     NO    YES      YES   NO          NO     WMSTORE_MASTER
    11 WMSTORE_INTERNATIONAL_PROXY    ########## NORMAL     NO    YES      NO    NO          YES    WMSTORE_MASTER
    12 WMSTORE_WEST_PROXY             ########## NORMAL     NO    YES      NO    NO          YES    WMSTORE_MASTER
     8 CALIFORNIA                     ########## NORMAL     NO    YES      NO    NO          NO     WMSTORE_MASTER
    10 NYC                            ########## NORMAL     NO    YES      NO    NO          NO     WMSTORE_MASTER
     9 TAHOE                          ########## NORMAL     NO    YES      NO    NO          NO     WMSTORE_MASTER
     7 TULSA                          ########## NORMAL     NO    YES      NO    NO          NO     WMSTORE_MASTER
     2 PDB$SEED                       ########## NORMAL     NO    NO       NO    NO          NO
     3 PDB1                           ########## NORMAL     NO    NO       NO    NO          NO
     6 PDB2                           ########## NORMAL     NO    NO       NO    NO          NO

12 rows selected.

SQL>
oracle@workshop multitenant]$ sqlplus /nolog

SQL*Plus: Release 19.0.0.0.0 - Production on Sat Sep 12 14:14:00 2020
Version 19.7.0.0.0

Copyright (c) 1982, 2020, Oracle.  All rights reserved.

SQL> connect system/oracle@localhost:1523/wmStore_Master
Connected.
SQL> column CON_UID               heading "Con UID"          format 9999999999
SQL> column APP_NAME              heading "Application Name" format a20          truncate
SQL> column APP_ID                heading "App ID"           format 99999
column APP_VERSION           heading "Version"          format a7
column APP_VERSION_COMMENT   heading "Comment"          format a50
SQL> SQL> SQL> column APP_STATUS            heading "Status"           format a12
column APP_IMPLICIT          heading "Implicit"         format a8
column APP_CAPTURE_SERVICE   heading "Capture Svc"      format a30
SQL> SQL> SQL> column APP_CAPTURE_MODULE    heading "Capture Mod"      format a15
column PATCH_NUMBER          heading "Patch #"          format 999999
SQL> SQL> column PATCH_MIN_VERSION     heading "Min Vers"         format a8
column PATCH_STATUS          heading "Status"           format a10
SQL> SQL> column PATCH_COMMENT         heading "Comment"          format a50
column ORIGIN_CON_ID         heading "Origin_Con_ID"    format 999999999999
column STATEMENT_ID          heading "Stmt ID"          format 999999
SQL> SQL> SQL> column CAPTURE_TIME          heading "Capture TS"       format a9
SQL> column APP_STATEMENT         heading "SQL Statement"    format a50          truncate
SQL> column ERRORNUM              heading "Error #"          format 999999
SQL> column ERRORMSG              heading "Error Message"    format a50          truncate
column SYNC_TIME             heading "Sync TS"          format a9SQL>
SQL>
SQL> set echo on
SQL> desc DBA_Applications
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 APP_NAME                                           VARCHAR2(128)
 APP_ID                                             NUMBER
 APP_VERSION                                        VARCHAR2(30)
 APP_STATUS                                         VARCHAR2(12)
 APP_IMPLICIT                                       VARCHAR2(1)
 APP_CAPTURE_SERVICE                                VARCHAR2(64)
 APP_CAPTURE_MODULE                                 VARCHAR2(64)
 APP_CAPTURE_ERROR                                  VARCHAR2(1)

SQL> select * from DBA_Applications;

Application Name     App ID Version Status       Implicit
-------------------- ------ ------- ------------ --------
Capture Svc                    Capture Mod     A
------------------------------ --------------- -
APP$AF189E1C34E16076      2 1.0     NORMAL       Y
CDB1                           SQL*Plus        N

WMSTORER                  3 3.0     NORMAL       N
wmstore_master                 SQL*Plus        N

SQL> desc DBA_App_Versions
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 APP_NAME                                           VARCHAR2(128)
 APP_VERSION                                        VARCHAR2(30)
 APP_VERSION_COMMENT                                VARCHAR2(4000)
 APP_VERSION_CHECKSUM                               NUMBER
 APP_ROOT_CLONE_NAME                                VARCHAR2(64)

SQL> desc DBA_App_PDB_Status
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 CON_UID                                            NUMBER
 APP_NAME                                           VARCHAR2(128)
 APP_ID                                             NUMBER
 APP_VERSION                                        VARCHAR2(30)
 APP_STATUS                                         VARCHAR2(12)

SQL> select * from DBA_App_PDB_Status;

    Con UID Application Name     App ID Version Status
----------- -------------------- ------ ------- ------------
 2752621406 WMSTORER                  3 2.0     NORMAL
  353897558 WMSTORER                  3 2.0     NORMAL
 1698289146 WMSTORER                  3 3.0     NORMAL
  186289129 WMSTORER                  3 3.0     NORMAL
 1581866043 WMSTORER                  3 3.0     NORMAL
 2696211975 WMSTORER                  3 2.0     NORMAL
 2430369725 WMSTORER                  3 3.0     NORMAL

7 rows selected.

SQL>

SQL> desc DBA_App_Statements
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 ORIGIN_CON_ID                                      NUMBER
 STATEMENT_ID                              NOT NULL NUMBER
 CAPTURE_TIME                              NOT NULL DATE
 APP_STATEMENT                                      CLOB
 APP_NAME                                           VARCHAR2(128)
 APP_STATUS                                         VARCHAR2(12)
 PATCH_NUMBER                                       NUMBER
 VERSION_NUMBER                                     NUMBER
 SESSION_ID                                         NUMBER
 OPCODE                                    NOT NULL NUMBER

SQL> desc DBA_App_Errors
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 APP_NAME                                           VARCHAR2(128)
 APP_STATEMENT                                      CLOB
 ERRORNUM                                           NUMBER
 ERRORMSG                                           VARCHAR2(4000)
 SYNC_TIME                                 NOT NULL DATE
 SYSTEM_IGNORABLE                                   VARCHAR2(1)
 USER_IGNORABLE                                     VARCHAR2(1)

SQL> select * from DBA_App_Errors;

no rows selected


```

#### Step 11: Diagnosing, Correcting Problems, and Restarting Sync

```sql

```
#### Step 12: Container Map

```sql
SQL> connect system/oracle@localhost:1523/cdb1

create pluggable database Terminal_Master as application container
admin user tc_admin identified by oracle;

alter pluggable database Terminal_Master open;Connected.
SQL> SQL>   2


Pluggable database created.

SQL> SQL>
Pluggable database altered.

SQL> SQL>
SQL>
SQL> connect system/oracle@localhost:1523/Terminal_Master

create pluggable database LHR
admin user tc_admin identified by oracle;

create pluggable database SFO
admin user tc_admin identified by oracle;

create pluggable database JFK
admin user tc_admin identified by oracle;

create pluggable database LAX
admin user tc_admin identified by oracle;

alter session set container=CDB$Root;
alter pluggable database all open;Connected.
SQL> SQL>   2

Pluggable database created.

SQL> SQL>   2

```








