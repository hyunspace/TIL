# def push_front(X):
#     global deque
#     deque = [X] + deque
#
# def push_back(X):
#     deque.append(X)
#
# def pop_front(arr):
#     if empty(arr):
#         return -1
#     else:
#         return deque.pop(0)
#
# def pop_back(arr):
#     if empty(arr):
#         return -1
#     else:
#         return deque.pop(-1)
#
# def size():
#     return len(deque)
#
# def empty(arr):
#     if arr:
#         return 0
#     else:
#         return 1
#
# def front(arr):
#     if empty(arr):
#         return -1
#     else:
#         return arr[0]
#
# def back(arr):
#     if empty(arr):
#         return -1
#     else:
#         return arr[-1]

# import sys
# input = sys.stdin.readline
#
# class Deque():
#     def __init__(self):
#         self.arr = []
#         self.size = len(self.arr)
#         self.front = 0
#         self.back = -1
#
#     def push_back(self, X):
#         self.arr = [X] + self.arr
#
#     def push_back(self, X):
#         self.arr.append(X)
#
#     def pop_front(self):
#         se
#
import sys

arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push_front':
        arr = [int(order[1])] + arr
    elif order[0] == 'push_back':
        arr.append(int(order[1]))
    elif order[0] == 'pop_front':
        if arr:
            print(arr.pop(0))
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if arr:
            print(arr.pop(-1))
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)