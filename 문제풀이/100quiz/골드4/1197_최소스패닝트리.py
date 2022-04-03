import sys; sys.setrecursionlimit(10**6)

def dfs(v, now_sum):
    global min_value

    visited[v] = 1 # 방문 표시 먼저

    if v == V: # 마지막 노드 도착
        if min_value > now_sum: # 최소값보다 더 큰 값을 찾았다면
            min_value = now_sum # 갱신
            return print(min_value)
        return

    if now_sum > min_value: # 확인 중간에 이미 최소값 초과
        return # 더이상 조사할 필요가 없음

    for next_node in tree[v]:
        if visited[next_node[0]] == 0: # 방문 안 했다면
            now_sum += next_node[1]    # 합에 더해주고
            dfs(next_node[0], now_sum) # dfs 넘겨주기(넘긴 후에 방문 표시할 것)

V, E = map(int, input().split())
tree = [[] for _ in range(V+1)]

for _ in range(E):
    node1, node2, value = map(int, input().split())
    tree[node1].append((node2, value))
    tree[node2].append((node1, value))
for t in tree:
    if t:
        t.sort(key=lambda x:x[1])
visited = [0 for _ in range(V+1)]
min_value = 2147483647
dfs(1, 0)