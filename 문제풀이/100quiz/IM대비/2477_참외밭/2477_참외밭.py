import sys; sys.stdin = open('2477_input.txt')

K = int(input())
direction_cnt = [0] * 5
sides = []

# 입력값을 쓰기 좋게 정리하자
for _ in range(6):
    d, l = map(int, input().split())
    for idx in range(1, 6):
        if idx == d:
            direction_cnt[idx] += 1
    sides.append([d, l])

# 가장 큰 사각형 구하기
wh = []
for i in range(1, 5):
    if direction_cnt[i] == 1:
        wh.append(i)
# print(wh) # 해당 방향으로 이동하는 애들은 1번만 등장 => 큰 변!

index = []
for di in range(6):
    if sides[di][0] in wh:
        if sides[(di + 1) % 6][0] not in wh:
            large_w, large_h = sides[(di - 1)][1], sides[di][1]
            small_w, small_h = sides[(di + 2) % 6][1], sides[(di + 3) % 6][1]
        # wh.append(sides[di][1])
        # index.append(di)

# large = wh.pop() * wh.pop()
# small = sides[(index[-1] + 2) % 6][1] * sides[(index[-1] + 3) % 6][1]

area = large_w * large_h - small_w * small_h

print(area * K)



# ==============================================================================
# K = int(input())
# width = []
# height = []
# orderly = []
#
# for _ in range(6):
#     d, l = map(int, input().split())
#     orderly.append((d,l))
#     # 가로 세로 따로 담아두기
#     if d == 1 or d == 2:
#         width.append(l)
#     else:
#         height.append(l)
#
# max_wi = max_hi = 0
# # 가로와 세로 최댓값의 odrerly 내부 인덱스 찾기
# for idx in range(6):
#     # 가로
#     if orderly[idx][0] in range(1, 3) and orderly[idx][1] == max(width):
#         max_wi = idx
#     # 세로
#     elif orderly[idx][0] in range(2, 4) and orderly[idx][1] == max(height):
#         max_hi = idx
#
# print(orderly)
# # 인덱스 벗어나지 않게 앞뒤로 더해주고 인덱스 수정
# find = orderly * 3
# max_wi += 6
# max_hi += 6
#
# # 작은 사각형 찾기
# if max_wi < max_hi:
#     small = find[max_wi - 2][1] * find[max_hi + 2][1]
# else:
#     small = find[max_wi + 2][1] * find[max_hi - 2][1]
#
# # 큰 사각형
# large = max(width) * max(height)
#
# # 밭의 면적
# area = large - small
# print(area)
#
# # 참외 개수
# print(area * K)


# ==================================================================
# from pprint import pprint
#
# K = int(input())
# di = [0, 0, 0, 1, -1]
# dj = [0, 1, -1, 0, 0]
# field = [[0] * 1001 for _ in range(1001)]
#
# i = j = 499
# for _ in range(6):
#     d, l = map(int, input().split())
#     print(d, l)
#     if d == 1 or d == 2: # 동/서는 가로(행)만 챙기면 됨
#         for k in range(l):
#                 field[i][j+di[d]*k] = 1
#     else:
#         for k in range(l):
#             field[i+di[d]*k][j] = 1
#
# area = 0
# for i in range(1000):
#     for j in range(1000):
#         if field[i][j] == 1 and field[i+1][j+1] == 0:
#             field[i+1][j+1] = 1
# area = 0
# for i in range(1001):
#     for j in range(1001):
#         if field[i][j] == 1:
#             area += 1
#
# print(area)
#
#
# # ============================================================== #
# K = int(input()) # 참외의 수
# width = []
# height = []
#
# for _ in range(6):
#     d, l = map(int, input().split())
#     if d == 1 or d == 2: #동서 => 가로
#         width.append(l)
#     else:
#         height.append(l)
# print(width)
# print(height)
# # 인덱스 오류가 나지 않게 두배로 늘려줌
# width.extend(width)
# height.extend(height)
#
# # 최대 가로와 세로가 처음 등장하는 인덱스 찾기
# max_w = max(width)
# max_h = max(height)
#
# for idx in range(3):
#     if max_w == width[idx]:
#         max_w = idx
#     break
# for idx in range(3):
#     if max_h == height[idx]:
#         max_h = idx
#     break
#
# minus_w = max_w + 2
# minus_h = max_h + 2
# print(width)
# print(height)
# result = width[max_w] * height[max_h] - width[minus_w] * height[minus_h]
# print(result)

# ============================================================== #
# width = []
# height = []
# for _ in range(6):
#     d, l = map(int, input().split())
#     if d == 1 or d == 2: #동서 => 가로
#         width.append(l)
#     else:
#         height.append(l)
#
# # 면적 구하기
# area = max(width) * max(height) - min(width) * min(height)
#
# # 참외 개수 구하기
# result = area * K
# print(result)