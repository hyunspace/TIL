# 4월 19일

def find_leaf(s):
    global leaves

    visited[s] = 1
    # 자식 1명 이상이면 돌아봐야지
    if len(tree[s]) >= 1:
        for child in tree[s]:
            if visited[child] == 0:
                find_leaf(child)
    else:
        if visited[s] == 0:
            visited[s] = 1
            leaves += 1
            return

N = int(input())
parents = list(map(int, input().split()))
tree = [[] for i in range(N)]
delete_node = int(input())

for idx in range(N):
    if parents[idx] == -1: # root
        continue
    else:
        tree[parents[idx]].append(idx)

leaves = 0
visited = [0 for i in range(N)]
find_leaf(0)
# print(tree)
# print(visited)
print(leaves)

# 3
# -1 0 1
# 2