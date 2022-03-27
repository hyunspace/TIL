import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(i, j):
    visited[i][j] = 1 # 방문표시
    area = 1
    # 델타 탐색
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < M and 0 <= nj < N and grids[ni][nj] == 0 and visited[ni][nj] == 0:
            area += dfs(ni, nj)
    return area

# M * N 배열, K개의 사각형
M, N, K = map(int, input().split())
data = []
for _ in range(K):
    a, b, c, d = map(int, input().split())
    data.append([M-d, M-b, a, c]) # 순환하기 쉽게 값 변환0

# 모눈종이에 사각형 표시하기
grids = [[0] * N for _ in range(M)]
for square in data:
    for i in range(square[0], square[1]):
        for j in range(square[2], square[3]):
            grids[i][j] = 1

cnt = 0 # 영역 셀 cnt
areas = []
visited = [[0] * N for _ in range(M)] # 방문 배열
for i in range(M):
    for j in range(N):
        if grids[i][j] == 0 and visited[i][j] == 0:
            areas.append(dfs(i, j))
            cnt += 1
print(cnt)
areas.sort()
print(*areas)
