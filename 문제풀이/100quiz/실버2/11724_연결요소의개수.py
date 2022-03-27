import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(start):
    # 방문 처리 먼저
    visited[start] = 1
    for next in arr[start]:
        if visited[next] == 0:
            dfs(next)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

# 방문
visited = [0 for _ in range(n+1)]

cnt = 0
for node in range(1, n+1):
    # 아직 방문 안 했으면 dfs 돌려야지
    if visited[node] == 0:
        dfs(node)
        cnt += 1
print(cnt)