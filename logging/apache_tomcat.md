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

 ```
 cd https://tomcat.apache.org/download-80.cgi
 wget https://mirror.navercorp.com/apache/tomcat/tomcat-8/v8.5.68/bin/apache-tomcat-8.5.68.tar.gz
 [root@oracle-odi-inst-nhsc tomcat]# mv apache-tomcat-8.5.68 apache-tomcat-8.5.59
[root@oracle-odi-inst-nhsc tomcat]#  mv apache-tomcat-8.5.59 /usr/local/lib
[root@oracle-odi-inst-nhsc tomcat]#

```

```
JAVA_HOME=/u01/oracle/jdk1.8.0_211/
JRE_HOME=/u01/oracle/jdk1.8.0_211/
CATALINA_HOME=/usr/local/lib/apache-tomcat-8.5.59
CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$CATALINA_HOME/lib/jsp-api.jar:$CATALINA_HOME/lib/servlet-api.jar
PATH=$PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin
export JAVA_HOME JRE_HOME CLASSPATH PATH CATALINA_HOME
```



* https://github.com/maeharin/apache-tomcat-docker-sample

* sample download
```
sudo yun install git -y
[opc@oracle-odi-inst-nhsc ~]$ git clone https://github.com/maeharin/apache-tomcat-docker-sample.git
Cloning into 'apache-tomcat-docker-sample'...
remote: Enumerating objects: 26, done.
remote: Total 26 (delta 0), reused 0 (delta 0), pack-reused 26
Unpacking objects: 100% (26/26), done.
[opc@oracle-odi-inst-nhsc ~]$ cd apache-tomcat-docker-sample/

```



* docker/httpd/Dockerfile 에 tomcat 이미지 위치 수정
   -> https://archive.apache.org/dist/tomcat/tomcat-connectors/jk/tomcat-connectors-1.2.48-src.tar.gz
``` 

docker-compose up -d

....
```

### oci logging 설정

* unified-monitoring
 
```
unified-monitoring-agent.service
unified-monitoring-agent_config_downloader.service
unified-monitoring-agent_config_downloader.timer
unified-monitoring-agent_restarter.path

```

```
/etc/unified-monitoring-agent/unified-monitoring-agent.conf
```

```
/var/log/unified-monitoring-agent/unified-monitoring-agent.log
```

* log 위치
  * /var/log/httpd/access_log
  * /var/log/httpd/error_log
  * /usr/local/lib/apache-tomcat-8.5.59/logs
  
```
-rw-r-----. 1 opc opc 18943 Jun 18 13:43 catalina.2021-06-18.log
-rw-r-----. 1 opc opc 18943 Jun 18 13:43 catalina.out
-rw-r-----. 1 opc opc     0 Jun 18 12:53 host-manager.2021-06-18.log
-rw-r-----. 1 opc opc  1193 Jun 18 13:43 localhost.2021-06-18.log
-rw-r-----. 1 opc opc     0 Jun 18 12:53 localhost_access_log.2021-06-18.txt
-rw-r-----. 1 opc opc     0 Jun 18 12:53 manager.2021-06-18.log

```
* tomcat parser
  * /var/log/httpd/access_log 
  * /var/log/httpd/error_log
  * /usr/local/lib/apache-tomcat-*/logs/catalina.out
  * /usr/local/lib/apache-tomcat-*/logs/localhost*.log


### OCI unified monitoring agent
### 반드시 참조해야 될 멀티라인 관련 설정
  * https://programmersought.com/article/22991207977/
   
* end point
  * https://auth.ap-seoul-1.oraclecloud.com
  * https://ingestion.logging.ap-seoul-1.oci.oraclecloud.com
* agent

```
sudo systemctl restart  unified-monitoring-agent.service
```

* log : /var/log/unified-monitoring-agent/unified-monitoring-agent.log 
* config : /etc/unified-monitoring-agent/conf.d/fluentd_config/fluentd.conf

* tomcat log
*
```

20-Jun-2021 17:47:20.990 SEVERE [main] org.apache.catalina.core.StandardServer.await StandardServer.await: create[localhost:8005]:
        java.net.BindException: Address already in use (Bind failed)
                at java.net.PlainSocketImpl.socketBind(Native Method)
                at java.net.AbstractPlainSocketImpl.bind(AbstractPlainSocketImpl.java:387)
                at java.net.ServerSocket.bind(ServerSocket.java:375)
                at java.net.ServerSocket.<init>(ServerSocket.java:237)
                at org.apache.catalina.core.StandardServer.await(StandardServer.java:422)
                at org.apache.catalina.startup.Catalina.await(Catalina.java:776)
                at org.apache.catalina.startup.Catalina.start(Catalina.java:722)
                at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
                at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
                at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                at java.lang.reflect.Method.invoke(Method.java:498)
                at org.apache.catalina.startup.Bootstrap.start(Bootstrap.java:345)
                at org.apache.catalina.startup.Bootstrap.main(Bootstrap.java:476)
20-Jun-2021 17:47:20.990 INFO [main] org.apache.coyote.AbstractProtocol.pause Pausing ProtocolHandler ["http-nio-8080"]
20-Jun-2021 17:47:20.991 INFO [main] org.apache.coyote.AbstractProtocol.pause Pausing ProtocolHandler ["ajp-nio-127.0.0.1-9009"]
20-Jun-2021 17:47:20.991 INFO [main] org.apache.catalina.core.StandardService.stopInternal Stopping service [Catalina]
20-Jun-2021 17:47:21.009 INFO [main] org.apache.coyote.AbstractProtocol.stop Stopping ProtocolHandler ["http-nio-8080"]
20-Jun-2021 17:47:21.011 INFO [main] org.apache.coyote.AbstractProtocol.destroy Destroying ProtocolHandler ["http-nio-8080"]
20-Jun-2021 17:47:21.011 INFO [main] org.apache.coyote.AbstractProtocol.stop Stopping ProtocolHandler ["ajp-nio-127.0.0.1-9009"]
20-Jun-2021 17:47:21.011 INFO [main] org.apache.coyote.AbstractProtocol.destroy Destroying ProtocolHandler ["ajp-nio-127.0.0.1-9009"]
```

###  Unified Monitoring : tomcat 용 fluentd.conf
* 
```
    <source>
        @type tail
        tag 727561.tomcat_log_cfg_input
        path  /usr/local/lib/apache-tomcat-*/logs/catalina.out
        pos_file  /etc/unifiedmonitoringagent/pos/727561-tomcat_log_cfg_input.pos
        path_key  tailed_path
        <parse>
            @type multiline
            format1  /^(?<datetime>[0-9]{2}-[A-Za-z]{3}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3} |^\s+)(?<message>.*)$/
            format_firstline  /[0-9]{2}-[A-Za-z]{3}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3} [A-Z]* ?.*/
        </parse>
    </source>

    <match 727561.**>
        @type oci_logging
        log_object_id  ocid1.log.oc1.ap-seoul-1.amaaaaaaaiz7opyafqogtoswk3cq7kpcpgn2srsishn6j475rx2umpdlrsza
        <buffer tag>
            @type file
            retry_timeout  3h
            path  /opt/unifiedmonitoringagent/run/buffer/727561
            disable_chunk_backup  true
            chunk_limit_size  5MB
            flush_interval  180s
            total_limit_size  1GB
            overflow_action  throw_exception
            retry_type  exponential_backoff
        </buffer>
    </match>

```
* 모두 보이는 패턴
```
| 를 이용하여 
grep -E '^(?[0-9]{2}-[A-Za-z]{3}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3} [A-Z]*|^\s+)' ../logs/catalina.out

```
 

* ``테스트 필요 2 (성공함)`` 
  * 에러메세지 
```
2021-06-20 15:56:45 +0000 [warn]: #0 pattern not matched: "20-Jun-2021 15:54:38.891 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in 571 ms"
2021-06-20 15:56:45 +0000 [warn]: #0 pattern not matched: "20-Jun-2021 15:56:45.450 INFO [main] org.apache.catalina.core.StandardServer.await A valid shutdown command was received via the shutdown port. Stopping the Server instance."
```

  * ``해결을 위한 설정`` 
  

```
  format1 /^(?<datetime>[0-9]{2}-[A-Za-z]{3}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3} |^\s+)(?<message>.*)$/
  format_firstline "/[0-9]{2}-[A-Za-z]{3}-[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3} [A-Z]* ?.*/"

```
* 로그 확인 
* ![image](https://user-images.githubusercontent.com/7068088/122684432-4f977d00-d240-11eb-9c99-6e87c6a9b977.png)
* ![image](https://user-images.githubusercontent.com/7068088/122684435-53c39a80-d240-11eb-9b0e-1e6c0530168d.png)

* 로그예제 - 톰캣 멀티라인 로그 수집

```
..
{
  "datetime": "20-Jun-2021 18:03:41.189 ",
  "message": "SEVERE [main] org.apache.catalina.core.StandardServer.await StandardServer.await: create[localhost:8005]: \n\tjava.net.BindException: Address already in use (Bind failed)\n\t\tat java.net.PlainSocketImpl.socketBind(Native Method)\n\t\tat java.net.AbstractPlainSocketImpl.bind(AbstractPlainSocketImpl.java:387)\n\t\tat java.net.ServerSocket.bind(ServerSocket.java:375)\n\t\tat java.net.ServerSocket.<init>(ServerSocket.java:237)\n\t\tat org.apache.catalina.core.StandardServer.await(StandardServer.java:422)\n\t\tat org.apache.catalina.startup.Catalina.await(Catalina.java:776)\n\t\tat org.apache.catalina.startup.Catalina.start(Catalina.java:722)\n\t\tat sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\n\t\tat sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)\n\t\tat sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\n\t\tat java.lang.reflect.Method.invoke(Method.java:498)\n\t\tat org.apache.catalina.startup.Bootstrap.start(Bootstrap.java:345)\n\t\tat org.apache.catalina.startup.Bootstrap.main(Bootstrap.java:476)",
  "tailed_path": "/usr/local/lib/apache-tomcat-8.5.59/logs/catalina.out"
}
...
```



### apache start 실패시

* journalctl -xe
  
```
[opc@oracle-odi-inst-nhsc httpd]$ journalctl -xe
-- Defined-By: systemd
-- Support: http://lists.freedesktop.org/mailman/listinfo/systemd-devel
--
-- Unit httpd.service has begun starting up.
Jun 18 13:27:39 oracle-odi-inst-nhsc kernel: xfs filesystem being remounted at /tmp supports timestamps until 2038 (0x7fffffff)
Jun 18 13:27:39 oracle-odi-inst-nhsc kernel: xfs filesystem being remounted at /var/tmp supports timestamps until 2038 (0x7fffff
Jun 18 13:27:39 oracle-odi-inst-nhsc systemd[1]: httpd.service: main process exited, code=exited, status=1/FAILURE
Jun 18 13:27:39 oracle-odi-inst-nhsc systemd[1]: Failed to start The Apache HTTP Server.
-- Subject: Unit httpd.service has failed
-- Defined-By: systemd
-- Support: http://lists.freedesktop.org/mailman/listinfo/systemd-devel
--
-- Unit httpd.service has failed.
--
-- The result is failed.
Jun 18 13:27:39 oracle-odi-inst-nhsc systemd[1]: Unit httpd.service entered failed state.
Jun 18 13:27:39 oracle-odi-inst-nhsc systemd[1]: httpd.service failed.
Jun 18 13:27:39 oracle-odi-inst-nhsc polkitd[1624]: Unregistered Authentication Agent for unix-process:12418:194241643 (system b
Jun 18 13:27:39 oracle-odi-inst-nhsc sudo[12414]: pam_unix(sudo:session): session closed for user root
Jun 18 13:27:42 oracle-odi-inst-nhsc setroubleshoot[12404]: SELinux is preventing httpd from write access on the file /var/log/h
Jun 18 13:27:42 oracle-odi-inst-nhsc python[12404]: SELinux is preventing httpd from write access on the file /var/log/httpd/mod

                                                    *****  Plugin catchall (100. confidence) suggests   ************************

                                                    If you believe that httpd should be allowed write access on the mod_jk.shm.1
                                                    Then you should report this as a bug.
                                                    You can generate a local policy module to allow this access.
                                                    Do
                                                    allow this access for now by executing:
                                                    # ausearch -c 'httpd' --raw | audit2allow -M my-httpd

```

```
[opc@oracle-odi-inst-nhsc httpd]$ sudo ausearch -c 'httpd' --raw | audit2allow -M my-httpd
******************** IMPORTANT ***********************
To make this policy package active, execute:

semodule -i my-httpd.pp

[opc@oracle-odi-inst-nhsc httpd]$ sudo  semodule -i my-httpd.pp

[opc@oracle-odi-inst-nhsc httpd]$
[opc@oracle-odi-inst-nhsc httpd]$

```
