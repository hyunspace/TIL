import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(i, j, rain):
    checked[i][j] = 1 # 찍고
    safe_land = 1
    # 4방향 델타 탐색
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and maps[ni][nj] > rain and checked[ni][nj] == 0:
            safe_land += dfs(ni, nj, rain)
    return safe_land

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

# 모두 물에 잠기는 장마철 비의 양을 먼저 구하자
# => 이 값 이하로 확인해주면 된다
max_rain = 1
for arr in maps:
    if max_rain < max(arr):
        max_rain = max(arr)


rain = N
result = []

for rain in range(max_rain+1):
    cnt = 0
    checked = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maps[i][j] > rain and checked[i][j] == 0:
                dfs(i, j, rain)
                cnt += 1
    result.append(cnt)
print(result)
print(max(result))