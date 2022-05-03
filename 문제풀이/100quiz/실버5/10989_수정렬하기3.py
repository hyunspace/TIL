# 4월 22일
import sys
input = sys.stdin.readline

N = int(input())
counting = [0] * 10001

for _ in range(N):
    counting[int(input())] += 1

for i in range(10001):
    if counting[i]:
        while counting[i] > 0:
            print(i)
            counting[i] -= 1
        # for _ in range(counting[i]):
        #     print(i)
