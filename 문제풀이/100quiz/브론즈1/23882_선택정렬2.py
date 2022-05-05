# 5월 5일

import sys
sys.setrecursionlimit(10**6) # 없으면 RecursionError!

def selection_sort(A, n, cnt):
    # 모든 정렬이 끝났을 때 교환 횟수 cnt가 K보다 작을 때
    if n == 0 and K > cnt:
        return print(-1)

    # 아직 정렬 해야한다면
    max_num = A[0]               # 배열 맨 앞의 숫자
    max_idx = 0                  # 배열 첫 인덱스
    for idx in range(n):         # 순회하면서
        if max_num < A[idx]:     # 더 큰 숫자가 등장하면
            max_num = A[idx]     # 최대값 갱신
            max_idx = idx        # 해당 최대값의 인덱스 갱신
    if max_idx != n - 1:         # 조사 마지막 자리에 있는게 아니라면
        A[max_idx], A[n-1] = A[n-1], A[max_idx] # 위치를 바꿔서 맨 뒤로 보내자
        cnt += 1                 # 바꿨으니 정렬 횟수 + 1
    if K == cnt:                 # K번 교환 발생 직후라면
        return print(*A)         # 배열 A 출력
    else:
        selection_sort(A, n-1, cnt) # 아니라면 다시 정렬하러 가기


N, K = map(int, input().split())
arr = list(map(int, input().split()))
selection_sort(arr, N, 0)