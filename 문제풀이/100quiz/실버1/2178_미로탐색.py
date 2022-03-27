from collections import deque
from pprint import pprint

def bfs(si, sj, N, M):
    queue = deque()
    visited = [[0] * M for _ in range(N)] # 방문 표시 배열
    queue.append([si, sj]) # enQueue
    visited[si][sj] = 1 # 방문 표시

    # 탐색 하기
    while queue: # queue에 원소가 있는 동안 계속 반복
        i, j = queue.popleft() # deQueue
        # 도착지 확인 먼저 => v(t) == 도착지라면 해야할 일을 하자 => 지나온 칸의 수 출력
        if i == N-1 and j == M-1:
            return print(visited[i][j])
        # 도착지가 아니라면, 델타 탐색하기
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            # 범위 벗어나지 않고, 갈 수 있는 길이고, 가본 적 없는 길이라면
            if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append([ni, nj]) # enQueue
                visited[ni][nj] = visited[i][j] + 1 # 방문 표시
    # 도착지 못 찾고 while문 종료 되는 경우는 없음
    pprint(visited)


# input 받기
N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
# pprint(maps)
# 시작점 (0,0), 도착점 (n-1, m-1)
bfs(0, 0, N, M)