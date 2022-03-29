# N = int(input())

# cards = [str(i) for i in range(1, N+1)]

# result = []

# while 1:
#         # 제일앞 카드 뽑고 공백더함
#     temp = cards.pop(0)
#     result.append(temp)
#     result += ' '
#     # 카드 다 쓸때까지 반복
#     if not cards:
#         break
#         # 제일앞 카드 뽑아서 뒤로
#     n = cards.pop(0)
#     cards += n
#     # 혹시몰라서 마지막 공백빼고 출력
# result = result[0:N*2-1]
# print(result)

# a = ['11']
# test= []
# test += a[0]
# # print(test)

# a = ['apple']
# b = []
# b.extend(a.pop(0))
# print(b)

# a = ['10','10']
# b = []
# b.append(a.pop(0))
# c = []
# c.extend(a.pop(0))
# print(b)
# print(c)

# N = int(input())

# cards = [str(i) for i in range(1, N+1)]
# result = ''

# while 1:
#     result += cards.pop(0)+' '
#     if not cards:
#         break
#     n = cards.pop(0)
#     cards += [n]
# result = result
# print(result)

a = ['123', '456', '789', '123', '456', '789']
b = []
temp = a.pop(0)
print(f'임시 변수 temp: {temp}')
b.append(temp)
print(f'b.append(temp) {b}')
b = []
b.append(a.pop(0))
print(f'b.append(a.pop(0)) {b}')
b = []
temp = a.pop(0)
print('-'*30)
b = []
b += temp
print(f'c += temp {b}')
b = []
b += a.pop(0)
print(f'c += a.pop(0) {b}')
b = []
temp = a.pop(0)
b += [temp]
print(f'c += [temp] {b}')
b = []
b.append([a.pop(0)])
print(f'c.append([a.pop(0)]) {b}')