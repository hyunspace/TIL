'''
이 아파트에 거주를 하려면 조건이 있는데,
“a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼
사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
'''

import sys; sys.stdin = open('2775.txt')

# 테스트 케이스의 수
T = int(input())
resi_list = [1]
# 테스크 케이스 수 만큼 전체를 반복반복
for tc in range(T):
    k = int(input()) #층
    n = int(input()) #호수
    print(f'{tc}번째 {k}층 {n}호 구하기')
    for j in range(k): #0층부터 k-1층까지
        for i in range(2, n+1): #2호부터 n호까지
            resi_list.append(i)
        print(resi_list)
