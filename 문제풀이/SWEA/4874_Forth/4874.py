import sys;sys.stdin = open('input.txt')

class Stack:

    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def is_Empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, n):
        # 원래라면 꽉 찼을 때 푸쉬하는 것도... 고려해야?
        self.top += 1
        self.arr[self.top] = n

    def pop(self):
        if self.is_Empty():
            return None
        else:
            result = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return result

    def peek(self):
        if not self.top == -1:
            return self.arr[self.top]
        else:
            return None

def postfix_cacluate(notes):
    # operators = Stack(256) => postfix 변환하는 거 아니라서 필요X
    postfix = Stack(256)
    # opt_dict = {'+': 1, '-': 1, '*': 2, '/': 2}
    # operator = ['+', '-', '*', '/']

    for n in notes:
        if n == '.':
            break
        elif n not in '+-*/':
            postfix.push(int(n))
        else:
            if postfix.top < 1:  # top이 1 미만이면 stack에 1개만 있거나 0개 => 연산X
                return 'error'
            a = postfix.pop()
            b = postfix.pop()
            if n == '+':
                postfix.push(a + b)
            elif n == '-':
                postfix.push(b - a)
            elif n == '*':
                postfix.push(a * b)
            else:
                postfix.push(b // a)
    if postfix.top == 0:
        return postfix.pop()
    else:
        return 'error'

T = int(input())

for tc in range(1, T+1):
    notes = list(input().split())
    print(f'#{tc} {postfix_cacluate(notes)}')



# for tc in range(1, T+1):
#     notes = list(input().split())
    # operators = Stack(256)
    # postfix = Stack(256)
    # # opt_dict = {'+': 1, '-': 1, '*': 2, '/': 2}
    # operator = ['+', '-', '*', '/']
    #
    # result = ''
    # for n in notes:
    #     if n == '.':
    #         break
    #     elif n not in operator:
    #         postfix.push(int(n))
    #     else:
    #         if postfix.top < 1: # top이 1 미만이면 stack에 1개만 있거나 0개 => 연산X
    #             result = 'error'
    #             break
    #         if n == '+':
    #             postfix.push(postfix.pop() + postfix.pop())
    #         elif n == '-':
    #             postfix.push(postfix.pop() - postfix.pop())
    #         elif n == '*':
    #             postfix.push(postfix.pop() * postfix.pop())
    #         else:
    #             postfix.push(postfix.pop() // postfix.pop())

    # if postfix.top == 0 and result != 'error':
    #     result = postfix.peek()
    # print(f'#{tc} {result}')
