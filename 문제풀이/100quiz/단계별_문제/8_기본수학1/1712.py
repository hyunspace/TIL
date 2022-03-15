'''
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다.
A, B, C는 21억 이하의 자연수이다.
A: 고정비, B: 가변비, C: 판매가
'''

'''
첫 번째 줄에 손익분기점 즉 최초로 이익이 발생하는 판매량을 출력한다.\
손익분기점이 존재하지 않으면 -1을 출력한다.
'''

### Feb 13 ###

# fixed cost, variable cost, price
fc, vc, p = map(int, input().split())

# 판매량
# q = 0
# while True:
#     if vc > p:
#         print(-1)
#         break
#     q += 1
#     if (p - vc) * q - fc > 0:
#         print(q)
#         break
# # => 시간초과ㅠ


### Feb 14 ###

while True:
    if vc >= p:
        print(-1)
        break
    print(fc//(p-vc)+1)
    break