## Real-Time Statistics in Oracle Database 19c
* https://oracle-base.com/articles/19c/real-time-statistics-19c
## 
* exdata 흉내내기 : "_exadata_feature_on"=true
```sql
sqlplus / as sysdba <<EOF

alter system set "_exadata_feature_on"=true scope=spfile;
shutdown immediate;
startup;

exit;
EOF
```
*  _exadata_feature_on 
```sql
sqlplus / as sysdba <<EOF

alter system reset "_exadata_feature_on" scope=spfile;
shutdown immediate;
startup;

exit;
EOF
```
