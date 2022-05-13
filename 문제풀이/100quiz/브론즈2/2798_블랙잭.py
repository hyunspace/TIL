import itertools

N, M = map(int, input().split())
cards = list(map(int, input().split()))
cases = list(itertools.combinations(cards, 3))

max_case = 0
for case in cases:
    if max_case <= sum(case) <= M:
        max_case = sum(case)

print(max_case)