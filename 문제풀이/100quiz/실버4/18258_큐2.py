# 4월 27일
from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
N = int(input())
for _ in range(N):
    command = input().split()
    x = command[0]
    if x == 'push':
        queue.append(command[1])
    elif x == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif x == 'size':
        print(len(queue))
    elif x == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif x == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif x == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)