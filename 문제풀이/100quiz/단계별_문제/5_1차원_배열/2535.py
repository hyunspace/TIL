# 9개의 서로 다른 자연수가 주어질 때,
# 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.


### Feb 10 ###

# T = 9
# numbers = []
# for _ in range(T):
#     numbers += [int(input())]

# max_idx = 0
# for i in range(T-1):
#     if numbers[i] <= numbers[i+1]:
#         max_idx = i+1

'''
if문에 문제가 있었다!!!!!!!!!!

엣지 케이스
>> 1 72 77 66 34 21 2 3 9
77을 최댓값으로 여기다가 뒤에서 3, 9 비교하면 9로 바꿔버림 ㅠㅠ
'''

# print(numbers[max_idx])
# print(max_idx + 1)

# numbers = []
# for _ in range(9):
#     numbers.append(int(input()))

# print(max(numbers))
# print(numbers.index(max(numbers))+1)


### Feb 11 ###

numbers = []
for _ in range(9):
    numbers += [int(input())]

max_num = numbers[0]
max_idx = 0 # 이거 정의 안하니까 NameError
for i in range(9):
    if max_num < numbers[i]:
        max_num = numbers[i]
        max_idx = i
        
print(numbers[max_idx])
print(max_idx + 1)