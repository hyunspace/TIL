import sys; sys.setrecursionlimit(10**6)

def use_elevator(s, cnt):
    visited[s] = 1 # 방문표시
    cnt += 1

    if s == goal: # 도착
        return cnt-1 # 횟수 반환

    if s + up <= F and visited[s+up] == 0: # 올라갈 수 있다
        use_elevator(s+up, cnt)
    if s - down >= 1 and visited[s-down] == 0: # 내려갈 수 있다
        use_elevator(s-down, cnt)

F, start, goal, up, down = map(int, input().split())

visited = [0 for _ in range(F+1)]
ans = use_elevator(start, 0)
if ans:
    print(ans)
else:
    print('use the stairs')