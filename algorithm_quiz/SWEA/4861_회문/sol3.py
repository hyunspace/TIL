import sys; sys.stdin = open('input.txt')

def palindrome(N, M, words):

    # 가로로 회문 찾기
    # => 세로의 열은 고정하고 가로 인덱스를 바꿔가며 M만큼을 빼와야 한다
    for i in range(N):
        for j in range(N - M + 1):
            if words[i][j:j + M] == words[i][j:j + M][::-1]:
                return words[i][j:j + M]

    # 세로로 회문 찾기
    # => 가로의 열은 고정하고 세로로 행을 바꿔가면서 한 글자씩 빼와야 한다
    for j in range(N):
        for i in range(N-M+1):
            word = ''  # 한 글자씩 빼서 담을 변수
            for k in range(M):
                word += words[i+k][j]
            if word == word[::-1]:
                return word

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    words = [input() for _ in range(N)]
    print(f'#{tc} {palindrome(N, M, words)}')
