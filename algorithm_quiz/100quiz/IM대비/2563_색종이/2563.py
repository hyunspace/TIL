import sys; sys.stdin = open('input.txt')

canvas = [[0] * 101 for _ in range(101)]

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            canvas[i][j] += 1

    # 이 아래 indentation에 의해서 답이 갈림
    # 테스트 케이스 결과는 같은데!
    # 반복하면서 계속 area 리셋하면 결국 마지막 값만 보는거 아닌가..?
    area = 0
    for i in range(101):
        for j in range(101):
            if canvas[i][j] >= 1:
                area += 1

print(area)