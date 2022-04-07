import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_root(x):
    if roots[x] == x:
        return x
    roots[x] = find_root(roots[x])
    return roots[x]

n, m = map(int, input().split())
roots = [i for i in range(n+1)]

for _ in range(m):
    check, a, b = map(int, input().split())
    x = find_root(a)
    y = find_root(b)
    if check == 0:
        # 합치기
        if x < y:
            roots[y] = x
        else:
            roots[x] = y
    else:
        # 합집합인 지 확인
        if x == y:
            print('YES')
        else:
            print('NO')