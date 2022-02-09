## Feb 8

# 셀프 넘버 함수 정의하기
def self():
    # 10000 이하의 정수 중에서 셀프 넘버인 애들을 찾아보자
    num_list = []
    for num in list(range(1, 10001)):
        if num < 100:
            num_list += [num + num//10 + num%10]
        elif num < 1000:
            num_list += [num + num//10*2 + num%10]
    # while len(list(range(1, 100+1))) >= len(num_list):

    # for num in list(range(1, 100+1)):
    #     for idx in str(num):
    #         num_list += [num + int(num[idx])]
    # print(num_list)
    # for nn in range(1, 100+1):
    #     if nn in num_list:
    #         continue
    #     # print(nn)

self()