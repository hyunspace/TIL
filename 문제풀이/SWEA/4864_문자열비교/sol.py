import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    short = input()
    long = input()

    # for l_char in long:
    #     for s_char in short:
    #         if l_char == s_char:
    #             checker += 1

    # Brute Force(고지식한 알고리즘)
    s = 0 # 검색할 짧은 단어의 인덱스
    l = 0 # 검색 대상인 긴 단어의 인덱스
    while s < len(short) and l < len(long): # 각 단어가 끝날 때까지 반복
        if short[s] != long[l]: # 일치하지 않는다면
            l = l - s           # 검색 대상은 다음으로 넘어가야하고
            s = -1              # 짧은 검색어는 0부터 재탐색 해야한다
        l += 1
        s += 1
    if s == len(short):     # 일치한다면
        print(f'#{tc} 1')   # 1을 출력
    else:                   # 불일치한다면
        print(f'#{tc} 0')   # 0을 출력
