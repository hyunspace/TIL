import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    words = [input() for _ in range(N)]

    result = '' # 찾은 회문 넣어둘 변수
    # 가로로 회문 찾기
    for i in range(N):
        if N == M:
            for j in range(N-M+1):
                # print(words[i][j:j+M])
                # print(words[i][j+M-1::-1])
                if words[i][j:j+M] == words[i][j+M-1::-1]:
                    result = words[i][j:j+M]
                    break
        if N > M:
            for j in range(N-M+1):
                # print(words[i][j:j+M])
                # print(words[i][j+M-1::-1])
                if words[i][j:j+M] == words[i][j+M-1:j-1:-1]:
                    result = words[i][j:j+M]
                    break

    # # 세로로 회문 찾기
    for i in range(N):
        word = ''
        for j in range(N-M+1):
            word += words[j][i]
        if word == word[::-1]:
            result = word
            break

    print(f'#{tc} {result}')



