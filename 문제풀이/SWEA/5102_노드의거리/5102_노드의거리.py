import sys;sys.stdin = open('input.txt')
from collections import deque

def bfs(S, G):
    queue = deque()
    # S 시작점, G 도착점
    visited = [0 for _ in range(V+1)] # 방문용
    queue.append(S) # enQue
    visited[S] = 1 # 방문 표시
    while queue:
        # 탐색할 범위를 정해주자(일종의 가지치기)
        size = len(queue)
        for _ in range(size):
            now_node = queue.popleft() # deQue
            if now_node == G: # v(t)
                return visited[now_node] - 1 # path 정보(시작점도 셌으니까 1 빼줘야 함)
            # 주변 정점 탐색하자
            for next_node in nodes[now_node]:
                if visited[next_node] == 0: # 방문 안 했으면~
                    queue.append(next_node)
                    visited[next_node] = visited[now_node] + 1

    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S,G)}')