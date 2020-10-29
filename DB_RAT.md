## Real Application Testing (RAT)
### Real Application Testing (It's not RAC !)
* [Real Application Testing: Step by Step](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/ntdbi/enabling-and-disabling-database-options-after-installation.html#GUID-C45D75FC-34B5-4C24-9DE8-1518044A3BB3)
* [NOTE:445116.1](https://support.oracle.com/epmos/faces/DocumentDisplay?parent=DOCUMENT&sourceId=742645.1&id=445116.1) - Using Workload Capture and Replay
* Capture SIze Estimation 
 * AWR report : ``bytes received via SQL*Net from client * 2``
* Overhead : The main overhead is from the ``writing of the capture files``. It is about ``4% to 5%``
* 여러번 반복 replay : Flashback 
### 	Database Testing: Best Practices (Doc ID 1535885.1)
* [	Database Testing: Best Practices (Doc ID 1535885.1)](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=431673761627791&parent=DOCUMENT&sourceId=1268920.1&id=1535885.1&_afrWindowMode=0&_adf.ctrl-state=imgk5degr_293)
### Real Application Testing (RAT): Recommended White Papers (Doc ID 1546337.1)
* [Doc ID 1268920.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=431505447515009&id=1268920.1&displayIndex=8&_afrWindowMode=0&_adf.ctrl-state=imgk5degr_176)
### Real Application Testing: How to Run Workload Analyzer (Doc ID 1268920.1)	 
* [Doc ID 1268920.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=431505447515009&id=1268920.1&displayIndex=8&_afrWindowMode=0&_adf.ctrl-state=imgk5degr_176)
### Database Replay: Command Line Interface (CLI) Usage Examples and Scripts (Doc ID 742645.1)
* [Doc ID 742645.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=253257074406430&parent=EXTERNAL_SEARCH&sourceId=HOWTO&id=742645.1&_afrWindowMode=0&_adf.ctrl-state=hhpe3qlm4_4)
  * [Click Here to download the scripts and README](https://support.oracle.com/epmos/main/downloadattachmentprocessor?parent=DOCUMENT&sourceId=742645.1&attachid=742645.1:db_replay_cli&clickstream=yes)

### Using Workload Capture and Replay (Doc ID 445116.1)
* [NOTE:445116.1](https://support.oracle.com/epmos/faces/DocumentDisplay?parent=DOCUMENT&sourceId=742645.1&id=445116.1) - Using Workload Capture and Replay
* [NOTE:463263.1](https://support.oracle.com/epmos/faces/DocumentDisplay?parent=DOCUMENT&sourceId=742645.1&id=463263.1) - Database Capture and Replay: Common Errors and Reasons
* [NOTE:560977.1](https://support.oracle.com/epmos/faces/DocumentDisplay?parent=DOCUMENT&sourceId=742645.1&id=560977.1) - Mandatory Patches for Database Testing Functionality for Current and Earlier Releases

### Guide
* https://www.oracle.com/technetwork/articles/oem/298770-132432.pdf
* [Testing Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/ratug/testing-guide.pdf)

### Test SQL

```sql
create table gark(
id number primary key,
name varchar2(25) not null,
value number,
description varchar2(250)
default 'Don''t tables to create sequenced values');

create index gark_uk on gark(name);

insert into gark(id, name, value)
values (1,'GARK_SQ1', 1);

commit;
0. 
create or replace function
get_nextval(p_name varchar2)
return number is
v_return number;
begin
lock table gark in exclusive mode;

select value into v_return
from gark where name=p_name;

update gark
set value=value+1
where name=p_name;

commit;

return v_return;
end;
/

1. 
begin
dbms_workload_capture.add_filter(
fname=>'gark_filter1',
fattribute=>'USER',
fvalue=>'ARKZOYD');
end;
/
2. 
col type format a10
col id format 999
col status format a6
col name format a15
col attribute format a20
col value format a20
select *
from DBA_WORKLOAD_FILTERS;
3. 
create directory capture_dir
as '/home/oracle/rat';   - rac shared volumn

4. 
BEGIN
DBMS_WORKLOAD_CAPTURE.START_CAPTURE (
name            => 'gark_capture',
dir             => 'CAPTURE_DIR',
duration        => null,
default_action  => 'INCLUDE'
);
END;
/

5. 
col id format 99
col NAME format a12
col DIRECTORY format a12
col ACTION format a10
col FILTS format 99
col CSIZ format 99999
col TRANS format 9999
select ID,
NAME,
DIRECTORY,
DEFAULT_ACTION ACTION,
FILTERS_USED FILS,
CAPTURE_SIZE CSIZE,
TRANSACTIONS TRANS
from DBA_WORKLOAD_CAPTURES;

 ID NAME         DIRECTORY    ACTION           FILS      CSIZE TRANS
--- ------------ ------------ ---------- ---------- ---------- -----
  3 gark_capture CAPTURE_DIR  INCLUDE             1      28796     0

declare
v_out number;
begin
for i in 1..30000 loop
v_out:=get_nextval('GARK_SQ1' );
end loop;
end;
/

6.
BEGIN
DBMS_WORKLOAD_CAPTURE.FINISH_CAPTURE (
timeout => 0,
Reason  => 'Capture finished OK');
END;
/

col id format 99
col NAME format a12
col status format a12
col CSIZ format 99999
col TRANS format 999999
select ID,
NAME,
STATUS,
CAPTURE_SIZE CSIZE,
TRANSACTIONS TRANS
from DBA_WORKLOAD_CAPTURES;

col id format 99
col NAME format a12
col status format a12
col CSIZ format 99999
col TRANS format 999999
select ID,
NAME,
STATUS,
CAPTURE_SIZE CSIZE,
TRANSACTIONS TRANS
from DBA_WORKLOAD_CAPTURES;



//////
DECLARE
cap_id  NUMBER;
cap_rpt CLOB;
fh      UTL_FILE.FILE_TYPE;
buffer  VARCHAR2(32767);
amount  BINARY_INTEGER;
offset  NUMBER(38);
BEGIN
cap_id := DBMS_WORKLOAD_CAPTURE.GET_CAPTURE_INFO(
dir => 'CAPTURE_DIR');

cap_rpt := DBMS_WORKLOAD_CAPTURE.REPORT(
capture_id => cap_id,
format     => DBMS_WORKLOAD_CAPTURE.TYPE_HTML);

fh := UTL_FILE.FOPEN(
location     => '&db_directory',
filename     => '&report_name',
open_mode    => 'w',
max_linesize => 32767);

amount := 32767;
offset := 1;

WHILE amount >= 32767 LOOP
DBMS_LOB.READ(
lob_loc => cap_rpt,
amount  => amount,
offset  => offset,
buffer  => buffer);

offset := offset + amount;

UTL_FILE.PUT(
file   => fh,
buffer => buffer);

UTL_FILE.FFLUSH(file => fh);
END LOOP;
UTL_FILE.FCLOSE(file => fh);
END;
/

////////////
select id,name,status,start_time,end_time,connects,user_calls,dir_path from dba_workload_captures where id = (select max(id) from dba_workload_captures);
 ID NAME         STATUS       START_TIM END_TIME    CONNECTS USER_CALLS
--- ------------ ------------ --------- --------- ---------- ----------
DIR_PATH
--------------------------------------------------------------------------------
  3 gark_capture COMPLETED    29-OCT-20 29-OCT-20         25        243
/home/oracle/rat


//
begin
DBMS_WORKLOAD_REPLAY.PROCESS_CAPTURE (
capture_dir =>'CAPTURE_DIR');
end;
/


BEGIN
DBMS_WORKLOAD_REPLAY.INITIALIZE_REPLAY (
replay_name => 'GREPLAY1',
replay_dir  => 'CAPTURE_DIR');
END;
/
col id format 99
col name format a8
col dir format a12
col status format a11
col secs format 9999
col cli format 99
col sync format a5
select id,
name,
DIRECTORY dir,
STATUS,
DURATION_SECS secs,
NUM_CLIENTS cli,
SYNCHRONIZATION sync
from dba_workload_replays;

ol CONN_ID format 99
col ORIG format a30 wor wra
col NEW format a30 wor wra
select CONN_ID,
substr(CAPTURE_CONN, 1, 30) ORIG,
substr(REPLAY_CONN,1,30) NEW
from DBA_WORKLOAD_CONNECTION_MAP
where replay_id=&REPLAY_ID;

BEGIN
DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY (
synchronization => TRUE);
END;
/

wrc system/WelC0me1## mode=calibrate  replaydir=/home/oracle/rat


wrc system/WelC0me1## mode=replay replaydir=/home/oracle/rat

BEGIN
DBMS_WORKLOAD_REPLAY.START_REPLAY ();
END;
/
col id format 99
col name format a8
col dir format a12
col status format a11
col secs format 9999
col cli format 99
col sync format a5
select id,
name,
to_char(sysdate,'DD/MM/YYYY HH24:MI:SS') SYS_DATE,
to_char(start_time,'DD/MM/YYYY HH24:MI:SS') START_DATE,
to_char(END_time,'DD/MM/YYYY HH24:MI:SS') END_DATE,
STATUS,
DURATION_SECS secs,
NUM_CLIENTS cli,
SYNCHRONIZATION sync
from dba_workload_replays
where id=&REPLAY_ID;



select DBMS_WORKLOAD_REPLAY.REPORT(
replay_id => 1,
format    => 'TEXT') as report from dual
/
~


BEGIN
DBMS_WORKLOAD_CAPTURE.DELETE_CAPTURE_INFO (
capture_id=>&capture_id);
END;
/


BEGIN
DBMS_WORKLOAD_REPLAY.DELETE_REPLAY_INFO(
REPLAY_ID=>&replay_id);
END;
/

begin
DBMS_WORKLOAD_REPLAY.cancel_replay(
'Replay Terminated by Cancel');
end;
/
```
