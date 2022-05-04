# 5월 5일

def selection_sort(A, n, cnt):
    max_num = A[0]
    max_idx = 0
    for idx in range(n):
        if max_num > A[idx]:
            max_num = A[idx]
            max_idx = idx
    A[idx], A[n] = A[n], A[idx]
    cnt += 1
    if K == cnt:
        return print(A)
    elif K > cnt:
        pass


N, K = map(int, input().split())
arr = list(map(int, input().split()))
selection_sort(arr, N)