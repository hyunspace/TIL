import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0 for _ in range(N)]
    # print(boxes)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        # print(L, R)
        for new_num in range(L-1, R):
            boxes[new_num] = i
    print(f'#{tc}', end=' ')
    print(*boxes)