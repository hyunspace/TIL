# 5월 23일

time = list(map(int, input().split()))
D = int(input())

for idx in range(2, 0, -1):
    time[idx] += D % 60
    D //= 60

time[0] += D
for idx in range(2, 0, -1):
    if time[idx] >= 60:
        time[idx - 1] += time[idx] // 60
        time[idx] %= 60
if time[0] % 24 == 0:
    time[0] = 0
elif time[0] > 24:
    time[0] //= 24

for t in time:
    print(t, end=' ')

