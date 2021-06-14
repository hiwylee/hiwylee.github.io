## ANT Media Server 

  
* https://github.com/ant-media/Ant-Media-Server/releases/download/ams-v2.3.3/ant-media-server-2.3.3-community-2.3.3-20210606_1542.zip

* https://github.com/ant-media/Ant-Media-Server/wiki/Getting-Started

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
[community version 다운로드](https://github.com/ant-media/Ant-Media-Server/releases/)

