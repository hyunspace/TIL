from collections import deque

def bfs(start, goal):
    queue = deque()
    visited = [0 for _ in range(N+1)] # 방문 배열
    visited[start] = 1  # 방문 표시
    queue.append(start) # enQue
    while queue:
        # 탐색 범위 정해주기
        size = len(queue)
        for _ in range(size):
            now_node = queue.popleft()
            if now_node == goal:  # 도착했다면
                return print(visited[now_node] - 1)
            # 주변 노드로 이동하자
            for next_node in data[now_node]:
                if visited[next_node[0]] == 0:
                    visited[next_node[0]] = visited[now_node] + next_node[1]
                    queue.append(next_node[0])


# input 값 받아오기 => 출력까지
N, M = map(int, input().split()) # N개의 노드, 궁금한 노드 M쌍 정보
data = [[] for _ in range(N+1)] # 노드 연결과 거리 정보
for _ in range(N-1):
    node1, node2, distance = map(int, input().split())
    data[node1].append((node2, distance))
    data[node2].append((node1, distance))
# print(data)
for _ in range(M):
    start, goal = map(int, input().split())
    bfs(start, goal)
