def new_tree(v):
    temp = [v]
    print(temp)
    if tree[v] and v != del_node:
        for node in tree[v]:
            if node != del_node:
                temp.append(node)
        new.append(temp)
        for i in temp:
            new_tree(i)
    print(new)

V = int(input()) # 노드의 개수
parents = list(map(int, input().split()))
del_node = int(input())

tree = [[] for node in range(V)]
for i in range(1, V):
    tree[parents[i]].append(i)
print(tree)
new = []
new_tree(0)
print(new)
'''
5
-1 0 0 1 1
1
'''