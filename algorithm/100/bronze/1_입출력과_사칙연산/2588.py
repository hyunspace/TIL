### Feb 07, 2022

# 두 줄에 나누어서 값이 들어오므로 input도 두 번
# 정수는 순회할 수 없으므로 b는 string으로 그대로 쓰자
a = int(input())
b = input()

# 인덱싱을 사용해서 곱하기!
print(a * int(b[-1]))
print(a * int(b[-2]))
print(a * int(b[0]))
print(a * int(b))