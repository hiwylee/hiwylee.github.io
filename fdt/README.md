## Fast Data Transfer

### 용도
* 데이터 전송을 빠르게 하기위한 오픈 소스
* ![](https://fast-data-transfer.github.io/fdt/img/FDT_diagram.png)

### 홈
* https://github.com/fast-data-transfer/fdt
* 여러개의 파일을 한번에 전송하려면 file에 목록을 등록하고 -fl file.lst 준다.
  * -fl 뒤에 전송하려는 파일을 주면 안됨.
* -S 를 주게 되면 한 번 전송 받은 후 서버가 종료됨.
* 이어 받기는 안되는 듯 보임.
* [option 설명](https://fast-data-transfer.github.io/fdt/doc-fdt-ddcopy.html)

#### Case 0 : non standalone mode/file list


```bash
cat fl.list

02.zip
03.zip


0) security list
	121.134.70.44/32	TCP	All	4000-4003
1) server
java -XX:MaxDirectMemorySize=1024m -Xms2048m -Xmx3096m -jar fdt.jar -p 4000   -bs 16M -tp 4001,4002,4003 -v
2) cleint
java -XX:MaxDirectMemorySize=1024m -Xms2048m -Xmx3096m -jar fdt.jar -c 132.226.232.128  -p 4000   -bs 16M -tp 4001,4002,4003 -v   -d . -fl fl.list



```

#### Case 1

```bash
0) security list
	121.134.70.44/32	TCP	All	All
1) server
java -XX:MaxDirectMemorySize=1024m -Xms2048m -Xmx3096m -jar fdt.jar -p 4000  -bs 16M -tp 4001,4002   -v
2) cleint
java -XX:MaxDirectMemorySize=1024m -Xms2048m -Xmx3096m -jar fdt.jar -c 132.226.232.128  -p 4000   -bs 16M -tp 4001,4002   -v  -d .  01.zip

```

####  Case 2

```bash
0) security list
	121.134.70.44/32	TCP	All	4000-4003
1) server
java -XX:MaxDirectMemorySize=1024m -Xms2048m -Xmx3096m -jar fdt.jar -p 4000  -bs 16M -tp 4001,4002,4003 -v
2) cleint
java -XX:MaxDirectMemorySize=1024m -Xms2048m -Xmx3096m -jar fdt.jar -c 132.226.232.128  -p 4000   -bs 16M -tp 4001,4002,4003 -v  -d .  01.zip


```
