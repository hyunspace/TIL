
def recursion(n):
    if n < 0:
        return
    # elif n == 1:
    #     print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
    #     print('"재귀함수가 뭔가요?"')
    #     print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    #     print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    #     print('라고 답변하였지.')
    else:
        recursion(n-1)
        a = '----' * n
        print(f'{a}어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
        print(f'{a}"재귀함수가 뭔가요?"')
        print(f'{a}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(f'{a}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    print(f'{a}라고 답변하였지.')


N = int(input())
recursion(N)
