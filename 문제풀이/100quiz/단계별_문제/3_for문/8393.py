# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 주어진 값을 n에 담는다
n = int(input())
# 1부터 n까지 더한 값을 담을 변수
result = 0
# 1부터 n까지 반복할 수 있도록 range 설정
for i in range(1, n+1):
    # result에 더해나가기
    result += i
# 출력
print(result)