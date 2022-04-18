K = int(input())        # 입력 받을 숫자의 개수
queue = []              # queue
for _ in range(K):      
    num = int(input())  # 입력 받은 숫자
    if num:             # 0이 아니라면 바로 queue에 추가
        queue.append(num)
    else:               # 0이라면 직전에 추가한 숫자를
        queue.pop(-1)   # 지워준다
print(sum(queue))       # queue에 남은 값 더하기