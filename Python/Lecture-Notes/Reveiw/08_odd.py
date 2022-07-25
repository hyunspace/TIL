# 1~30까지 숫자 중에 (반복)
# 홀수만 (조건)

for i in range(1, 31):
    if i % 2 == 1:
        print(i)

print("====================")

# 하나로 
# 1-1 빈통 만들기
numbers = []
for i in range(1, 31):
    if i % 2 == 1:
        numbers.append(i)
    print(numbers)

print("====================")

numbers_2 = [ i for i in range(1, 31) if i % 2 == 1]
print(numbers_2)