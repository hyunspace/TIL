# 5월 5일

def find_max(start, end, now_have):
    global ans
    middle = end // 2                           # 중앙 인덱스 찾기
    this_turn = now_have // (end - start + 1)   # 총 잔액 // 현재 탐색 대상인, 살아 있는 예산 요청 개수
    if budgets[middle] >= this_turn:                # 중앙 값 >= 이번 조사 값
        for idx in range(start, middle):
            now_have -= budgets[idx]                # 왼쪽 지자체는 모두 돈 받아감
            ans += budgets[idx]                     # 준 거 체크하기
        for idx in range(middle, end):
            now_have -= this_turn                   # 오른쪽 지자체는 this_turn 만큼만 받아감
            ans += this_turn                        # 줬으니까 일단 체크

    elif budgets[middle] > this_turn:               # 중앙 값 > 이번 조사 값 => 왼쪽으로 가세요
        find_max(start, middle, now_have)

    else:                                           # 중앙 값 < 이번 조사 값 => 오른쪽으로 가세요
        for idx in range(start, middle + 1):
            now_have -= budgets[idx]                # 왼쪽 지자체는 모두 돈 받아감
            ans += budgets[idx]                     # 준 거 체크하기
        find_max(middle + 1, )



N = int(input())
budgets = list(map(int, input().split()))
budgets.sort()
max_budget = int(input())

ans = 0

if sum(budgets) <= max_budget:
    print(sum(budgets))
else:
    find_max(0, N, max_budget)
    print(ans)