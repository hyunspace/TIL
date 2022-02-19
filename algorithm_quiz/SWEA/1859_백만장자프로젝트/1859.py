import sys; sys.stdin = open('input2.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    # print(prices)

    # 주어진 예상 가격표를 순회해보자
    # 계산을 위한 변수들
    days = profit = buy = 0
    for day in range(len(prices)-1): # 인덱스 범위를 벗어나지 않게 -1 해준다
        if prices[day] <= prices[day+1]: # 내일 가격이 오른다면 사고, 오늘 내일 가격이 같다면 또 산다
            buy += prices[day]
            days += 1
        elif prices[day] > prices[day+1]: # 내일 가격이 떨어지면 오늘 팔아야지
            profit += prices[day] \
                      * days - buy
            days = buy = 0
    print(f'#{tc} {profit}')

