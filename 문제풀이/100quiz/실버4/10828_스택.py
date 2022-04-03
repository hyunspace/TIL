import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    orders = list(input().split())
    order = orders[0]
    if order == 'push':
        stack.append(int(orders[1]))
    elif order == 'pop':
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

