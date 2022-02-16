## Feb 8

# 셀프 넘버 함수 정의하기
# def self():
#     # 10000 이하의 정수 중에서 셀프 넘버인 애들을 찾아보자
#     num_list = []
#     for num in list(range(1, 10001)):
#         if num < 100:
#             num_list += [num + num//10 + num%10]
#         elif num < 1000:
#             num_list += [num + num//10*2 + num%10]
    # while len(list(range(1, 100+1))) >= len(num_list):

    # for num in list(range(1, 100+1)):
    #     for idx in str(num):
    #         num_list += [num + int(num[idx])]
    # print(num_list)
    # for nn in range(1, 100+1):
    #     if nn in num_list:
    #         continue
    #     # print(nn)



### Feb 15 ###

'''
1. 1부터 10000까지 리스트에 담아놨다가
2. 생성자가 있는 숫자를 빼버리자...!
    이미 빼버린 경우에는 오류가 나지 않도록 주의할 것
---
1. d(n) 함수를 일단 만들어서
2. 1부터 10000까지 돌리면서 숫자가 나오면 담아 놨다가 (set)
3. 1부터 10000까지 담긴 set에서 빼버리자 (집합처럼!)
'''

# d(n) 함수 만들기 => 재귀를 사용하자 or while문
def d(n):
    result = n
    while n > 0:
        result += n % 10
        n = n // 10
    return result

numbers = list(range(1, 11))
print(numbers)
not_self = []
for num in numbers:
    not_self.append(d(num))
    if d(num) in numbers:
        numbers.remove(d(num))
print(not_self)
print(numbers)

print('=====')
# 1부터 10000까지 순회하면서 생성자를 만들어보자
numbers = list(range(1, 101))
not_self = []
for num in numbers:
    not_self.append(d(num))
    if d(num) in numbers:
        numbers.remove(num)
print(numbers)