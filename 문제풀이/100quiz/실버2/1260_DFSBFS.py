from collections import deque


def dfs(v):
    dfs_visited[v] = 1
    print(v, end = ' ')
    for nxt in nodes[v]:
        if dfs_visited[nxt]:
            continue
        dfs(nxt)

def bfs(start):
    queue = deque()
    visited = [0 for _ in range(n+1)]
    queue.append(start)
    visited[start] = 1
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        for next in nodes[now]:
            if visited[next]:
                continue
            queue.append(next)
            visited[next] = 1

n, m, v = map(int, input().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

# 조건에 맞춰서 sort하기
for i in nodes:
    i.sort()

# bfs를 위한 방문 리스트는 바깥에!
dfs_visited = [0 for _ in range(n+1)]

dfs(v)
print()
bfs(v)