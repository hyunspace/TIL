import sys
input = sys.stdin.readline

N = int(input())
poles = []
for _ in range(N):
    poles.append(int(input()))

max_height = 0 # 최고 높이
visible = 0 # 보이는 건물 수
# 뒤에서부터 확인하기
for idx in range(N-1, -1, -1):
    if max_height < poles[idx]:
        max_height = poles[idx]
        visible += 1
print(visible)