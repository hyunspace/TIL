import sys; sys.stdin = open('2304_input.txt')

N = int(input()) # 기둥의 개수

heights = [0] * 1001

# 기둥에 대한 정보를 먼저 정리하자
for n in range(N):
    X, H = map(int, input().split())
    heights[X] = H
# print(heights)

# 가장 높은 곳의 인덱스 찾기
max_h = max(heights)
max_x = heights.index(max_h)

# 왼쪽 >> 가장 높은 곳
for i in range(0, max_x):
    if heights[i] > heights[i+1]:
        heights[i+1] = heights[i]
# print(heights)

# 가장 높은 곳 << 오른쪽
for i in range(1000, max_x, -1):
    if heights[i] > heights[i-1]:
        heights[i-1] = heights[i]
# print(heights)

print(sum(heights))