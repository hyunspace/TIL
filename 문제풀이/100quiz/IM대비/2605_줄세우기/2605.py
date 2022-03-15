import sys; sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))
seats = [0] * N

# 학생1부터 학생N까지 순회(0~N-1)
for student in range(N):
    if numbers[student] == 0: # 0번을 뽑았다면 자기 자리로
        seats[student] = student + 1 # 인덱스 == 학생번호-1
    else: # 다른 번호를 뽑았다면 그 번호만큼 앞으로 가야함
        move = numbers[student] # 움직일 숫자를 담아두자
        # 학생이 가야할 자리부터 지금 번호 앞자리까지를 한칸씩 뒤로 밀자
        seats[student-move+1:student+1] = seats[student-move:student]
        # 그리고 가야할 자리에 들어가기
        seats[student-move] = student + 1
print(*seats)