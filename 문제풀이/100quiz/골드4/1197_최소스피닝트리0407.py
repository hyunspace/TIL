def find_root(x):
    if roots[x] == x:
        return x
    else:
        return find_root(roots[x])

def union(x, y):
    if x < y:
        roots[y] = x
        # 아래 for문 돌리는 건 그룹 찾을 때만! 지금은 필요 없다.
    else:
        roots[x] = y

V, E = map(int, input().split())
roots = [i for i in range(V+1)] # make set
data = []
for _ in range(E):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x:x[2])

ans = 0
for a, b, c in data:
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root != b_root:
        union(a_root, b_root)
        ans += c
print(ans)