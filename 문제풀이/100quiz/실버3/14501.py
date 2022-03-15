N = int(input())
work = []

for _ in range(N):
    T, P = map(int, input().split())
    work.append([T, P])
# print(work)

profit = 0 # 최종 출력
days = [] # 확인용
# 뒤에서부터 조사하자
for idx in range(N-1, -1, -1):
    if work[idx][0] > N - idx:
        continue
    elif work[idx][0] <= N - idx:
        if len(days) == 0:
            days.append(idx)
            profit += work[idx][1]
        else: # 남은 기간동안 상담 가능
            if work[idx][0] <= days[-1] - idx:
                profit += work[idx][1]
                days.append(idx)
            else: # 겹치는 구간 발생
                # 그동안 모아온 돈과 비교해야함
                # 필요한 기간
                duration = list(range(1, work[idx][0]))
                # 비교해야하는 기간과 금액
                cancel = []
                cancel_profit = 0
                for day in duration:
                    cancel.append(idx + day)
                for c in cancel:
                    if c in days: # 겹치는 날짜
                        cancel_profit += work[c][1]
                if work[idx][1] > cancel_profit:
                    profit -= cancel_profit
                    profit += work[idx][1]
                    days.append(idx)
                    # 겹치는 날짜 제거
                    for c in cancel:
                        if c in days:
                            days.remove(c)
                else:
                    continue

print(profit)
# print(days)




# # 뒤에서부터 거꾸로 담기
# work.append([0,0]) # 인덱스랑 날짜 맞추기
# work = work[::-1]
#
# profit = 0
# days = []
# for i in range(1, N+1):
#     if work[i][0] > i:
#         pass
#     else:
#         if profit < work[i][1]:
#             days.append(N - work[i][0])
#             profit += work[i][1]
#         elif profit == work[i][1]:
#             pass
#         elif profit > work[i][1]:
#             pass
#
# print(profit)
# print(days)
