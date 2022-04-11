from collections import deque
from pprint import pprint

# def clean_room(sy, sx, di, cnt):
    # cleaned = [[0] * M for _ in range(N)] # 방문 표시 배열
    # queue = deque()
    #
    # cleaned[sy][sx] = 1 # 현재 위치 청소
    # result = 1            # 청소 횟수 더하기
    # queue.append((sy, sx, di, cnt))
    #
    # dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
    #
    # while queue:
    #     y, x, dir, cnt = queue.popleft()
    #     # 바로 왼쪽에 청소하지 않은 빈 공간이 존재하는가
    #     while cnt < 4:
    #         ny, nx = y + dy[dir], x + dx[dir]
    #         if 0 <= ny < N and 0 <= nx < M and rooms[ny][nx] == 0 and cleaned[ny][nx] == 0:
    #             cleaned[ny][nx] = 1 # 청소 표시
    #             result += 1
    #             queue.append((ny, nx, (dir + 3) % 4, 0)) # 왼쪽 회전 후 청소할 수 있게 enQue
    #             break
    #         else:
    #             dir = (dir + 3) % 4 # 왼쪽 회전만
    #             cnt += 1            # 횟수 늘려
    #     if cnt == 4: # 다 채웠으면 뒤를 확인 해야함
    #         back = (dir + 3) % 4
    #         by, bx = y + dy[back], x + dx[back]
    #         if 0 <= by < N and 0 <= bx < M and rooms[by][bx] != 1 and cleaned[by][bx] == 0:
    #             queue.append((by, bx, dir, 0))
    #         else:
    #             return result

N, M = map(int, input().split())
r, c, d = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

rooms[r][c] = 2 # 현재 위치 청소 표시
result = 1      # 청소 횟수 더하기
queue = deque()
queue.append((r, c, d)) # 현재 위치, 방향, 횟수

dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]

while queue:
    y, x, di = queue.popleft()
    # 바로 왼쪽에 청소하지 않은 빈 공간이 존재하는가
    cnt = 1
    # while cnt < 4:
    for i in range(4):
        pprint(rooms)
        print()
        if i < 3:
            ny, nx = y + dy[di], x + dx[di] # 현재 위치의 바로 왼쪽
            if 0 <= ny < N and 0 <= nx < M and rooms[ny][nx] == 0:
                rooms[ny][nx] = 2 # 청소 표시
                result += 1
                queue.append((ny, nx, (di + 3) % 4)) # 왼쪽 회전 후 청소할 수 있게 enQue
                break
            else:
                di = (di + 3) % 4   # 왼쪽 회전만
                cnt += 1            # 횟수 늘려
        elif i == 3: # 다 채웠다! => 뒤를 확인 해야함
    # if cnt == 4: # 다 채웠으면
            back = (di + 3) % 4
            by, bx = y + dy[back], x + dx[back]
            if 0 <= by < N and 0 <= bx < M and rooms[by][bx] == 0:
                queue.append((by, bx, di, 0))
            else:
                break
print(result)