from collections import deque

def find_paths(si, sj, total, flag):
    visited = [[0] * N for _ in range(N)]
    queue = deque()

    queue.append((si, sj, total, flag))
    visited[si][sj] = 1

    while queue: # 큐 안에 있으면 반복
        y, x, total, flag = queue.popleft()





N = int(input())
maps = [[] for _ in range(N)]
for i in range(N):
    temp = input().split()
    if i % 2 == 0: # 숫자 연산자 숫자 연산자
        for j in range(N):
            if j % 2 == 0: # 숫자
                maps[i].append(int(temp[j]))
            else:
                maps[i].append(temp[j])
    else: # 연산자 숫자 연산자 숫자
        for j in range(N):
            if j % 2 == 0: # 연산자
                maps[i].append(temp[j])
            else:
                maps[i].append(int(temp[j]))

min_path = N**2
max_path = 0

find_paths(0, 0, 0, -1)

