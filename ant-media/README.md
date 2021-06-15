## ANT Media Server 
* [WiKI](https://github.com/ant-media/Ant-Media-Server/wiki)

* Home Page
  * Test URL : [http://146.56.167.42:5080/](http://146.56.167.42:5080/) or [http://myorcl.tk:5080/](http://myorcl.tk:5080)
  * [freenom.com](https://www.freenom.com/) user: hiwylee 에서 myorcl.tk 등록 :  [https://146.56.167.42:5443/](https://146.56.167.42:5443/) or  [https://myorcl.tk:5443/](https://myorcl.tk:5443)
* WebRTC
  * CE publish: [https://146.56.167.42:5443/WebRTCApp](https://146.56.167.42:5443/WebRTCApp) <-> CE play :  [https://146.56.167.42:5443/WebRTCApp/player.html](https://152.67.208.179:5443/WebRTCApp/player.html)
  * EE : https://146.56.167.42:5443/WebRTCAppEE 
* Live Stream Demo
  * https://github.com/ant-media/utilities 사용 /home/ubuntu/ant/utilities/   
  * [테스트 영상](https://myorcl.tk:5443/LiveApp/play.html?name=071278547887943360407523) : tps://myorcl.tk:5443/LiveApp/play.html?name=071278547887943360407523](https://myorcl.tk:5443/LiveApp/play.html?name=071278547887943360407523)
### S/W 설치 
* 주의사항 : 반드시 아래 버전을 사용해야 함 : 2.3.3 은 안됨.
 * [``ant-media-server-2.3.2-community-2.3.2-20210422_0754.zip`` ](https://github.com/ant-media/Ant-Media-Server/releases/download/ams-v2.3.2/ant-media-server-2.3.2-community-2.3.2-20210422_0754.zip)

```
wget https://github.com/ant-media/Ant-Media-Server/releases/download/ams-v2.3.2/ant-media-server-2.3.2-community-2.3.2-20210422_0754.zip
wget https://raw.githubusercontent.com/ant-media/Scripts/master/install_ant-media-server.sh && chmod 755 install_ant-media-server.sh
./install_ant-media-server.sh  -i ant-media-server-2.3.2-community-2.3.2-20210422_0754.zip

```
### 방화벽 열기
* Port List
```
TCP:1935 (RTMP)
TCP:5080 (HTTP)
TCP:5443 (HTTPS)
UDP:5000-65000 (WebRTC)
TCP:5000-65000 (You need to open this range in only cluster mode for internal network. It should not be open to public.)
```
 
* cloud (OCI) : VCN ingress rule (ssl enable 하려면 80 port open 필수)
* ![image](https://user-images.githubusercontent.com/7068088/122059366-82e4a100-ce27-11eb-80e3-20f16fdfb97e.png)
* ubuntu O/S : iptables

```
sudo iptables  -p tcp -I INPUT --dport 5080 -j ACCEPT
sudo iptables  -p tcp -I INPUT --dport 1935 -j ACCEPT
sudo iptables  -p tcp -I INPUT --dport 5443 -j ACCEPT
sudo iptables  -p tcp -I INPUT --dport 5000:65000 -j ACCEPT
sudo iptables  -p udp -I INPUT --dport 5000:65000 -j ACCEPT

sudo netfilter-persistent save
sudo netfilter-persistent reload
```

### SSL Enable
* SSL Enable : 대부분의 경우 https 를 사용해야 함. 
```
cd /usr/local/antmedia
sudo ./enable_ssl.sh -d {DOMAIN_NAME}
```
* Enabling SSL in Linux(Ubuntu) : (ssl enable 하려면 80 port open 필수)
  * https://github.com/ant-media/Ant-Media-Server/wiki/SSL-Setup

### 접속 URL

```
http://ipaddress:5080
```
* hiwylee/OracleWelcome1
* ![image](https://user-images.githubusercontent.com/7068088/122047767-7a866900-ce1b-11eb-8e9f-5ffa740c7764.png)
* ![image](https://user-images.githubusercontent.com/7068088/122048028-c20cf500-ce1b-11eb-95f6-3ec25c5ed885.png)

### WEB RTMP 
* https://your_domain_name:5443/WebRTCAppEE in Enterprise Edition or https://your_domain_name:5443/WebRTCApp in CE
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

* [Install guide](https://github.com/ant-media/Ant-Media-Server/wiki/Getting-Started)
* [community version 다운로드](https://github.com/ant-media/Ant-Media-Server/releases/)
* ![image](https://user-images.githubusercontent.com/7068088/122071989-2b97fe00-ce32-11eb-93d9-c0e3c4ff64ac.png)

### ant media status

* [how to enable SSL](https://www.youtube.com/watch?v=gxkUHyH-WpU)
 
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

### cloud-init

```
wget https://github.com/ant-media/Ant-Media-Server/releases/download/ams-v2.3.2/ant-media-server-2.3.2-community-2.3.2-20210422_0754.zip
wget https://raw.githubusercontent.com/ant-media/Scripts/master/install_ant-media-server.sh && chmod 755 install_ant-media-server.sh
./install_ant-media-server.sh  -i ant-media-server-2.3.2-community-2.3.2-20210422_0754.zip


sudo iptables  -p tcp -I INPUT --dport 80 -j ACCEPT
sudo iptables  -p tcp -I INPUT --dport 5080 -j ACCEPT
sudo iptables  -p tcp -I INPUT --dport 1935 -j ACCEPT
sudo iptables  -p tcp -I INPUT --dport 5443 -j ACCEPT
sudo iptables  -p tcp -I INPUT --dport 5000:65000 -j ACCEPT
sudo iptables  -p udp -I INPUT --dport 5000:65000 -j ACCEPT

sudo netfilter-persistent save
sudo netfilter-persistent reload

cd /usr/local/antmedia
sudo ./enable_ssl.sh -d myorcl.tk

sudo service antmedia status

sudo apt-get install -y git
sudo apt-get install -y vim

cd
sudo git clone https://github.com/ant-media/utilities.git
cd utilities
sudo nohup ./happytime-rtsp-server/rtspserver &
sudo nohup ./onvifserver &


```
<iframe width="560" height="315" src="https://myorcl.tk:5443/LiveApp/play.html?name=071278547887943360407523" frameborder="0" allowfullscreen></iframe>



