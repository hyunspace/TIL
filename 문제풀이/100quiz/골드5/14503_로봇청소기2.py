from pprint import pprint

N, M = map(int, input().split())
r, c, d = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]
# cleaned = [[0] * M for _ in range(N)]

ans = 1 # 시작 위치는 청소 완료!
turns = 0
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

while True:
    # 왼쪽으로 회전 후
    d = (d + 3) % 4
    # 앞으로 한 칸
    nr, nc = r + dr[d], c + dc[d]
    # 아직 청소 X + 청소 가능한 곳?
    if rooms[nr][nc] == 0:
        rooms[nr][nc] = 2 # 청소 완료
        ans += 1          # 청소 했으니까 세기
        turns = 0         # 회전 횟수 초기화(2a에서 1번으로 돌아갔으므로)
        r, c = nr, nc     # 현재 위치로 바꿔줌
        continue
    # 청소 불가능한 곳 => 돌아야...
    else:
        turns += 1

    if turns == 4: # 돌만큼 돌았다
        # 후진하자
        d = (d + 2) % 4
        nr, nc = r + dr[d], c + dc[d]
        if rooms[nr][nc] != 1: # 벽이 아님 => 후진 가능!
            r, c = nr, nc
        else: # 후진해도 더이상 청소 불가능
            break
        turns = 0
print(ans)