from pprint import pprint


N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())
apples = []
for _ in range(K):
    row, column = map(int, input().split())g
    apples.append([row, column])

for apple in apples:
    for i in range(N):
        for j in range(N):
            if apple[0] == i and apple[1] == j:
                board[i][j] = 1

L = int(input()) #뱀의 방향 변환 횟수
moves = []
for _ in range(L):
    X, C = input().split()
    moves.append([int(X), C])
    
