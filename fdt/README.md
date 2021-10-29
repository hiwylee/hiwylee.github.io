## Fast Data Transfer

### TEST 


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
