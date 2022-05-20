# 5월 20일

N, M = map(int, input().split())
nset = set(input() for _ in range(N))
mset = set(input() for _ in range(M))
nmset = nset&mset

ans = len(nmset)
ans_list = []
for nm in nmset:
    ans_list.append(nm)
print(ans)
for nm in sorted(ans_list):
    print(nm)