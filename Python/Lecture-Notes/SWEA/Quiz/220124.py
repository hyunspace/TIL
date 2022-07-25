## 6206
# K = float(input())
# lb = K * 2.2046

# print(f'{K:.2f} kg =>  {lb:.2f} lb')

## 6209
# F = int(input())
# C = (F - 32) / 1.8
# print(f'{F:.2f} ℉ =>  {C:.2f} ℃')

## 6216
# result = (100 * 0.2) / (100 + 200) * 100
# print(f'혼합된 소금물의 농도: {result:.2f}%')


## 6219
# n = int(input())
# cnt = 0
# for i in range(1, n+1):
#     if n % i:
#         pass
#     else:
#         cnt += 1
#         print(f'{i}(은)는 {n}의 약수입니다.')
#     if cnt == 2:
#         print(f'{n}(은)는 1과 {n}로만 나눌 수 있는 소수입니다.')

## 6219
# m1 = input()
# m2 = input()
# # 돌려보자
# play = {
#     '가위': 1,
#     '바위': 2,
#     '보': 3
# }
# if m1 == '가위' and m2 == '보':
#     print('Result : Man1 Win!')
# elif m1 == '보' and m2 == '가위':
#     print('Result : Man2 Win!')
# else:

#     if play[m1] > play[m2]:
#         print('Result : Man1 Win!')
#     elif play[m1] == play[m2]:
#         print('Result : Draw')
#     else:
#         print('Result : Man2 Win!')

## 6222

# alpha = input()

# if alpha.isupper == True:
#     asc1 = ord(alpha)
#     asc2 = ord(alpha) + 32
#     asc3 = chr(asc2)
#     print(f'{alpha}(ASCII: {asc1}) => {asc3}(ASCII: {asc2})')
# else:
#     asc1 = ord(alpha)
#     asc2 = ord(alpha) - 32
#     asc3 = chr(asc2)
#     print(f'{alpha}(ASCII: {asc1}) => {asc3}(ASCII: {asc2})')


## 6226

# for i in range(1, 201):
#     if i % 7 == 0:
#         if i % 5 != 0:
#             num = str(i) + ','
#             print(num, end='')


## 6227

# def all_even(numbers):
#     for number in (100, numbers+1):
#         # for num in number:
#         #     # 숫자는 not iterable 
#         #     if num % 2 == 0:
#         #         print(num, end=' ')
#         # 각 자리수를 나누어서 찾아보자
#         if number >= 10:
#             remainder = number % 10 
#             number = number // 10
#             if remainder % 2 == 0:
#                 return all_even(numbers) + remainder

# print(all_even(300))

for number in (100, 301):
    while number < 301:
        remainder = number % 10
        number = number // 10
        if remainder % 2 == 0:
            remainder = number % 10
            number = number // 10
            if remainder % 2 == 0:
                print(number)