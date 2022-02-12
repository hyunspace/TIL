'''
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에
0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
'''

# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다.
# A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.


### Feb 11 ###

# input 받기
a = int(input())
b = int(input())
c = int(input())

# 숫자를 일단 펼쳐서 리스트에 담아두기
numbers = list(map(int, str(a*b*c)))
# print(numbers) # [1, 7, 0, 3, 7, 3, 0, 0]
# 숫자의 갯수를 담을 박스
cnt_box = [0] * 10

for idx in range(len(numbers)):
    for num in range(10):
        if num == numbers[idx]:
            cnt_box[num] += 1

for i in range(10):
    print(cnt_box[i])