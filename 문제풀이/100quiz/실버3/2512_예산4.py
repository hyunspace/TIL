# 5월 8일, 5월 9일

def find_budget(start, end, have): # 탐색 시작점, 끝점, 지금 가진 돈
    global ans              # 갱신해갈 값은 글로벌로 받아오기
    if have > 0 and end > 0 and start <= N:
        length = end - start    # 탐색 대상의 개수
        temp = have // length   # 현재 최적 상한액
        center = end // 2 - 1       # 중간 값
        ans += temp
        if temp == 0:
            return

        if budgets[center] < temp:                  # 탐색값이 더 크다면
            for i in range(start, center + 1):      # 왼쪽 구간은 원하는 만큼 다 주기
                have -= budgets[i]
            for j in range(center + 1, end):            # 오른쪽 구간은 탐색값만큼만
                have -= temp
            find_budget(center + 1, end, have)          # 오른쪽 구간으로 이동

        elif budgets[center] == temp:               # 탐색값과 같다면 (왼쪽은 무조건 작음)
            for i in range(start, center + 1):
                have -= budgets[i]
            for j in range(center + 1, end):
                have -= temp
            find_budget(center + 1, end, have)

        else:                                        # 탐색값이 더 작다면 => 왼쪽과 오른쪽 동시에 탐색해야함
            for i in range(start, center):
                if budgets[i] < temp:
                    have -= budgets[i]
                else:
                    have -= temp
            for j in range(center, end):
                have -= temp
            find_budget(start, end, have)


N = int(input())
budgets = sorted(list(map(int, input().split())))
M = int(input())

if sum(budgets) <= M:
    print(max(budgets))
else:
    ans = 0
    find_budget(0, N, M)
    print(ans)