# 5월 15일 시간초과

from itertools import combinations

N = int(input())
works = list(map(int, input().split()))
sub_sets = []

for i in range(1, N + 1):
    sub_sets += list(combinations(works, i))
# print(sub_sets)

flag = 0
for sub_set in sub_sets:
    if sum(sub_set) < 7:
        if sum(sub_set) == 4:
            flag = 1
    elif sum(sub_set) % 7 == 3:
        flag = 1
        break
    else:
        continue

if flag:
    print('YES')
else:
    print('NO')
