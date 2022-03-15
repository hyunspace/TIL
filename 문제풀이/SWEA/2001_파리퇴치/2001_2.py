import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill_fly = 0
            for ni in range(i, i+M):
                for nj in range(j, j+M):
                    kill_fly += flies[ni][nj]
            if max_fly < kill_fly:
                max_fly = kill_fly
    print(f'#{tc} {max_fly}')

