import sys; sys.stdin = open('SWEA12712_input.txt')

# + 모양 / x 모양
di = [-1, 0, 1, 0, -1, 1, 1, -1]
dj = [0, 1, 0, -1, 1, 1, -1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N):
        for j in range(N):
            kill = arr[i][j]
            for k in range(4):
                for m in range(1, M):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        kill += arr[ni][nj]
            if max_kill < kill:
                max_kill = kill

            kill = arr[i][j]
            for k in range(4, 8):
                for m in range(1, M):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        kill += arr[ni][nj]
            if max_kill < kill:
                max_kill = kill
    print(f'#{tc} {max_kill}')