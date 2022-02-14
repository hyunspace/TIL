import sys; sys.stdin = open('input.txt')

for tc in range(10):
    tc_num = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    ans = 0 # 합의 최댓값을 저장하기 위한 변수
    diag1 = diag2 = 0 # 대각의 합을 구하기 위한 변수

    # 변수를 늘려서 for문을 하나로 합칠 수 있다!!!
    for i in range(100):
        # 대각의 합도 합칠 수 있다!
        # arr[i][i], arr[i][99-i]
        diag1 += arr[i][i]
        diag2 += arr[i][99-i]

        rsum = csum = 0
        for j in range(100):
            rsum += arr[i][j]
            csum += arr[j][i]
        # ans = max(ans, rsum, csum)
        if ans < rsum:
            ans = rsum
        if ans < csum:
            ans = csum
    if ans < diag1:
        ans = diag1
    if ans < diag2:
        ans = diag2

    print(ans)