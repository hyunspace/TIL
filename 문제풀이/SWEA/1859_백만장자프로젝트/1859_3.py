import sys; sys.stdin = open('input2.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    # print(prices)

    start = h_idx = profit = 0

    while start < N:
        h_idx = start
        for i in range(start, N):
            if prices[h_idx] < prices[i]:
                h_idx = i

        for i in range(start, h_idx):
            profit += prices[h_idx] - prices[i]
        start = h_idx + 1

    print(f'#{tc} {profit}')