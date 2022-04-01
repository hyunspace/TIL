A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
    B = B + C
    while B >= 60:
        B -= 60
        A += 1
else:
    B += C
if A >= 24:
    A -= 24

print(A, B)