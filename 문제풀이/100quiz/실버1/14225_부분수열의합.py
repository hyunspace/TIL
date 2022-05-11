# 5월 11일

def find_sub_set(arr):
    sub_set = [[]]
    for i in arr:
        length = len(sub_set)
        for j in range(length):
            sub_set.append(sub_set[j] + [i])
    return sub_set

# 입력값 구하기
N = int(input())
S = list(map(int, input().split()))

# 부분 집합 구하기
sub_sets = find_sub_set(S)

# 부분 수열의 합을 담아둘 리스트
sum_numbers = []

# 순회하며 부분 수열의 합을 담기
for case in sub_sets:
    sum_numbers.append(sum(case))

# 정렬
sum_numbers.sort()

# 정답 찾기
def find_answer():
    ans = 0
    for number in sum_numbers:
        if ans == number:
            continue
        elif ans + 1 == number:
            ans += 1
        else:
            return print(ans + 1)
    return print(ans + 1)

find_answer()
