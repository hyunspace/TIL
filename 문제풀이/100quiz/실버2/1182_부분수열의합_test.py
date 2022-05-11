# s_sum : 선택된 것의 합계
# s_cnt : 선택된 것의 개수
# s : 목표하는 원소의 합
# n : 원소의 개수
def dfs(level, s_sum):
    global sol
    # 가지치기
    if level > n or s_sum > s:
        return

    # 종료조건
    if s_sum == s:
        # n개의 원소를 가지고 있고 원소 합이 k인 부분집합
        sol += 1
        return

    dfs(level + 1, s_sum + arr[level])
    dfs(level + 1, s_sum)


n, s = map(int, input().split())
arr = list(map(int, input().split()))
sol = 0
dfs(0, 0)
print(sol)