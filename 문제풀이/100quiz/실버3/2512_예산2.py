# 5월 8일

def find_budget(start, end, have): # 탐색 시작점, 끝점, 지금 가진 돈
    global ans              # 갱신해갈 값은 글로벌로 받아오기
    if have > 0 and end > 0:
        length = end - start    # 탐색 대상의 개수
        temp = have // length   # 현재 최적 상한액
        center = end // 2 - 1       # 중간 값
        ans += temp
        if budgets[center] <= temp:
            for i in range(start, center):
                have -= budgets[i]
            for j in range(center, end):
                have -= temp
            find_budget(center + 1, end, have)
        else:
            for i in range(start, center + 1):
                have -= budgets[i]
            for j in range(center + 1, end):
                have -= temp
            find_budget(start, center, have)


N = int(input())
budgets = sorted(list(map(int, input().split())))
M = int(input())

if sum(budgets) <= M:
    print(max(budgets))
else:
    ans = 0
    find_budget(0, N, M)
    print(ans)