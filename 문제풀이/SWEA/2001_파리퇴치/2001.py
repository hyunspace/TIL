import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # print(flies)

    for i in range(N-M+1):
        kill_fly = 0
        max_fly = 0
        for j in range(N-M+1):
            for k in range(M):
                kill_fly += flies[i+k][j+k]

            if max_fly < kill_fly:
                max_fly = kill_fly

    print(f'#{tc} {max_fly}')


