# 4월 17일

N, M = map(int, input().split()) # 세로(행) N, 가로(열) M!!!!!!
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

room[r][c] = 2 # 1. 시작점 청소
ans = 1        # 청소 횟수 + 1
turn = 0       # 몇 번 회전 했는지 세는 변수

while True:
    new_d = (d + 3) % 4 # 2-a. 왼쪽으로 회전
    nr, nc = r + dr[new_d], c + dc[new_d] # 2-a. 앞으로 한 칸
    if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0: # 범위 내 + 청소 X
        room[nr][nc] = 2 # 1. 현재 위치 청소
        ans += 1          # 청소 횟수 세기
        r, c = nr, nc     # 다음 탐색을 위한 청소기 위치 반영
        d = new_d         # 다음 탐색을 위한 방향 반영
        turn = 0          # 1로 돌아가면 되므로 회전 횟수 초기화

    else:                 # 2-b. 왼쪽으로 한 번 더 회전
        d = new_d         # 위치는 그대로, 방향만 회전한 채로 넘기기
        turn += 1         # 회전 횟수 세기

    if turn == 4:             # 최대 회전 횟수를 채웠다!
        new_d = (d + 2) % 4   # 뒤쪽을 확인하자
        nr, nc = r + dr[new_d], c + dc[new_d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1: # 범위 내 + 후진 가능
            r, c = nr, nc     # 후진 위치 반영
            turn = 0          # 1로 돌아가면 되므로 회전 횟수 초기화
        else: # 후진 불가능
            break

print(ans)


# 참고 코드 : https://data-flower.tistory.com/60