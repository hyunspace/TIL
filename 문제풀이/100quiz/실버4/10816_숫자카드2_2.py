# 5월 19일

# import sys
# input = sys.stdin.readline => 오히려 메모리 더 씀

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

negative_list = [0] * 10000001
positive_list = [0] * 10000001

for card in cards:
    if card >= 0:
        positive_list[card] += 1
    else:
        negative_list[abs(card)] += 1

for target in targets:
    if target >= 0:
        print(positive_list[target], end = ' ')
    else:
        print(negative_list[abs(target)], end = ' ')