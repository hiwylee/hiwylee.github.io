### Docker Backup , and Move to New Env

* [외부망 Docker 이미지 백업 및 내부망 이관 롤백](https://waspro.tistory.com/514)
* https://ratseno.tistory.com/89
* [Docker Local Repository 사용하는 방법](https://snowdeer.github.io/docker/2018/01/24/docker-use-local-repository/)
* [폐쇄망에 Docker 구축하기](https://waspro.tistory.com/465?category=831750%EF%BB%BF)

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
