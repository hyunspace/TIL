# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

## Feb 10, 2022 ##

import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 원본 숫자는 리스트에 담아두자
    nums = list(map(int, input().split()))
    # 숫자를 더할 변수와 더한 숫자를 담아둘 리스트
    total = 0
    totals = []
    # nums를 순회하면서 => 슬라이싱을 사용하면 for문 1개만 써도 됨
    for i in range(0, N-M+1):
        # M씩 묶어서 더하고
        for idx in range(i, i+M):
            total += nums[idx]
        # 묶어서 더한 숫자는 리스트에 추가하고
        totals.append(total)
        # 새로운 묶음으로 더해야 하므로 total은 다시 0으로 초기화
        total = 0
    # 더한 값이 담긴 리스트를 정렬하자
    # sorted_totals = sorted(totals)
    # print(f'#{tc} {sorted_totals[-1] - sorted_totals[0]}')

    # 만약 sorted를 쓰지 않는다면
    length = len(totals)
    for j in range(length-1, 0, -1):
        for k in range(0, j):
            if totals[k] > totals[k+1]:
                totals[k], totals[k+1] = totals[k+1], totals[k]
    print(f'#{tc} {totals[-1] - totals[0]}')
