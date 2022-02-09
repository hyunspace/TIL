### Feb 07, 2022

# 입력 받을 값을 나누어서 담아준다
a, b = map(int, input().split())

# 0이 되면 멈춰야하니까, 0이 아닐 땐 계속 움직이도록
while a != 0 and b!= 0:
    # 더한 값을 출력하고
    print(a+b)
    # 새로운 값을 받아야 한다
    a, b = map(int, input().split())