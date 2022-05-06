# 5월 7일

def fibonacci(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fibonacci(k-1) + fibonacci(k-2)

n = int(input())

print(fibonacci(n))
