# 5월 22일

from itertools import combinations

N = int(input())
works = list(map(int, input().split()))
sub_sets = []

for i in range(1, N + 1):
    sub_sets += list(combinations(works, i))
# print(sub_sets)
sum_sets = set()

for sub_set in sub_sets:
    sum_sets.add(sum(sub_set))

flag = 0
for x in sum_sets:
    if x < 7:
        if x == 4:
            flag = 1
    elif x % 7 == 3:
        flag = 1
        break
    else:
        continue

if flag:
    print('YES')
else:
    print('NO')
