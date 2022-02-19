import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    primes = [2, 3, 5, 7, 11]
    cnt = 0
    result = []

    for prime in primes:
        while N % prime == 0:
            N = N // prime
            cnt += 1
        result.append(cnt)
        cnt = 0

    # print(f'#{tc} ', end='')
    # print(*result)
    print(f'#{tc} ', *result)