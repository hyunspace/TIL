import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(si, sj):
    visited[si][sj] = 1 # 방문 표시 먼저!

    # 탐색해야지 !! 대각선까지 !! 4방향: 하, 우, 상, 좌 // 대각선: 좌상, 우상, 좌하, 우하
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
        ni, nj = si + di, sj + dj
        if 0 <= ni < h and 0 <= nj < w and maps[ni][nj] == 1 and visited[ni][nj] == 0:
            dfs(ni, nj)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: # 종료 조건
        break

    maps = [list(map(int, input().split())) for _ in range(h)] # input 받기
    visited = [[0] * w for _ in range(h)] # dfs용 방문 배열

    # 섬의 개수 출력
    land_cnt = 0
    for i in range(h):
        for j in range(w):
            # 섬이 있고, 방문한 적 없는 곳이라면 dfs 시작해보자
            if maps[i][j] == 1 and visited[i][j] == 0:
                 dfs(i, j)
                 land_cnt += 1
    print(land_cnt)