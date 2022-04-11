numbers = [0] * 7
cubes = list(map(int, input().split()))
# 자기 자리에 넣기
for i in cubes:
    numbers[i] += 1

if 3 in numbers: # 같은 눈 3개
    ans = 10000 + numbers.index(3) * 1000
    print(ans)
elif 2 in numbers: # 같은 눈 2개
    ans = 1000 + numbers.index(2) * 100
    print(ans)
else:
    max_idx = 0
    for idx in range(6, 0, -1):
        if numbers[idx] == 1:
            max_idx = idx
            break
    ans = max_idx * 100
    print(ans)
