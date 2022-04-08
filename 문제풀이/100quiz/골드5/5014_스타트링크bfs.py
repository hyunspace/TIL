from collections import deque

def use_elevator(s, cnt):
    visited = [0 for _ in range(F+1)]
    queue = deque()

    queue.append((s, cnt))
    visited[s] = 1

    while queue: # 반복 조건
        now_floor, cnt = queue.popleft()

        if now_floor == goal: # 도착했으면
            return print(cnt) # 누른 횟수 출력하고 종료

        go_up = now_floor + up
        go_down = now_floor - down
        # 1층부터니까 범위는 1부터여야ㅠㅠ!!!!
        if 1 <= go_up <= F and visited[go_up] == 0: # 범위 내 + 방문X
            visited[go_up] = 1
            queue.append((go_up, cnt+1))
        if 1 <= go_down <= F and visited[go_down] == 0:
            visited[go_down] = 1
            queue.append((go_down, cnt+1))
    return print('use the stairs')

F, start, goal, up, down = map(int, input().split())

use_elevator(start, 0)