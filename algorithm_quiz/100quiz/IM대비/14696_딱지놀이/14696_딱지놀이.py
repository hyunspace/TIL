import sys; sys.stdin = open('14696_input.txt')

N = int(input())

for tc in range(N):
    A, *a = map(int, input().split())
    B, *b = map(int, input().split())

    # 4-3-2-1 순으로 확인하기
    for n in range(4, 0, -1):
        flag = 0
        if a.count(n) != b.count(n):
            if a.count(n) > b.count(n):
                print('A')
                flag = 1
                break  # 결과가 나오면 break!
            else:
                print('B')
                flag = 1
                break  # 결과가 나오면 break!
        else:
            continue

    # 4번을 순회하고도 여전히 승패를 알 수 없다면
    if flag == 0:
        print('D')

    # if a.count(4) != b.count(4):
    #     if a.count(4) > b.count(4):
    #         print('A')
    #     else:
    #         print('B')
    # elif a.count(3) != b.count(3):
    #     if a.count(3) > b.count(3):
    #         print('A')
    #     else:
    #         print('B')
    # elif a.count(2) != b.count(2):
    #     if a.count(2) > b.count(2):
    #         print('A')
    #     else:
    #         print('B')
    # elif a.count(1) != b.count(1):
    #     if a.count(1) > b.count(1):
    #         print('A')
    #     else:
    #         print('B')
    # else:
    #     print('D')
