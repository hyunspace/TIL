import sys; sys.stdin = open('test.txt')

N, M = map(int, input().split())
# print(N, M)
words = [input() for _ in range(N)]

# print(words[0][0:5])
# print(words[0][4::-1])

# 가로로 회문 찾기
# for i in range(N):
#     for j in range(N-M+1):
#         print(words[i][j:j+M])
#         print(words[i][j+M-1:j:-1])


# 함수를 만들자 ㅎ
def palindrome(N, M):

    # 가로로 회문 찾기
    for i in range(N):
        if N == M:
            for j in range(N - M + 1):
                word = ''
                # print(words[i][j:j+M])
                # print(words[i][j+M-1::-1])
                # if words[i][j:j + M] == words[i][j + M - 1::-1]:
                word = words[i][j:j + M]
                if word == word[::-1]:
                    return word
        if N > M:
            for j in range(N - M + 1):
                word = ''
                # print(words[i][j:j+M])
                # print(words[i][j+M-1::-1])
                # if words[i][j:j + M] == words[i][j + M - 1:j - 1:-1]:
                word = words[i][j:j + M]
                if word == word[::-1]:
                    return word

    # # 세로로 회문 찾기
    for j in range(N):
        if N == M:
            word = ''
            for i in range(N):
                word += words[i][j]
            if word == word[::-1]:
                return word
        if N > M:
            for i in range(N-M):
                for idx in range(i, i+M):
                    word = ''
                    word += words[i][j]
                    print(word)
                    if word == word[::-1]:
                        return word

print(palindrome(N, M))
