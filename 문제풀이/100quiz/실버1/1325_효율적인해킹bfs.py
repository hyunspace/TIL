import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

def bfs(start):
    queue = deque()
    visited = [0 for _ in range(N + 1)]
    visited[start] = 1
    queue.append(start)
    cnt = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            now_com = queue.popleft()
            for next_com in coms[now_com]:
                if visited[next_com] == 0:
                    visited[next_com] = 1
                    queue.append(next_com)
                    cnt += 1
    return cnt

# N개의 컴퓨터 M개의 연결 정보
N, M = map(int, input().split())

# 연결 정보 받아오기
coms = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    coms[b].append(a)

# 시작 컴퓨터 별 최대 해킹 컴퓨터 개수
max_coms = [0 for _ in range(N+1)]
for com in range(1, N+1):
    max_coms[com] = bfs(com)

# 최댓값 찾기
max_com = max(max_coms)
# 최댓값을 가진 컴퓨터 번호
result = []
for i in range(1, N+1):
    if max_coms[i] == max_com:
        result.append(i)
result.sort()
print(*result)