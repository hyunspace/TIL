N = int(input())
cnt = 0

def good_word(word):
    # 홀수라면 무조건 좋은 단어 X
    if len(word) % 2:
        return 0
    elif word.count('A') % 2 or word.count('B') % 2:
        return 0

    # 짝수라면 가능성!
    stack = []
    for i in word:
        if not stack: # 비어있으면
            stack.append(i) # 그냥 넣어도 됨
            continue
        elif len(stack) == 1 and stack[-1] != i:
            stack.append(i)
        elif i == stack[-1]: # 마지막 값이랑 같으면
            stack.pop(-1)
            continue
        else: # 다르면 좋은 단어 X
            return 0
    return 1

for _ in range(N):
    word = input()
    cnt += good_word(word)
print(cnt)