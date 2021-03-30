## run time stats
###

```sql
select 'STAT...' || a.name name, b.value
   from v$statname a, v$mystat b
   where a.statistic# = b.statistic#
   union all
   select 'LATCH.' || name,  gets
      from v$latch
     union all
     select 'STAT...Elapsed Time', hsecs from v$timer

SYS@//rac-scan.subnet1.labvcn.oraclevcn.com/unisrv.subnet1.labvcn.oraclevcn.com> /

NAME                                                                                  VALUE
-------------------------------------------------------------------------------- ----------
STAT...OS CPU Qt wait time                                                                0
STAT...Requests to/from client                                                            7
STAT...logons cumulative                                                                  1
STAT...logons current                                                                     1
STAT...opened cursors cumulative                                                        145
STAT...opened cursors current                                                             1
STAT...user commits                                                                       0
STAT...user rollbacks                                                                     0
STAT...user calls                                                                         9
STAT...recursive calls                                                                  307
STAT...recursive cpu usage                                                                3
STAT...pinned cursors current                                                             1
STAT...user logons cumulative                                                             1
STAT...user logouts cumulative                                                            0
STAT...session logical reads                                                            361
STAT...session logical reads in local numa group                                          0
STAT...session logical reads in remote numa group                                         0
STAT...session stored procedure space                                                     0
STAT...CPU used when call started                                                        49
STAT...CPU used by this session                                                          49
STAT...DB time                                                                           99
STAT...session uga memory                                                           1962728
STAT...session uga memory max                                                       2155312
STAT...messages sent                                                                      0
STAT...messages received                                                                  0
STAT...background timeouts                                                                0
STAT...remote Oradebug requests                                                           0
STAT...session pga memory                                                           4854168
STAT...session pga memory max                                                       6164888
.....
TCH.quarantine object                                                                 785
LATCH.quarantine region                                                                   0
LATCH.undo global data                                                                29503
LATCH.Change Notification Hash table latch                                               33
LATCH.Change Notification Latch                                                           0
LATCH.flashback archiver latch                                                            2
LATCH.change notification client cache latch                                             16
LATCH.ILM activity tracking latch                                                        16
LATCH.ILM Stats main anchor latch                                                      2285
LATCH.ILM Stats Stripe Latch                                                             16
LATCH.GDID metadata structure latch                                                       0
LATCH.IM Global dictionary queue latch                                                   16
LATCH.KZIC Latch                                                                          0
LATCH.test generic pdb                                                                    0
LATCH.test generic open                                                                   0
LATCH.Result Cache: RC Latch                                                            380
LATCH.kexsv SC latch                                                                      0
LATCH.jslv pdb context latch                                                            119
STAT...Elapsed Time                                                              1802203589


```

```sql
create global temporary table run_stats
( runid varchar2(15),
  name varchar2(80),
  value int )
on commit preserve rows;

create or replace view stats
as select 'STAT...' || a.name name, b.value
   from v$statname a, v$mystat b
   where a.statistic# = b.statistic#
   union all
   select 'LATCH.' || name,  gets
      from v$latch
     union all
     select 'STAT...Elapsed Time', hsecs from v$timer;


create or replace package runstats_pkg
as
   procedure rs_start;
   procedure rs_middle;
   procedure rs_stop( p_difference_threshold in number default 0 );
end;
/

create or replace package body runstats_pkg
as

g_start number;
g_run1  number;
g_run2  number;

procedure rs_start
is
  begin
  delete from run_stats;

  insert into run_stats
  select 'before', stats.* from stats;

  g_start := dbms_utility.get_time;
end;

procedure rs_middle
is
  begin
  g_run1 := (dbms_utility.get_time-g_start);

  insert into run_stats
  select 'after 1', stats.* from stats;
  g_start := dbms_utility.get_time;
end;

procedure rs_stop(p_difference_threshold in number default 0)
is
 begin
 g_run2 := (dbms_utility.get_time-g_start);

 dbms_output.put_line ( 'Run1 ran in ' || g_run1 || ' hsecs' );
 dbms_output.put_line  ( 'Run2 ran in ' || g_run2 || ' hsecs' );
 dbms_output.put_line  ( 'run 1 ran in ' || round(g_run1/g_run2*100,2) || '% of the time' );
 dbms_output.put_line( chr(9) );

 insert into run_stats select 'after 2', stats.* from stats;

 dbms_output.put_line ( rpad( 'Name', 30 ) || lpad( 'Run1', 12 ) || lpad( 'Run2', 12 ) || lpad( 'Diff', 12 ) );

 for x in
   ( select rpad( a.name, 30 ) ||
         to_char( b.value-a.value, '999,999,999' ) ||
         to_char( c.value-b.value, '999,999,999' ) ||
         to_char( ( (c.value-b.value)-(b.value-a.value)), '999,999,999' ) data
     from run_stats a, run_stats b, run_stats c
     where a.name = b.name
     and b.name = c.name
     and a.runid = 'before'
     and b.runid = 'after 1'
     and c.runid = 'after 2'
     -- and (c.value-a.value) > 0
     and abs( (c.value-b.value) - (b.value-a.value) ) > p_difference_threshold
    order by abs( (c.value-b.value)-(b.value-a.value))
   ) loop
      dbms_output.put_line( x.data );
   end loop;

 dbms_output.put_line( chr(9) );
 dbms_output.put_line ( 'Run1 latches total versus runs -- difference and pct' );
 dbms_output.put_line ( lpad( 'Run1', 12 ) || lpad( 'Run2', 12 ) || lpad( 'Diff', 12 ) || lpad( 'Pct', 10 ) );

 for x in
   ( select to_char( run1, '999,999,999' ) ||
         to_char( run2, '999,999,999' ) ||
         to_char( diff, '999,999,999' ) ||
         to_char( round( run1/run2*100,2 ), '99,999.99' ) || '%' data
    from ( select sum(b.value-a.value) run1, sum(c.value-b.value) run2,
                  sum( (c.value-b.value)-(b.value-a.value)) diff
             from run_stats a, run_stats b, run_stats c
            where a.name = b.name
              and b.name = c.name
              and a.runid = 'before'
              and b.runid = 'after 1'
              and c.runid = 'after 2'
              and a.name like 'LATCH%'
            )
     ) loop
        dbms_output.put_line( x.data );
     end loop;
 end;
end;
/```
