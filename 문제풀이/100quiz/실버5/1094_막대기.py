# 5월 1일

X = int(input())
poles = [64]

while sum(poles) > X:
    x = poles[-1] // 2
    poles[-1] = x
    if sum(poles) >= X:
        continue
    else:
        poles.append(x)

print(len(poles))