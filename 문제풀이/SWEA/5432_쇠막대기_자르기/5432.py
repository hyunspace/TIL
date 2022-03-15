import sys; sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    info = input()
    # print(info[0])

    # ()을 찾아서 모양을 바꾸자
    # for i in range(len(info)-1):
    #     if info[i] == '(' and info[i+1] == ')':
    #         info[i] = ''
    #         info[i+1] = 'r'
    # => string은 순회가능하지만 변경불가능하므로, 값을 변경할 수 없고
    # 리스트 형태로 받아서 변경하면 ['(', '(', '', 'r',...] 하는 식으로 바뀌어서 의미가 없다ㅠ

    # 하민님 코드에서 본 replace를 빌려오자..!ㅎㅎ
    # for i in range(len(info)): => 불필요한 for문 때문에 시간 초과ㅠㅠ
    r_info = info.replace('()', 'r')
    # print(r_info)

    # r_info를 순회하면서 막대 개수 세기
    rod = 0
    cut_rod = 0
    for j in r_info:
        if j == '(': # 쇠막대 시작
            rod += 1
        elif j == 'r': # 레이저 만남 => 잘림
            cut_rod += rod
        elif j == ')': # 쇠막대 끝
            rod -= 1
            cut_rod += 1

    print(f'#{tc} {cut_rod}')


