# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, 
# N번째 줄에는 별 N개를 찍는 문제

# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.


## Feb 10, 2022 ##

N = int(input())
for star in range(1, N + 1):
    print('*' * star)