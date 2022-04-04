import sys; sys.stdin = open('input.txt')

def bfs(s, turn):
    queue = []
    queue.append((s, turn))
    contacted[s] = turn  # 방문 처리
    while queue:
        s, turn = queue.pop(0)
        for j in range(101):
            if data[s][j] and contacted[j] == 0:
                contacted[j] = turn + 1
                bfs(data[s][j], contacted[j])
    else: # 마지막 노드
        return

for tc in range(1, 11):
    # 입력값
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    # 빈트리
    data = [[0]*101 for _ in range(101)]
    # 트리 채우기
    for i in range(N//2):
        data[arr[i*2]][arr[i*2+1]] = arr[i*2+1]

    contacted = [0 for _ in range(101)]
    bfs(start, 1)
    print(contacted)
    last_contact = max(contacted)
    possible = []
    for idx in range(101):
        if contacted[idx] == last_contact:
            possible.append(idx)

    print(f'#{tc} {max(possible)}')