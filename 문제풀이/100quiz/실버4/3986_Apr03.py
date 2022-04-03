def find_good(word):
    if len(word) % 2: # 홀수라면
        return 0

    # 짝수라면 일단 통과
    stack = [] # 한 글자씩 확인해서 넣어줄 스택
    idx = 0    # 인덱스의 시작은 0
    stack.append(word[idx]) # 첫 단어 넣어주기
    idx += 1                # 넣어줬으니 +1

    while idx < len(word): # 단어 확인 중이라면
        if len(stack) == 0:
            stack.append(word[idx])
            idx += 1
        # 단어 확인 중
        if stack[-1] == word[idx]: # 같다면
            stack.pop(-1) # 맨 뒤에 글자 빼고
            idx += 1
        else: # 다르다면
            stack.append(word[idx])
            idx += 1
    if idx >= len(word) and stack:  # 단어 확인은 끝났는데 스택은 남아 있으면 => 안 맞는 것
        return 0
    return 1

N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    cnt += find_good(word)
print(cnt)