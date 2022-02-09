### Feb 07, 2022

# a, b = map(int, input().split())

# while input() is not None:
#     print(a + b)
#     a, b = map(int, input().split())

# while True:
#     print(a + b)
#     a, b = map(int, input().split())

## 풀이 참고함
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
# try, break 공부 다시 할 것..!