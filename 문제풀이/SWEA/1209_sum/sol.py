import sys; sys.stdin = open('input.txt')

### Feb 14 ###


# 10개의 테스트 케이스
T = 10

# 를 반복하면서
for tc in range(T):
    case_number = int(input())
    # 먼저 행렬 받기! / 2차원 리스트
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 행/열/대각선의 합을 담을 변수와 구한 합을 담아둘 리스트
    sum_ij = 0 # 매번 초기화 할 것
    sum_list = []

    # 행 우선으로 돌아보자
    for i in range(100):
        for j in range(100):
            sum_ij += arr[i][j]
        sum_list.append(sum_ij)
        sum_ij = 0
    # 열 우선으로 돌아보자
    for j in range(100):
        for i in range(100):
            sum_ij += arr[i][j]
        sum_list.append(sum_ij)
        sum_ij = 0
    # 왼쪽 위=>오른쪽 아래 대각선
    for i in range(100):
        sum_ij += arr[i][i]
    sum_list.append(sum_ij)
    sum_ij = 0
    # 오른쪽 위=>왼쪽 아래 대각선
    for i in range(100):
        sum_ij += arr[i][99-i]
    sum_list.append(sum_ij)

    # 최댓값 구하기...
    max_num = 0
    for idx in range(len(sum_list)):
        if max_num < sum_list[idx]:
            max_num = sum_list[idx]

    # 결과값 출력
    print(f'#{tc+1} {max_num}')




