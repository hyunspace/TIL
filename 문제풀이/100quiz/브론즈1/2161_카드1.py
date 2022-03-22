N = int(input()) # 카드 개수
queue = list(range(1, N+1)) # 카드를 queue에 담기
throw = [] # 버린 카드 담아둘 리스트

while len(queue) > 1: # 1이 되면 종료해야
    # 버리고
    throw.append(queue.pop(0))
    # 맨 아래로 넣기
    temp = queue.pop(0)
    queue.append(temp)

# 출력 형식 맞추기
throw.append(queue[0])
result = throw
print(*result)

# 원래 출력 코드 => 오류남
# print(*throw, end=' ')
# print(queue[0])