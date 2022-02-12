'''
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다.
예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
'''

# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다.
# 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

remains = []
for tc in range(10):
    remains.append(int(input()) % 42)

# 나머지를 담을 컨테이너
remain_cnt = [0] * 42
# 숫자가 있는 idx를 셀 컨데이너
result = 0

for remain in range(10):
    for idx in range(42):
        if remains[remain] == idx:
            remain_cnt[idx] += 1

for n in range(42):
    if remain_cnt[n] > 0:
        result += 1

print(result)