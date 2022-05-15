import math

M, N = map(int, input().split())

def prime_number(number):
    if 1 < number <= 2:
        return number
    for n in range(2, number + 1):
        if number % n:
            pass


for num in range(M, N+1):
    if 1 < num <= 2:
        print(num)
    elif num > 3:
        flag = 1
        end = int(math.sqrt(num))
        for n in range(2, end + 1):
            if num % n == 0:
                flag = 0
                break
        if flag:
            print(num)

