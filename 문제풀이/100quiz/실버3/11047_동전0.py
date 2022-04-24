# 4월 24일
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

rear = N - 1
cnt = 0
while True:
    # 종료 조건
    if K == 0:
        break
    # 목표 < 현재 동전
    if K < coins[rear]:
        rear -= 1
    # 목표 == 현재 동전
    elif K == coins[rear]:
        cnt += 1
        break
    # 목표 > 현재 동전
    else:
        X = K // coins[rear] # 여러번 반복하지 말고 끝내자
        cnt += X
        K %= coins[rear]
        # K -= coins[rear]
        # cnt += 1
print(cnt)
