ducks = []
problems = 0

while True:
    S = input()
    if S == '고무오리 디버깅 끝':
        break
    elif S == '문제':
        problems += 1
    elif S == '고무오리':
        # 해결할 문제가 있다면
        if problems > 0:
            problems -= 1
        # 해결할 문제가 없다면
        else:
            problems += 2
            ducks.append('고무오리')

if problems == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')