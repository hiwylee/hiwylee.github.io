### Log 발생량 확인

1 현재 설정된 로그 파일 크기'

```sql
SQL> SELECT GROUP#, BLOCKSIZE, STATUS, MEMBERS, BYTES / (1024 * 1024) AS Size_MB FROM v$log;

    GROUP#  BLOCKSIZE STATUS		  MEMBERS    SIZE_MB
---------- ---------- ---------------- ---------- ----------
	 1	  512 INACTIVE			1	 200
	 2	  512 INACTIVE			1	 200
	 3	  512 CURRENT			1	 200

```

2 Check the frequency of the log switches and determine if they are occurring too often.
  * 15 to 30 minutes , maximum 4 times per hour. 

```sql
SELECT Start_Date, Start_Time, Num_Logs,
Round(Num_Logs * (Vl.Bytes / (1024 * 1024)), 2) AS Mbytes, Vdb.NAME AS Dbname FROM (SELECT To_Char(Vlh.First_Time, 'YYYY-MM-DD') AS Start_Date, To_Char(Vlh.First_Time, 'HH24') || ':00' AS Start_Time, COUNT(Vlh.Thread#) Num_Logs
FROM V$log_History Vlh GROUP BY To_Char(Vlh.First_Time, 'YYYY-MM-DD'), To_Char(Vlh.First_Time, 'HH24') || ':00') Log_Hist, V$log Vl, V$database Vdb WHERE Vl.Group# = 1
ORDER BY Log_Hist.Start_Date,log_Hist.Start_Time;
START_DATE START   NUM_LOGS	MBYTES DBNAME
---------- ----- ---------- ---------- ---------
2021-09-14 05:00	  1	   200 ORCL
2021-10-18 12:00	  4	   800 ORCL
2021-10-18 13:00	  5	  1000 ORCL
2021-10-18 14:00	  4	   800 ORCL

```
