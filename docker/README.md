### OCIR 접속

```
sudo yum install -y docker-engine
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 sudo chmod +x /usr/local/bin/docker-compose

 sudo usermod -aG docker $USER
 
 systemctl status docker.service
 systemctl enable docker.service
 
 sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

 docker image pull nginx
Using default tag: latest
Trying to pull repository docker.io/library/nginx ...
latest: Pulling from docker.io/library/nginx
eff15d958d66: Pull complete
1e5351450a59: Pull complete
2df63e6ce2be: Pull complete
9171c7ae368c: Pull complete
020f975acd28: Pull complete
266f639b35ad: Pull complete
Digest: sha256:097c3a0913d7e3a5b01b6c685a60c03632fc7a2b50bc8e35bcaa3691d788226e
Status: Downloaded newer image for nginx:latest
nginx:latest

[opc@free cicd]$ sudo docker login icn.ocir.io
Username: cnixtvdthbb6/wonyong.lee@oracle.com
Password:

[opc@free cicd]$ sudo docker images
REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
icn.ocir.io/cnixtvdthbb6/cicd   nginx               ea335eea17ab        2 days ago          141MB
nginx                           latest              ea335eea17ab        2 days ago          141MB
[opc@free cicd]$ sudo docker tag ea335eea17ab icn.ocir.io/cnixtvdthbb6/cicd/nginx:latest
[opc@free cicd]$ sudo docker images
REPOSITORY                            TAG                 IMAGE ID            CREATED             SIZE
nginx                                 latest              ea335eea17ab        2 days ago          141MB
icn.ocir.io/cnixtvdthbb6/cicd/nginx   latest              ea335eea17ab        2 days ago          141MB
[opc@free cicd]$ sudo docker push icn.ocir.io/cnixtvdthbb6/cicd/nginx:latest
The push refers to repository [icn.ocir.io/cnixtvdthbb6/cicd/nginx]

[opc@free cicd]$ sudo docker push icn.ocir.io/cnixtvdthbb6/cicd/nginx:latest
The push refers to repository [icn.ocir.io/cnixtvdthbb6/cicd/nginx]
8525cde30b22: Pushed
1e8ad06c81b6: Pushed
49eeddd2150f: Pushed
ff4c72779430: Pushed
37380c5830fe: Pushed
e1bbcf243d0e: Pushed
latest: digest: sha256:2f14a471f2c2819a3faf88b72f56a0372ff5af4cb42ec45aab00c03ca5c9989f size: 1570

[opc@free cicd]$ sudo docker run --name nginx  icn.ocir.io/cnixtvdthbb6/cicd/nginx:latest

[opc@free cicd]$ cat docker-compose.yml
version: "3.7"

services:
  app:
    image: icn.ocir.io/cnixtvdthbb6/cicd/nginx:latest
    ports:
      - 80:80
#    working_dir: /app
    volumes:
      - ./:/app
    environment:
      MYSQL_HOST: mysql
      MYSQL_USER: root
      MYSQL_PASSWORD: secret
      MYSQL_DB: todos

[opc@free cicd]$ docker-compose up
Starting cicd_app_1 ... done
Attaching to cicd_app_1
app_1  | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
app_1  | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
app_1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
app_1  | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
app_1  | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
app_1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
app_1  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
app_1  | /docker-entrypoint.sh: Configuration complete; ready for start up
app_1  | 2021/11/19 23:09:42 [notice] 1#1: using the "epoll" event method
app_1  | 2021/11/19 23:09:42 [notice] 1#1: nginx/1.21.4
app_1  | 2021/11/19 23:09:42 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6)
app_1  | 2021/11/19 23:09:42 [notice] 1#1: OS: Linux 5.4.17-2102.206.1.el7uek.x86_64
app_1  | 2021/11/19 23:09:42 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
app_1  | 2021/11/19 23:09:42 [notice] 1#1: start worker processes
app_1  | 2021/11/19 23:09:42 [notice] 1#1: start worker process 32
app_1  | 2021/11/19 23:09:42 [notice] 1#1: start worker process 33

```

### Docker Concept

* [Docker 개념, 관리, 이미지생성까지 한번에!](https://cultivo-hy.github.io/docker/image/usage/2019/03/14/Docker%EC%A0%95%EB%A6%AC/)
* ![](https://subicura.com/assets/article_images/2017-01-19-docker-guide-for-beginners-1/image-layer.png)

* ![](https://subicura.com/assets/article_images/2017-01-19-docker-guide-for-beginners-1/image-url.png)
 
 *![](https://subicura.com/assets/article_images/2017-02-10-docker-guide-for-beginners-create-image-and-deploy/create-image.png)
 
 * ![](https://subicura.com/assets/article_images/2017-02-10-docker-guide-for-beginners-create-image-and-deploy/docker-registry.png)

### Docker Network
* [Docker 네트워크](https://youngmind.tistory.com/entry/%EB%8F%84%EC%BB%A4-%EA%B0%95%EC%A2%8C-3-%EB%8F%84%EC%BB%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-1)
  * [Docker강좌 ](https://youngmind.tistory.com/category/%EA%B0%80%EC%83%81%ED%99%94/Docker_K8s)
### Docker Compose
* ![](http://raccoonyy.github.io/content/images/2017/03/docker-compose-yml.png)
### Docker Backup , and Move to New Env

* [외부망 Docker 이미지 백업 및 내부망 이관 롤백](https://waspro.tistory.com/514)
* https://ratseno.tistory.com/89
* [Docker Local Repository 사용하는 방법](https://snowdeer.github.io/docker/2018/01/24/docker-use-local-repository/)
* [폐쇄망에 Docker 구축하기](https://waspro.tistory.com/465?category=831750%EF%BB%BF)
* [도커 프라이빗 레지스트리 구성 후 이미지 파일 올리기](https://ratseno.tistory.com/89)

  
```txt
https://ratseno.tistory.com/89

1) docker registry를 구성하기 위해 registy image를 받겠습니다.

docker pull [registry_img]

2) 이미지 확인

docker images

2-1) 해당 이미지를 이용하여 컨테이너를 실행

docker container run -d -p [컨테이너 포트 넘버]:[호스트 포트 넘버] --name [컨테이너명] registry
docker container run -d -p 5000:5000 --name registry registry

2-2) 컨테이너 실행 확인
docker ps

============
도커 레지스트리 환경 구성 전제
============

<< 인터넷이 되는 docker 환경(외부)에서 image 파일을 pull.  (인터넷 가능 도커환경)>>
(1) 백업
docker pull [postgres]
docker images
docker save -o postgres.tar postgres:latest

(2) move postgres.tar to 새로운 환경

*3) docker load 명령어로 image 파일 불러오기. (폐쇄망 도커환경)

docker load -i postgres.tar

(4) 구성해둔 프라이빗 레지스트리에 push하기 위해 새롭게 tag생성
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
docker postgres:latest 127.0.0.1:5000/postgres-test:latest

127.0.0.1:5000은 현재 프라이빗 레지스트리가 동작하고있는 컨테이너로의 주소입니다.
tag를 생성할때 저장소 주소/이미지 명:태그 형식으로 작성

(5) 레지스트리로 push

docker image push 127.0.0.1:5000/postgres-test:latest

(6) push 확인해봅니다.  

curl -X GET http://127.0.0.1:5000/v2/_catalog

docker images

----------------------------------------------------------

yml :  repository 변경내용 저장

        image: postgres:9.5 
        image: 127.0.0.1:5000/postgres-test:latest  이런식으로 변경하여 사용할수 있습니다.
```        
