# 4월 25일
# 4월 28일 재도전!

def availability(i, j):
    global temp_cost
    temp_cost += garden[i][j]
    di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]  # 중앙, 상우하좌
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            temp_cost += garden[ni][nj]
        else:
            temp_cost = 0
            return 0
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        visited[ni][nj] = 1 # 방문 표시
        return temp_cost


def lowest_cost(i, j):
    if availability(i, j):
        pass


N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [0, -1, 0, 1, 0], [0, 0, 1, 0, -1]  # 중앙, 상우하좌

min_cost = 200*5*3
temp_cost = 0

for y in range(N):
    for x in range(N):
        visited = [[0] * N for _ in range(N)]
        if availability(y, x): # 유효성 통과
            pass