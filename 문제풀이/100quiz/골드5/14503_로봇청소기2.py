from collections import deque
from pprint import pprint

N, M = map(int, input().split())
r, c, d = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

'''
queue에 들어가 있는 애들 => 청소 후보 
'''

ans = 0
queue = deque()
queue.append((r, c, d)) # 현재 위치, 방향, 횟수

dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]

while queue:
    y, x, di = queue.popleft()

    if rooms[y][x] == 0: # 청소 가능한 곳이면
        ans += 1
        rooms[y][x] = 2  # 청소 표시

    for i in range(4):
        if i < 3: # 3이하일 때는 여러번 시도 괜찮음
            nd = (di + 3) % 4
            ny, nx = y + dy[nd], x + dx[nd] # 현재 위치의 바로 왼쪽
            if 0 <= ny < N and 0 <= nx < M and rooms[ny][nx] == 0:
                queue.append((ny, nx, nd))
                break
            else:
                di = (di + 3) % 4   # 왼쪽 회전만
        elif i == 3: # 다 채웠다! => 뒤를 확인 해야함
            back = (di + 3) % 4
            by, bx = y + dy[back], x + dx[back]
            if 0 <= by < N and 0 <= bx < M and rooms[by][bx] == 0:
                queue.append((by, bx, di))
            else:
                break
print(ans)