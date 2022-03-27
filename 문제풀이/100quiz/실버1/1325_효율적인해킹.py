import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

# def dfs(start): => 시간 초과 ㅡㅡ
#     visited[start] = 1
#     cnt = 1
#     for next_com in coms[start]:
#         if visited[next_com] == 0:
#             cnt += dfs(next_com)
#     return cnt

def bfs(start):
    visited = [0 for _ in range(N + 1)]

# N개의 컴퓨터 M개의 연결 정보
N, M = map(int, input().split())

# 연결 정보 받아오기
coms = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    # coms[a].append(b) => A에서 B로 갈 수는 없어
    coms[b].append(a)

# 시작 컴퓨터 별 최대 해킹 컴퓨터 개수
max_coms = [0 for _ in range(N+1)]
for com in range(1, N+1):
    visited = [0 for _ in range(N + 1)]  # 방문 배열 초기화
    max_coms[com] = dfs(com)

# 최댓값 찾기
max_com = max(max_coms)
# 최댓값을 가진 컴퓨터 번호
result = []
for i in range(1, N+1):
    if max_coms[i] == max_com:
        result.append(i)
result.sort()
print(*result)