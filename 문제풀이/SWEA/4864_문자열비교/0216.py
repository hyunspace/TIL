'''2월 16일 보충'''

import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    for char in str2:
        for cha in str1:
            if cha == char:
