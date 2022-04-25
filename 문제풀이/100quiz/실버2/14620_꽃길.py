N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [0, -1, 0, 1, 0], [0, 0, 1, 0, -1] # 중앙, 상우하좌

visited = [[0] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        pass
