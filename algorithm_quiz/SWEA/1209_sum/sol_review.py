import sys; sys.stdin = open('input.txt')

## 보충 시간에 배운 걸 적용해서 다시 한 번 풀어보자 !

for tc in range(1, 11):
    TC = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 최종적으로 출력할 최댓값을 담을 변수
    result = 0

    # 대각선 합을 더할 변수
    # 반복문을 통해 행 우선, 열 우선, 대각선([i][i]과 [i][N-1-i]
    le_sum = ri_sum = 0
    for i in range(100):
        le_sum += arr[i][i]
        ri_sum += arr[i][99-i]

        r_sum = c_sum = 0
        for j in range(100):
            r_sum += arr[i][j] # 행 우선
            c_sum += arr[j][i] # 열 우선
            if result < r_sum: # 행 우선 합 비교
                result = r_sum
            if result < c_sum: # 열 우선 합 비교
                result = c_sum

    # for문 다 돌고 나서 대각선 합을 비교하기
    if result < le_sum:
        result = le_sum
    if result < ri_sum:
        result = ri_sum

    print(f'#{tc} {result}')