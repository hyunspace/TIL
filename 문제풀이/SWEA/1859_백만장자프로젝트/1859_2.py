import sys; sys.stdin = open('input2.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # N일에 대한 정보가 들어 올 것
    prices = list(map(int, input().split())) # 일일 가격을 담아둘 리스트
    # print(prices)

    # 1. 0부터 N-1까지 중에서 가장 큰 값을 먼저 구한다
    h_price = max(prices)
    for i in range(N):
        if h_price == prices[i]:
            h_idx = i
    # print(h_idx, prices[h_idx])

    profit = start = 0
    # 0부터 h_idx까지 발생한 이익을 더한다
    for i in range(start, h_idx):
        profit += h_price - prices[i]

    start = h_idx
    h_price = 0 # 초기화 후 다음 구간에서의 최댓값 구하기
    for j in range(h_idx+1, N-1):
        if h_price < prices[j]:
            h_price = prices[i]
            h_idx = i
