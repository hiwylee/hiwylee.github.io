### Graphviz - Graph Visualization Software
* [Graphviz - Graph Visualization Software](https://graphviz.org/documentation/)
* https://graphviz.org/doc/info/output.html
* https://graphs.grevian.org/example

### SQL table dependency 그래프

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

* digraph 를 이미지로 변환

```dot
dot -Tgif gv.gv -o gv.gif
```
---
### WebGraphvz
### Dot Guide
* https://graphviz.org/pdf/dotguide.pdf

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
