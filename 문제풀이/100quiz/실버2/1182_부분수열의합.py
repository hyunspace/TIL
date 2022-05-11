# 5월 10일

def find_sub_sets(arr):
    sub_set = [[]]
    for i in arr:
        len_ = len(sub_set)
        for j in range(len_):
            sub_set.append(sub_set[j] + [i])
    return sub_set

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
ans = 0
sets = find_sub_sets(numbers)
for idx in range(1, len(sets)):
    if sum(sets[idx]) == S:
        ans += 1
print(ans)