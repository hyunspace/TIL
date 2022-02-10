# 9개의 서로 다른 자연수가 주어질 때,
# 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.


### Feb 10 ###

T = 9
numbers = []
for _ in range(T):
    numbers += [int(input())]

max_idx = 0
for i in range(T-1):
    if numbers[i] < numbers[i+1]:
        max_idx = i+1

print(numbers[max_idx])
print(max_idx + 1)


numbers = []
for _ in range(9):
    numbers.append(int(input()))

print(max(numbers))
print(numbers.index(max(numbers))+1)