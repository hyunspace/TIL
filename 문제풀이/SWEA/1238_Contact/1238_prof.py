import sys; sys.stdin = open('input.txt')

def bfs(s, turn):
    # 최종 결과 초기화 하면서
    result = [0, 0]
    queue = []
    queue.append((s, turn))
    visited[s] = 1
    while queue:
        s, turn = queue.pop(0)
        for idx in range(101):
            if tree[s][idx] and visited[idx] == 0:
                visited[idx] = 1
                if result[1] < turn:
                    result = [tree[s][idx], turn]
                elif result[1] == turn and result[0] < tree[s][idx]:
                    result = [tree[s][idx], turn]
                queue.append((idx, turn+1))
    return result

for tc in range(1, 11):
    # 입력값
    N, start = map(int, input().split())
    data = list(map(int, input().split()))

    # 빈 행렬
    tree = [[0]*101 for _ in range(101)]
    # 인접행렬 표시
    for i in range(N//2):
        tree[data[i*2]][data[i*2+1]] = data[i*2+1]

    # 방문 표시
    visited = [0 for _ in range(101)]

    # 시작점, 방문 횟수
    ans = bfs(start, 0)

    print(f'#{tc} {ans[0]}')