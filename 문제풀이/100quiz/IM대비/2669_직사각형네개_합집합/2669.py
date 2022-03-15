import sys; sys.stdin = open('input.txt')

# 전체 모눈판 (인덱스랑 일치시키기 위해서 101까지)
grid = [list([0] * 101) for _ in range(101)]
# print(grid)

for N in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # x는 가로, y는 세로
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] += 1

    # 전체 모눈판에서 1이상, 즉 사각형이 1개 이상 차지한 영역 구하기
    result = 0
    for row in range(101):
        for col in range(101):
            if grid[row][col] >= 1:
                result += 1
print(result)