import sys; sys.stdin = open('input.txt')

def palindrome(N, M, words):

    # 가로로 회문 찾기
    # => 세로의 열은 고정하고 가로 인덱스를 바꿔가며 M만큼을 빼와야 한다
    if N == M: # 찾으려는 단어의 길이와 행렬의 크기가 같을 때
        for i in range(N):
            word = words[i]
            if word == word[::-1]:
                return word
    else: # 찾으려는 단어의 길이와 행렬의 크기가 다를 때 => 단어가 더 짧음
        for i in range(N):
            for j in range(N - M + 1):
                word = words[i][j:j + M]
                if word == word[::-1]:
                    return word

    # 세로로 회문 찾기
    # => 가로의 열은 고정하고 세로로 행을 바꿔가면서 한 글자씩 빼와야한다
    if N == M: # 찾으려는 단어의 길이와 행렬의 크기가 같을 때
        for j in range(N):
            word = '' # 한 글자씩 빼서 담을 변수
            for i in range(N):
                word += words[i][j]
            if word == word[::-1]:
                return word

    else: # 단어가 더 짧을 때
        for j in range(N):
            for i in range(N-M+1):
                word = '' # 한 글자씩 빼서 담을 변수
                for idx in range(i, i+M):
                    word += words[i+idx][j]
                if word == word[::-1]:
                    return word

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    words = [input() for _ in range(N)]
    print(f'#{tc} {palindrome(N, M, words)}')
