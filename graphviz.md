### Graphviz - Graph Visualization Software
* [Graphviz - Graph Visualization Software](https://graphviz.org/documentation/)
* https://graphviz.org/doc/info/output.html
* https://graphs.grevian.org/example

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
