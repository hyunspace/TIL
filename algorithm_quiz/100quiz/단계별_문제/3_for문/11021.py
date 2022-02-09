# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며,
# 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
import sys; sys.stdin = open('11021.txt')

# T = int(input())
# print(T)
# for tc in (1, T + 1): => range빼먹음...ㅠ
#     print(tc)
#     a, b = map(int, input().split())
#     print(a + b)
#     # print(f'Case #{tc}: {a + b}')

T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'Case #{tc}: {a + b}')