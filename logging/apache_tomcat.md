### apache tomcat logging

### apache tomcat docker 설치
### docker compose 

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   633  100   633    0     0    491      0  0:00:01  0:00:01 --:--:--   491
100 11.6M  100 11.6M    0     0  4916k      0  0:00:02  0:00:02 --:--:-- 19.4M

[opc@oracle-odi-inst-nhsc ~]$ sudo chmod +x /usr/local/bin/docker-compose
[opc@oracle-odi-inst-nhsc ~]$
[opc@oracle-odi-inst-nhsc ~]$ docker-compose --version
docker-compose version 1.27.4, build 40524192
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

### apache tomcat 설치
### oci logging 설정

* tomcat parser

```
<source>
  @type tail
  format multiline
  # Match the date at the beginning of each entry, which can be in one of two
  # different formats.
  format_firstline /^(\w+\s\d+,\s\d+)|(\d+-\d+-\d+\s)/
  format1 /(?<message>.*)/
  multiline_flush_interval 5s
  path /var/log/tomcat*/catalina.out,/var/log/tomcat*/localhost.*.log
  pos_file /var/lib/google-fluentd/pos/tomcat-multiline.pos
  read_from_head true
  tag tomcat
</source>
```
