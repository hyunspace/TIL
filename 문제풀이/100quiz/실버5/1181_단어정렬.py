# 4월 24일

N = int(input())
words = [[] for _ in range(51)]

# 글자길이에 맞춰서 넣기
for _ in range(N):
    word = input()
    words[len(word)].append(word)

# 글자길이 순으로 출력 + 여러개라면 정렬하고, 중복 없애고 출력
for x in words:
    if len(x) == 1:
        print(*x)
    else:
        x = set(x)
        new_x = []
        for y in x:
            new_x.append(y)
        new_x.sort()
        for ny in new_x:
            print(ny)