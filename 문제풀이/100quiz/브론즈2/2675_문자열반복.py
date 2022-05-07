# 5월 8일

T = int(input())
for tc in range(T):
    R, S = input().split()
    R = int(R)
    P = ''

    for char in S:
        for _ in range(R):
            P += char
    print(P)