import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(si, sj):
    visited[si][sj] = 1 # 방문 표시

    # 델타 탐색
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = si + di, sj + dj
        if 0 <= ni < M and 0 <= nj < N and fields[ni][nj] == 1 and visited[ni][nj] == 0:
            dfs(ni, nj)

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    fields = [[0] * N for _ in range(M)] # M행 N열

    # 배추 위치 정보
    for _ in range(K):
        i, j = map(int, input().split())
        fields[i][j] = 1

    cnt = 0 # 필요한 지렁이 개수
    visited = [[0] * N for _ in range(M)] # 방문 배열
    for i in range(M):
        for j in range(N):
            if fields[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1

    print(cnt)