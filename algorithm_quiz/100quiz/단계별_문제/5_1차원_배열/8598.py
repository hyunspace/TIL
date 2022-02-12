'''

'''

import sys; sys.stdin = open('8598.txt')

### Feb 12, 2022 ###

# 테스트 케이스의 수
T = int(input())

for tc in range(T):
    # 주어진 O, X를 리스트에 담기
    test = list(input())
    # O의 점수를 누적할 변수와 총점을 담을 변수
    combo = 0
    result = 0
    # 리스트를 순회하면서
    for i in range(len(test)):
        # O가 나오면 combo에 누적! => result에 더하기!
        if test[i] == 'O':
            combo += 1
            result += combo
        # X가 나오면 combo는 리셋
        else:
            combo = 0
    print(result)
