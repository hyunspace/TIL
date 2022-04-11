from collections import deque

# def yes_or_no(s):
#     for i in range(length):
#         if s[i] not in '[(])': # 알파벳은 패스
#             continue
#         elif s[i] == '[' or s[i] == '(':
#             stack.append(s[i])
#         elif len(stack) >= 1:
#             if s[i] == ']':
#                 if stack.pop(-1) == '[':
#                     continue
#                 else:
#                     return print('no')
#             elif s[i] == ')':
#                 if stack.pop(-1) == '(':
#                     continue
#                 else:
#                     return print('no')
#     if len(stack) > 0:
#         return print('no')
#     return print('yes')

def yes_or_no(s):
    stack = []
    # 괄호가 아니면 일단 패스
    for i in range(length):
        if s[i] not in '[(])':
            continue
        elif s[i] == '[' or s[i] == '(':
            stack.append(s[i])
        elif s[i] == ']':
            if len(stack) > 0 and stack.pop(-1) == '[':
                continue
            else:
                return print('no')
        elif s[i] == ')':
            if len(stack) > 0 and stack.pop(-1) == '(':
                continue
            else:
                return print('no')
    if len(stack) > 0:
        return print('no')
    else:
        return print('yes')



while True:
    sentence = input()
    if sentence == '.':
        break
    length = len(sentence) # 길이
    yes_or_no(sentence)