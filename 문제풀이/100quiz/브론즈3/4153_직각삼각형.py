while True:
    legs = list(map(int, input().split()))
    legs.sort()
    a, b, c = legs
    if a == b == c == 0:
        break

    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')