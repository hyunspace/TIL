# 5월 8일

N = int(input())
budgets_data = list(map(int, input().split()))
budgets = budgets_data[::]
M = int(input())

current_plan = M // N
for idx in range(N):
    if budgets[idx] <= current_plan:
        budgets[idx] = 0
    else:
        budgets[idx] -= current_plan