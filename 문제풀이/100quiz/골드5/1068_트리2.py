# 4월 16일
# 입력값
V = int(input())
parent = list(map(int, input().split()))
del_node = int(input())
tree = [[] for _ in range(V)]
for i in range(V):
    if


# from collections import deque
#
# # 입력값
# V = int(input())
# parent = list(map(int, input().split()))
# del_node = int(input())
# child1 = [0 for _ in range(V)] #왼자식
# child2 = [0 for _ in range(V)] #오른자식
#
# for idx in range(1, V):
#     if child1[parent[idx]] == 0: # 왼쪽 자식 비었으면
#         child1[parent[idx]] = idx
#     else:                         # 왼쪽 자식 O => 오른쪽 자식
#         child2[parent[idx]] = idx
#
# print(child1)
# print(child2)
#
# # 노드 지우기
# stack = deque()
# stack.append(del_node)
# while stack:
#     x = stack.popleft()
#     if child1[x]:
#         stack.append(child1[x])
#         child1[x] = 0
#     if child2[x]:
#         stack.append(child2[x])
#         child2[x] = 0
# for node in range(V):
#     if child1[node] == del_node:
#         child1[node] = 0
#     if child2[node] == del_node:
#         child2[node] = 0
#
# print(child1)
# print(child2)
# ans = V-1
# for i in range(V):
#     if i != del_node:
#         if child1[i] or child2[i]:
#             pass
#         else:
#             ans -= 1
# print(ans)