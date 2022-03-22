def total_score(gears):
    result = 0
    score = [0, 1, 2, 4, 8]
    for i in range(1, 5):
        if gears[i][0]:
            result += score[i]
    return result

# 톱니바퀴 정보 받기
gears = [[0] * 8]
for _ in range(4):
    gears.append(list(map(int,input())))
# 확인해야하는 톱니바퀴 인덱스 정리
a, b, c, d, e, f = gears[1][2], gears[2][-2], gears[2][2], gears[3][-2], gears[3][2], gears[4][-2]

# 회전 정보 받기
K = int(input())
for _ in range(K):
    gear_num, turns = map(int, input().split())
    if gear_num == 1:
        if a != b and turns == 1: #다르다 => 2번 움직임, 1번은 시계, 2번은 반시계
            gears[0].pop(0)


