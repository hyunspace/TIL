# -*- coding: utf-8 -*-

# 06-19.py

'''
if문을 활용해 아래의 실행 결과를 반영한 간단 계산기를 만들어 봅시다.
우리가 만들어 볼 간단 계산기는 사용자로부터 두 개의 숫자와 한 개의 연산자를 입력 받아
그 연산자에 따른 계산을 수행할 것입니다.
연산자는 +(덧셈), -(뺄셈), *(곱셈), /(나눗셈)을 지원하도록 할 것입니다.

[실행 결과 1]
첫 번째 숫자를 입력하세요: 2
연산자를 입력하세요 (+, -, *, /): +
두 번째 숫자를 입력하세요: 3
2 + 3 = 5

[실행 결과 2]
첫 번째 숫자를 입력하세요: 2
연산자를 입력하세요 (+, -, *, /): #
두 번째 숫자를 입력하세요: 3
'#'은 본 프로그램에서 지원하지 않는 연산자입니다.
'''

operand1, operator, operand2 = 0, "", 0

operand1 = int(input("첫 번째 함수를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
operand2 = int(input("두 번째 숫자를 입력하세요: "))

if operator == "+":
    print("%d + %d = %d" % (operand1, operand2, operand1 + operand2))
elif operator == "-":
    print("%d - %d = %d" % (operand1, operand2, operand1 - operand2))
elif operator == "*":
    print("%d * %d = %d" % (operand1, operand2, operand1 * operand2))
elif operator == "/":
    print("%d / %d = %.2f" % (operand1, operand2, operand1 / operand2))
else:
    print("'%s'은 본 프로그램에서 지원하지 않는 연산자입니다." % operator)
