def preorder(v):
    for idx in range(N):
        if tree[idx][0] == v:
            print(tree[idx][0], end='')
            preorder(tree[idx][1])
            preorder(tree[idx][2])

def inorder(v):
    for idx in range(N):
        if tree[idx][0] == v:
            inorder(tree[idx][1])
            print(tree[idx][0], end='')
            inorder(tree[idx][2])

def postorder(v):
    for idx in range(N):
        if tree[idx][0] == v:
            postorder(tree[idx][1])
            postorder(tree[idx][2])
            print(tree[idx][0], end='')

N = int(input()) #노드의 개수
tree = [list(input().split()) for _ in range(N)]
print(tree)
preorder('A')
print()
inorder('A')
print()
postorder('A')
