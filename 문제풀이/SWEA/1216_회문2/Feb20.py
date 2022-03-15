import sys; sys.stdin = open('input.txt')

def max_palindrome(arr):
    max_len = palin_len = 0
    for k in range(100, 0, -1):
        for i in range(100):
            for j in range(0, 101 - k):
                word = arr[i][j:j + k]
                if word == word[::-1]:
                    palin_len = k
                if max_len < palin_len:
                    max_len = palin_len
    return max_len

for T in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    # print(arr)

    # 가로로 확인
    row_max = max_palindrome(arr)

    # 세로로 확인
    column_arr = list(map(list, zip(*arr)))
    column_max = max_palindrome(column_arr)
    # print(column_max)

    # 둘 중에 큰 값을 반환
    if row_max > column_max:
        print(f'#{tc} {row_max}')
    else:
        print(f'#{tc} {column_max}')
