N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]

# 세트로 사야한다면 몇 개를 사야하는 가
set_num = 0
if N % 6 == 0:
    set_num = N // 6
else:
    set_num = N // 6 + 1

min_price = 1000
for x, y in data:
    set_price = x * set_num
    idv_price = y * N
    if set_price < idv_price: # 세트가 더 저렴할 때
        if min_price > set_price:
            min_price = set_price
    else: # 낱개가 더 저렴할 때
        if min_price > idv_price:
            min_price = idv_price
        new_price = (N//6) * x + (N - N//6) * y
        if min_price > new_price:
            min_price = new_price
# 브랜드를 섞어서 살 수도 있다 ㅜㅜ
print(min_price)