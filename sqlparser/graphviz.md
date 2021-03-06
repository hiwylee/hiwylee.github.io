### Graphviz - Graph Visualization Software
* [Graphviz - Graph Visualization Software](https://graphviz.org/documentation/)
* https://graphviz.org/doc/info/output.html
* https://graphs.grevian.org/example
---

### SQL 문장에 사용되는 테이블  종속  관계 그래프 (python)
---

#### 필요 S/W
* python
  *  sqlparse / sql_metadata
* graphviz

#### 테스트 
* python pip install

```
$ curl https://bootstrap.pypa.io/get-pip.py -o ge
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 1884k  100 1884k    0     0  1516k      0  0:00:01  0:00:01 --:--:-- 1517k

$ python get-pip.py

$  pip install --upgrade pip

```

* python 필요 패키지 설치 : sqlparse/sql_metadata

```
pip install sqlparse
pip install sql_metadata
```

* gv.py : sql 문장을 파싱하여 테이블 참조를 만들어 graphviz 파일로 만듬

```python

# pip install sqlparse
# pip install sql_metadata

import sqlparse;
import sql_metadata

# https://pypi.org/project/sql-metadata/

def sql_list(filename):
    print("digraph {")
    print("  rankdir=RL;")

    with open(filename,encoding='utf8') as f:
        content = f.read()
    for stmt in sqlparse.parse(content, encoding='utf-8') :
        if stmt.get_type() == 'CREATE' :
            tbls = sql_metadata.get_query_tables(stmt.value)
            for i in range(1,len(tbls)) :
                print("  %s -> %s" % (tbls[i],  tbls[0]))
    print("}")            


import sys

if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
   #  sql_list(sys.argv[0])
   if len(sys.argv) == 1  :
      sql_list("y.sql")
      ## sql_list("x.sql")
   else :
      sql_list(sys.argv[1])
```

* digraph 파일 생성 및 이미지로 변환
  * graphviz [설치](https://graphviz.org/download/)
```dot
$ python gv.py y.sql > gv.gv
$ dot -Tgif gv.gv -o gv.gif
```
---
### WebGraphvz
### Dot Guide
* https://graphviz.org/pdf/dotguide.pdf
* Download & Install graphvis
### Samples
* type large.gv
```dot
digraph {
    A [label="King Arthur"]
    B [label="Sir Bedevere the Wise"]
    L [label="Sir Lancelot the Brave"]
    A -> B
    A -> L
    B -> L [constraint=false]
}
```
* generate pdf

```
dot -Tpdf large.gv -o large.pdf
```
![](https://camo.githubusercontent.com/e61fc68123555d2542a82d5f008d3f400661b6f7dacd23e4e846718206d91550/68747470733a2f2f7261772e6769746875622e636f6d2f78666c72362f677261706876697a2f6d61737465722f646f63732f726f756e642d7461626c652e706e67)
---
## java SQLParser 사용법 (java version)
---
### 순서
* maven download
* 환경변수 설정
* javacc download [github](https://github.com/javacc/javacc)
* JSQLParser download and build [github](https://github.com/JSQLParser/JSqlParser) [original home](http://jsqlparser.sourceforge.net/)
* sql parser 프로그램 개발

```
set MAVEN_HOME=D:\Tools\apache-maven-3.6.3
set JAVA_HOME=C:\Program Files\Java\jdk1.8.0_281
```

```
mvn pacakge
```
