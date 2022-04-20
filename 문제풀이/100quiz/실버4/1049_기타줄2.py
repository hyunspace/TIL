# 4월 21일

N, M = map(int, input().split())

# 여러 브랜드 중에서 세트와 낱개 줄이 가장 싼 경우만 기억해둔다
min_set = 1000
min_ind = 1000
for _ in range(M):
    s_price, i_price = map(int, input().split())
    if min_set > s_price:
        min_set = s_price
    if min_ind > i_price:
        min_ind = i_price

# 최저가 기타줄 정보를 바탕으로 N개의 기타줄을 구입하자
min_pay = 1000*100 # 필요한 돈의 최솟값

# 6으로 나누어 지는 경우
if N % 6 == 0:
    # 1) 세트로 구입
    s_pay = min_set * (N//6)
    # 2) 낱개로 구입
    i_pay = min_ind * N
# 6으로 나눴을 때 나머지가 생기는 경우
else:
    # 1) 세트와 낱개를 섞어서 구매
    s_pay1 = min_set * (N // 6) + min_ind * (N % 6)
    # 2) 세트만 구매
    s_pay2 = min_set * (N//6 + 1)
    if s_pay1 < s_pay2:
        s_pay = s_pay1
    else:
        s_pay = s_pay2
    # 3) 낱개로만 구매
    i_pay = min_ind * N

if min_pay > s_pay:
    min_pay = s_pay
if min_pay > i_pay:
    min_pay = i_pay

print(min_pay)