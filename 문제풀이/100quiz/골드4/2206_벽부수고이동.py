from collections import deque

# dfs로 바꿔서 풀어보기 ㅜㅜ
def find_path(si, sj, cnt):
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    result = []

    queue.append((si, sj, cnt))
    visited[si][sj] = 1

    while queue:
        i, j, remove = queue.popleft()
        # 도착
        if i == N-1 and j == M-1 and remove <= 1:
            result.append(visited[i][j])
        # 도착X => 탐색
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if maze[ni][nj] != 1: # 벽이 아니면
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append((ni, nj, remove))
                elif maze[ni][nj] == 1 and remove < 1: # 벽이지만 부술 수 있다면
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append((ni, nj, remove+1))
    return result

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
# print(maze)
result = find_path(0, 0, 0)
if result:
    print(min(result))
else:
    print(-1)

'''
8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100
'''