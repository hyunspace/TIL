# 트리 tree

* 트리
* 이진트리
* 이진탐색 트리
* 힙

<br/>

## 트리

### 개념

​	: A `tree` is a collection of entities called `nodes`. Nodes are connected by `edges`. Each `node` contains a `value` or `data`, and it may or may not have a `child node` .

* 비선형 구조
* 원소들 간에 `1:N` 관계를 가지는 자료 구조
* 원소들 간에 계층 관계를 가지는 계층형 자료 구조
* 상위 원소에서 하위 원소로 내려 가면서 확장되는 트리(나무) 모양의 구조

### 정의

* 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다

  * 노드 중 최상위 노드 => 루트(root)

  * 나머지 노드들은 n(>=0)개의 분리 집합 T1, ... TN으로 분리될 수 있다.

    ![Binary Tree](07_tree.assets/binary_tree.jpg)

### 용어 정리

* **노드** : 트리의 원소
* **간선(edge)** : 노드를 연결하는 선. The link between two nodes.
* **Path** : Path refers to the sequence of nodes along the edges of a tree.
* **Root** : The node at _the top of the tree_ is called root. There is only one root per tree and one path from the root node to any node.
* **Parent** : Any node except the root node has one edge upward to a node called parent.
* **Child** − The node below a given node connected by its edge downward is called its child node.ㅛ?
* **Leaf** − The node which does not have any child node is called the leaf node.
* **Subtree** − Subtree represents the descendants of a node.
* **Visiting** − Visiting refers to checking the value of a node when control is on the node.
* **Traversing** − Traversing means passing through nodes in a specific order.
* **Levels** − Level of a node represents the generation of a node. If the root node is at level 0, then its next child node is at level 1, its grandchild is at level 2, and so on.
* **keys** − Key represents a value of a node based on which a search operation is to be carried out for a node.

## Reference

[Definition](https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/)

[Tree structure](https://www.tutorialspoint.com/data_structures_algorithms/tree_data_structure.htm)

[그래프 그려주는 사이트](https://csacademy.com/app/graph_editor/)