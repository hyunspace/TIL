# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

'''
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )
'''

## Feb 10, 2022 ##

import sys; sys.stdin = open('input.txt')

T = int(input())


# 테스트 케이스 개수만큼 반복
for tc in range(1, T+1):
    # 카드를 숫자대로 담아둘 빈 리스트
    cards = [0] * 10
    N = int(input())
    numbers = list(map(int, input())) # 의문!!! 여기서 split하니까 오히려 통째로 들어가고 안하면 알아서 나눠서 들어감
    '''map(function, iterable) => 순회 가능한 객체가 들어가는데, 현재 주어진 값은 띄어쓰기X 그냥 넣어도 알아서 됨 split의 기준은 띄어쓰기~'''
    # 카드를 돌면서
    for i in range(N):
        # 카드의 숫자를 세서 해당하는 cards 리스트에 담아줌
        cards[numbers[i]] += 1
    # 개수를 담아둔 cards 리스트에서 최댓값이 담긴 인덱스와 해당 값을 출력해줘야함
    # 최댓값이 나올때마다 담아줄 변수
    max_cnt = 0
    max_idx = 0
    for j in range(10):
        if max_cnt <= cards[j]:
            max_cnt = cards[j]
            max_idx = j
    print(f'#{tc} {max_idx} {max_cnt}')





