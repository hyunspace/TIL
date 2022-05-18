# 5월 13일

import sys; sys.setrecursionlimit(10**6)

def cnt_card(goal, start, end):
    if start >= end:
        return 0
    middle = (start + end) // 2
    if goal == cards[middle]:
        cnt = 0
        for idx in range(start, end):
            if cards[idx] == goal:
                cnt += 1
        return cnt
    elif goal > cards[middle]:
        return cnt_card(goal, middle + 1, end)
    else:
        return cnt_card(goal, start, middle + 1)


N = int(input())
cards = sorted(list(map(int, input().split())))
print(cards)
M = int(input())
targets = list(map(int, input().split()))
print(targets)

cnt_dict = {}
for card in cards:
    if card not in cnt_dict:
        # print(target, cnt_dict)
        cnt_dict[card] = cnt_card(card, 0, N)
print(cnt_dict)

for target in targets:
    if target in cnt_dict:
        print(target)
        print(cnt_dict[target], end=' ')
    else:
        print(0)