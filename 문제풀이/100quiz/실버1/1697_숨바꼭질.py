from collections import deque

def bfs(n, k):
    queue = deque()
    visited = [0 for _ in range(100001)] # 인덱스 에러 주의!
    visited[n] = 1 # 방문 표시
    queue.append(n)
    while queue:
        size = len(queue)
        for _ in range(size):
            now_n = queue.popleft()
            if now_n == k: # 동생 만났으면
                return print(visited[now_n] - 1)
            # 못 만났으면 걷거나 순간이동해야지 (탐색하기)
            # 걷기
            for d in [-1, 1]:
                next_n = now_n + d
                if 0 <= next_n <= 100000 and visited[next_n] == 0:
                    visited[next_n] = visited[now_n] + 1
                    queue.append(next_n)
            # 순간 이동
            next_n = now_n * 2
            if 0 <= next_n <= 100000 and visited[next_n] == 0:
                visited[next_n] = visited[now_n] + 1
                queue.append(next_n)

N, K = map(int, input().split())
maps = [0 for _ in range(100000)]

bfs(N, K)