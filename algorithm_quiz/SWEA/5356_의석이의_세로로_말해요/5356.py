import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    result = ''
    # print(arr)

    # 열 고정, 행 순회
    result = ''
    for j in range(15):
        for i in range(5): # 행은 5줄로 고정
            if j < len(arr[i]): # 현재 순회 중인 j보다 길이가 크다 == 값이 있다
                result += arr[i][j]

    print(f'#{tc} {result}')