## Feb 08, 2022

h, m = map(int, input().split())

mm = m - 45
if mm < 0:
    mm += 60
    if h == 0:
        h = 23
    else:
        h -= 1
    print(h, mm)
else:
    print(h, mm)