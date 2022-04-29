# 4월 30일

from collections import deque

def check_vps(ps):
    for p in ps:
        if p == '(':
            queue.append(p)
        else: # 닫는 괄호
            if len(queue) > 0 and queue.popleft() == '(':
                continue
            else:
                return print('NO')
    if queue:
        return print('NO')
    else:
        return print('YES')


T = int(input())
for _ in range(T):
    queue = deque()
    ps = input()
    check_vps(ps)