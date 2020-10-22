
####  Using EM Express
### Monitoring a Database << 매뉴얼 참조할 것
* https://docs.cloud.oracle.com/en-us/iaas/Content/Database/Tasks/monitoringDB.htm
* RAC 일때 주의 사항 있음.
* Security list : port (6200,5500,1158)
```
6200 - For Oracle Notification Service (ONS).
5500 - For EM Express. 5500 is the default port
1158 - For Enterprise Manager Database Control. 1158 is the default port.
```
* VM iptable port 열기
```bash
[opc@odi2 .ssh]$ sudo iptables-save > /tmp/iptables-orig
[opc@odi2 .ssh]$ sudo iptables -I INPUT  -p tcp -m state --state NEW -m tcp --dport 5500 -j ACCEPT -m comme                                            nt --comment "Required for EM Express."
[opc@odi2 .ssh]$
[opc@odi2 .ssh]$
[opc@odi2 .ssh]$ sudo service iptables status
Redirecting to /bin/systemctl status iptables.service
● iptables.service - IPv4 firewall with iptables
   Loaded: loaded (/usr/lib/systemd/system/iptables.service; enabled; vendor preset: disabled)
   Active: active (exited) since Tue 2020-10-20 23:25:17 KST; 1 day 12h ago
 Main PID: 1045 (code=exited, status=0/SUCCESS)
   CGroup: /system.slice/iptables.service

Oct 20 23:25:17 localhost systemd[1]: Starting IPv4 firewall with iptables...
Oct 20 23:25:17 localhost iptables.init[1045]: iptables: Applying firewall rules: [  OK  ]
Oct 20 23:25:17 localhost systemd[1]: Started IPv4 firewall with iptables.

[opc@odi2 .ssh]$ sudo  /sbin/service iptables save
iptables: Saving firewall rules to /etc/sysconfig/iptables:[  OK  ]

```

```
$ . oraenv
ORACLE_SID = [oracle] ? orcl
The Oracle base has been set to /scratch/u01/app/oracle
$ sqlplus / as sysdba

SQL*Plus: Release 19.0.0.0.0 - Production on Wed Mar 25 00:54:43 2019
Version 19.3.0.0.0

Copyright (c) 1982, 2019, Oracle.  All rights reserved.

Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.3.0.0.0

SQL>  

$ SQL> alter session set container orclpdb;

Session altered.
SQL> alter pluggable database orclpdb open;

Pluggable database altered.
SQL>  SELECT dbms_xdb_config.gethttpsport() from dual; 

DBMS_XDB_CONFIG.GETHTTPSPORT()
------------------------------
5502


```
https://apexapps.oracle.com/pls/apex/f?p=44785:52:2979035488864:::52:P52_CONTENT_ID,P52_MODULE_ID,P52_ACTIVITY_ID,P52_EVENT_ID:26500,4219,19645,6362
