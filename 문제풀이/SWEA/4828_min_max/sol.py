# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

'''
줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
'''
## Feb 10, 2022 ##

import sys; sys.stdin = open('input.txt')


# 첫 줄에 주어지는 테스트 케이스의 수 T
T = int(input())

# 테스트 케이스의 수만큼 계산을 반복한다
for tc in range(1, T+1):
    # 케이스의 첫 줄에 주어진 양수의 개수 N
    N = int(input())
    # 다음 줄에 들어올 양수를 담을 빈 리스트
    numbers = []
    # 양수를 나눠서 리스트에 담는다
    numbers = list(map(int, input().split()))
    # 양수의 개수만큼 반복문을 돈다
    # 가장 큰 수를 담을 변수
    # max_num = numbers[0] => 필요X 그냥 앞 뒤 두 개씩 비교 하면 됨
    # for idx in range(0, N-1):
    #     if numbers[idx] < numbers[idx+1]:
    #         numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
    # print(numbers)
    '''버블 정렬
    뒤에서부터 하나씩 범위를 줄여오면서 비교하면 됨'''
    for i in range(N-1, 0, -1):
        for j in (range(0, i)): # i-1까지만 순회하므로 IndexError XX
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(f'#{tc} {numbers[N-1]-numbers[0]}')

