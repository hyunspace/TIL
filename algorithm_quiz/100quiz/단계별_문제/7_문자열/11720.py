'''
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다.
둘째 줄에 숫자 N개가 공백없이 주어진다.
'''


### Feb 13, 2022 ###

N = int(input())
# 두 번째 줄의 숫자를 나눠서 하나씩 리스트에 담기
numbers = list(map(int, input()))
# 누적해서 더할 변수
result = 0

for num in numbers:
    result += num

print(result)