import sys; sys.setrecursionlimit(10**6)

def delete_child(v):
    if tree[v]:
        for index in range(1, len(tree[v])):
            delete_child(tree[v][index])
        tree[v] = [0]

def clear_node(v):
    for t in tree:
        for n in range(len(t)):
            if t[n] == v:
                t.pop(n)
                break

V = int(input()) # 노드의 개수
parents = list(map(int, input().split()))
del_node = int(input())

tree = [[node] for node in range(V)]
for i in range(1, V):
    tree[parents[i]].append(i)
print(tree)
delete_child(del_node)
clear_node(del_node)
cnt = 0
print(tree)
for j in range(len(tree)):
    if tree[j] == [j]:
        cnt += 1
print(cnt)
'''
4
-1 0 1 2
2
'''