import sys; sys.stdin = open('input.txt')

# infix를 postfix로 변환하는 함수
def in_to_postfix(infix_note):
    operators = []  # 연산자
    numbers = []  # 숫자
    postfix = []  # 후위

    for n in infix_note:
        if n != '+' and n != '*': # str(숫자)라면
            postfix.append(int(n)) # int() 형변환 후 추가
        else:
            if len(operators) == 0: # 스택이 비었으면 그냥 추가 (비교대상X)
                operators.append(n)
            elif operators[-1] == n: # peek == n => 우선순위 같으므로 pop

                postfix.append(operators.pop(-1))
                operators.append(n)
            elif operators[-1] == '+' and n == '*': # + < * 이니까 *는 바로 붙여 주기(pop)
                operators.append(n)
            elif operators[-1] == '*' and n == '+': # * < + 이니까 *는 pop, +은 집어 넣기
                postfix.append(operators.pop(-1))
                operators.append(n)
    if len(operators) != 0:
        for _ in range(len(operators)):
            postfix.append(operators.pop(-1))

    return postfix

def postfix_caclulate(postfix_note):
    post_cal = []
    for i in postfix_note:
        if i != '+' and i != '*':
            post_cal.append(int(i))
        elif i == '+':
            post_cal.append(post_cal.pop(-1) + post_cal.pop(-1))
        elif i == '*':
            post_cal.append(post_cal.pop(-1) * post_cal.pop(-1))
    return post_cal[-1]

for tc in range(1, 11):
    N = int(input())
    postfix_note = in_to_postfix(input())
    # print(postfix_note)
    print(f'#{tc} {postfix_caclulate(postfix_note)}')




# print(in_to_postfix('23*56*7*+8+'))



