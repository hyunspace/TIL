# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

'''
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
'''

### Feb 10 ###

import sys
N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

# 버블소트 => 시간 초과ㅠㅠㅠ
# for i in range(N-1, 0, -1):
#     for j in range(0, i):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# print(numbers[0], numbers[-1])

# 최댓값 구하기
max_num = numbers[0]
for i in range(1, N):
    if max_num < numbers[i]:
        max_num = numbers[i]

# 최솟값 구하기
min_num = numbers[0]
for i in range(1, N):
    if min_num > numbers[i]:
        min_num = numbers[i]

print(min_num, max_num)