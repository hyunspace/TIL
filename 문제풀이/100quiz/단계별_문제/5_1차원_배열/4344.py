'''
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다
학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다.
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
'''

import sys; sys.stdin = open('4344.txt')

### Feb 12, 2022 ###

# 테스트 케이스의 수
C = int(input())

'''내장 함수 없이 반복문으로 계산하기!'''
# for tc in range(C):
#     # 학생의 수와 점수를 담는 리스트 score
#     # scores[0] = 학생의 수 = len(scores) - 1
#     scores = list(map(int, input().split()))
#     num = scores[0] # 계속 쓸거니까 변수에 담아두자
#     # 점수를 다 더해서 평균을 구해보자
#     total = 0
#     for i in range(1, num+1):
#         total += scores[i]
#     # 총점을 학생 수로 나누면 평균이 나온다
#     average = total / num
#
#     # 구한 평균을 바탕으로 평균을 넘는 학생의 비율을 구해보자
#     students = 0 # 평균을 넘은 학생을 담을 변수
#     for j in range(1, num+1):
#         if scores[j] > average:
#             students += 1
#     result = students/num*100
#     # print(f'{result: 0.3f}%') => 출력 형식 잘못됐대ㅠ
#     print('{:0.3f}%'.format(result))

for tc in range(C):
    # 학생의 수와 점수를 담는 리스트 score
    # scores[0] = 학생의 수 = len(scores) - 1
    scores = list(map(int, input().split()))
    num = scores[0] # 계속 쓸거니까 변수에 담아두자
    # 내장함수 sum을 이용해서 총점 구하기
    total = sum(scores[1::])
    # 총점을 학생 수로 나누면 평균이 나온다
    average = total / num
    # 구한 평균을 바탕으로 평균을 넘는 학생의 비율을 구해보자
    students = 0 # 평균을 넘은 학생을 담을 변수
    for j in range(1, num+1):
        if scores[j] > average:
            students += 1
    result = students/num*100
    # print(f'{result: 0.3f}%') => 출력 형식 잘못됐대ㅠ
    print('{:0.3f}%'.format(result))
