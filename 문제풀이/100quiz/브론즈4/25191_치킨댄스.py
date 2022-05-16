# 5월 17일

N = int(input())
A, B = map(int, input().split())

max_chicken = 0
max_chicken += (A // 2 + B)

if N >= max_chicken:
    print(max_chicken)
else:
    print(N)
