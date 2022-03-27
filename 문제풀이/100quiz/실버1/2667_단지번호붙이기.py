from pprint import pprint
# 주변 탐색 델타
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(si, sj):
    home = 1 # 개수
    visited[si][sj] = 1 # 방문 처리

    # 주변 탐색
    for k in range(4):
        ni, nj = si + di[k], sj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and map[ni][nj] == '1':
            home += dfs(ni, nj)
        # if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj] or map[ni][nj ] == '0':
        #     continue
        # print(ni,nj)

    return home

N = int(input())
map = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)] # 이차원
# pprint(visited)

cnt = 0
result = []
for i in range(N):
    for j in range(N):
        # if map[i][j] == '0' or visited[i][j]:
        #     continue
        if map[i][j] == '1' and visited[i][j] == 0:
            result.append(dfs(i, j))
            cnt += 1

result.sort() # 오름차순 정렬
print(cnt) # 단지 개수
# print(result)
for num in result:
    print(num)