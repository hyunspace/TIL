import sys
input = sys.stdin.readline
from collections import deque

def bfs(s, g):
    queue = deque()
    visited = [0 for _ in range(n+1)]
    visited[s] = 1 # 방문처리
    queue.append(s) # enQue
    while queue:
        size = len(queue)
        for _ in range(size):
            now_mem = queue.popleft()
            if now_mem == g:
                return print(visited[now_mem] - 1)
            # 탐색 시작
            for next_mem in data[now_mem]:
                if visited[next_mem] == 0:
                    visited[next_mem] = visited[now_mem] + 1
                    queue.append(next_mem)
    return print(-1)


# 입력값
n = int(input()) # 전체 사람 수
start, goal = map(int, input().split()) # 궁금한 두 사람
data = [[] for _ in range(n+1)]
m = int(input()) # 관계의 개수
for _ in range(m):
    parent, child = map(int, input().split())
    data[parent].append(child)
    data[child].append(parent)

bfs(start, goal)