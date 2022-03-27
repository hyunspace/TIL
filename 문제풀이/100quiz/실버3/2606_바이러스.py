import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(start):
    ans = 1
    visited[start] = 1 # 방문 표시 먼저!
    for next_com in data[start]:
        if visited[next_com] == 0:
            ans += dfs(next_com)
    return ans

V = int(input()) # 컴퓨터의 수 == 노드의 수!
E = int(input()) # 간선의 개수
data = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
# print(data)
visited = [0 for _ in range(V+1)]
print(dfs(1)-1) # 1과 연결된 컴퓨터(노드)의 개수! 1부터 셌으니까 1개 빼기