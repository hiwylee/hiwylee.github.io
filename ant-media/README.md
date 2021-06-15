## ANT Media Server 
### WIKI page
* https://github.com/ant-media/Ant-Media-Server/wiki
 
* https://github.com/ant-media/Ant-Media-Server/releases/download/ams-v2.3.3/ant-media-server-2.3.3-community-2.3.3-20210606_1542.zip
* https://github.com/ant-media/Ant-Media-Server/wiki/Getting-Started

### Ant Media server Installation
* https://github.com/ant-media/Ant-Media-Server/wiki/Clustering-&-Scaling
* https://github.com/ant-media/Ant-Media-Server/wiki/Scaling-and-Load-Balancing

### supported os
* *Ubuntu 18.04, Ubuntu 20.04, Ubuntu 20.10* 
* *Centos 8*

###  Ant Media Server
* [Ant Media Server 유튜브 홈](https://www.youtube.com/c/AntMediaServer/playlists)

### 구성 (AWS 기준: clustgered)
* Orgin server
* Edge Server
* MongoDB

### 초기 패스워드

```
mongo
use serverdb
db.User.find()
```
### 방화벽 열기

```
ubuntu@mysql:/usr/local/antmedia$ sudo iptables  -p tcp -I INPUT --dport 5080 -j ACCEPT
ubuntu@mysql:/usr/local/antmedia$ sudo iptables  -p tcp -I INPUT --dport 1935 -j ACCEPT
ubuntu@mysql:/usr/local/antmedia$ sudo iptables  -p tcp -I INPUT --dport 5443 -j ACCEPT
ubuntu@mysql:/usr/local/antmedia$ sudo iptables  -p tcp -I INPUT --dport 5000:65000 -j ACCEPT
ubuntu@mysql:/usr/local/antmedia$ sudo iptables  -p udp -I INPUT --dport 5000:65000 -j ACCEPT

```

```
ubuntu@mysql:~/ant$ ./install_ant-media-server.sh  -i ant-media-server-2.3.3-community-2.3.3-20210606_1542.zip  -d true

- OpenJDK 11 (openjdk-11-jdk)
- De-archiver (unzip)
- Commons Daemon (jsvc)
- Apache Portable Runtime Library (libapr1)
- SSL Development Files (libssl-dev)
- Video Acceleration (VA) API (libva-drm2)
- Video Acceleration (VA) API - X11 runtime (libva-x11-2)
- Video Decode and Presentation API Library (libvdpau-dev)
- Crystal HD Video Decoder Library (libcrystalhd-dev)

Are you sure that the above packages are installed?  Y/N
```

* We are supporting Ubuntu 18.04, Ubuntu 20.04, Ubuntu 20.10 and Centos 8

```

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.2 LTS
Release:        20.04
Codename:       focal
```

* [Install guide](https://github.com/ant-media/Ant-Media-Server/wiki/Getting-Started)

```
-rw-rw-r-- 1 ubuntu ubuntu 241709345 Jun  7 07:49 ant-media-server-2.3.3-community-2.3.3-20210606_1542.zip
-rwxr-xr-x 1 ubuntu ubuntu     12572 Jun 14 06:36 install_ant-media-server.sh
ubuntu@mysql:~/ant$ sudo ./install_ant-media-server.sh  -i ant-media-server-2.3.3-community-2.3.3-20210606_1542.zip  -d true

- OpenJDK 11 (openjdk-11-jdk)
- De-archiver (unzip)
- Commons Daemon (jsvc)
- Apache Portable Runtime Library (libapr1)
- SSL Development Files (libssl-dev)
- Video Acceleration (VA) API (libva-drm2)
- Video Acceleration (VA) API - X11 runtime (libva-x11-2)
- Video Decode and Presentation API Library (libvdpau-dev)
- Crystal HD Video Decoder Library (libcrystalhd-dev)

Are you sure that the above packages are installed?  Y/N Y

```

```
Open your browser and type http://SERVER_IP_ADDRESS:5080 to go to the web panel. If you're having difficulty in accessing the web panel, there may be a firewall that blocks accessing the 5080 port.

Server Ports
In order to server run properly you need to open some network ports. Here are the ports server uses

TCP:1935 (RTMP)
TCP:5080 (HTTP)
TCP:5443 (HTTPS)
UDP:5000-65000 (WebRTC)
TCP:5000-65000 (You need to open this range in only cluster mode for internal network. It should not be open to public.)
```

* [community version 다운로드](https://github.com/ant-media/Ant-Media-Server/releases/)

### ant media status
* [how to enable SSL](https://www.youtube.com/watch?v=gxkUHyH-WpU)
* status check
*
### ant media server status

```
ubuntu@mysql:/usr/local/antmedia$ sudo service antmedia status
● antmedia.service - Ant Media Server
     Loaded: loaded (/etc/systemd/system/antmedia.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2021-06-14 07:19:24 UTC; 1 day 3h ago
   Main PID: 21297 (java)
      Tasks: 67 (limit: 36000)
     Memory: 574.3M
     CGroup: /system.slice/antmedia.service
             └─21297 /usr/lib/jvm/java-11-openjdk-amd64/bin/java -Dlogback.ContextSelector=org.red5.logging.LoggingContextSelector -cp /usr/local/antmedia/ant-media-server-service.jar:/usr/local/antmedia/conf -Djava.security.debug=f>

Jun 14 07:19:24 mysql systemd[1]: Started Ant Media Server.
ubuntu@mysql:/usr/local/antmedia$ pwd^C
ubuntu@mysql:/usr/local/antmedia$ cd /usr/local/antmedia/
ubuntu@mysql:/usr/local/antmedia$ ls -la
total 7104
drwxr-xr-x  8 antmedia antmedia    4096 Jun 14 07:19 .
drwxr-xr-x 12 root     root        4096 Jun 14 07:19 ..
drwxr-xr-x  3 antmedia antmedia    4096 Jun 14 07:19 .javacpp
-rw-rw-r--  1 antmedia antmedia    9453 Jun  6 15:15 README.md
-rw-rw-r--  1 antmedia antmedia 2265139 Jun  6 15:17 StreamApp-2.3.3.war
-rw-rw-r--  1 antmedia antmedia   14522 Jun  6 15:43 ant-media-server-service.jar
-rw-rw-r--  1 antmedia antmedia  686744 Jun  6 15:43 ant-media-server.jar
-rwxrwxr-x  1 antmedia antmedia    1421 Jun  6 15:15 antmedia
-rw-r--r--  1 antmedia antmedia    1755 Jun  6 15:15 antmedia.service
-rwxr-xr-x  1 antmedia antmedia    1254 Jun  6 15:15 change_server_mode.sh
drwxr-xr-x  2 antmedia antmedia    4096 Jun 14 07:24 conf
-rwxr-xr-x  1 antmedia antmedia    3938 Jun  6 15:15 create_app.sh
-rwxr-xr-x  1 antmedia antmedia    1219 Jun  6 15:15 delete_app.sh
-rwxr-xr-x  1 antmedia antmedia    8175 Jun  6 15:15 enable_ssl.sh
-rwxr-xr-x  1 antmedia antmedia     662 Jun  6 15:15 install_tensorflow_plugin.sh
drwxr-xr-x  3 antmedia antmedia   12288 Jun 14 07:19 lib
-rw-r--r--  1 antmedia antmedia 1048576 Jun 14 07:19 liveapp.db
-rw-r--r--  1 antmedia antmedia 1048576 Jun 14 07:19 liveapp.db.wal.0
lrwxrwxrwx  1 antmedia antmedia      17 Jun 14 07:19 log -> /var/log/antmedia
drwxr-xr-x  2 antmedia antmedia    4096 Jun  6 15:43 plugins
-rwxr-xr-x  1 antmedia antmedia     614 Jun  6 15:15 shutdown.sh
-rw-r--r--  1 antmedia antmedia      36 Jun 14 07:19 shutdown.token
-rwxr-xr-x  1 antmedia antmedia     217 Jun  6 15:15 start-debug.sh
-rwxr-xr-x  1 antmedia antmedia    5906 Jun  6 15:15 start.sh
drwxr-xr-x  5 antmedia antmedia    4096 Jun  6 15:43 webapps
-rw-r--r--  1 antmedia antmedia 1048576 Jun 14 07:19 webrtcapp.db
-rw-r--r--  1 antmedia antmedia 1048576 Jun 14 07:19 webrtcapp.db.wal.0
drwxr-xr-x  3 antmedia antmedia    4096 Jun 14 07:19 work
```

```
