import sys; sys.stdin = open('input.txt')

for tc in range(10):
    tc_num = input()

    # 100 x 100 2차 배열 형태로
    # arr = []
    # for _ in range(100):
    #     arr.append(list(map(int, input().split())))

    # list-comprehension
    # arr = [i**2 for i in range(100)]
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 입력이 정상적으로 되는지 확인

    ans = 0 # 합의 최댓값을 저장하기 위한 변수
    # 각 행의 합 => 행 우선 순회
    # 외부 for문의 변수를 행 값으로
    for i in range(100):
        # 매번 행을 순회해서 합을 구하기 전에
        total = 0
        for j in range(100):
            total += arr[i][j]
        # i번 행의 합이 total에 담겨져 있다
        if ans < total:
            ans = total

    # 각 열의 합 => 열 우선 순회
    # 외부 for문의 변수를 열 값으로
    for i in range(100):
        # 매번 행을 순회해서 합을 구하기 전에
        total = 0
        for j in range(100):
            total += arr[j][i]
        # i번 행의 합이 total에 담겨져 있다
        if ans < total:
            ans = total

    # 대각의 합
    # 좌상단-> 우하단 => (행, 행) => (i, i) for i in range(100)
    total = 0
    for i in range(100):
        total += arr[i][i]
    if ans < total:
        ans = total
    # 우상단-> 좌하단 => (행, N-1-행) => (i, N-1-i) for i in range(100)
    total = 0
    for i in range(100):
        total += arr[i][99-i]
    if ans < total:
        ans = total

    print(ans)