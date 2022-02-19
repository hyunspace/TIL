import sys; sys.stdin = open('input.txt')

def count_blank(arr, N, K):
    result = 0
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if arr[i][j] == 1: # 1일때: 들어갈 공간 O
                cnt += 1
            else:              # 0일때: 들어갈 공간 X
                if cnt == K:
                    result += 1
                cnt = 0
    return result

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0]*(N+1))
    # print(arr)

    # 가로
    row_cnt = count_blank(arr, N, K)
    # print(row_cnt)

    # 세로
    trans_arr = list(map(list, zip(*arr)))
    column_cnt = count_blank(trans_arr, N, K)

    print(f'#{tc} {row_cnt + column_cnt}')



