### apache tomcat logging

### apache tomcat docker 설치
### docker compose 

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
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


* docker-compose  기본 명령어
``` 
#도커 컨테이너 기동
docker-compose up -d

#도커 컨테이너 기동 ( 배포 후 빌드 / Dokcerfile 필수)
docker-compose up -d --build

#도커 컨테이너 종료
docker-compose stop

#도커 특정 컨테이너 접근
docker-compose -i -t <컨테이너명> /bin/bash

#도커 이미지 검색
docker search <이미지명>

#도커 실행중인 컨테이너 목록
docker ps
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
