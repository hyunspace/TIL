# -*- coding: utf-8 -*-

# 09-21.py

data_list = list(range(1, 21))

print("data_list: {0}".format(data_list))

map_str = input("항목 x에 대해 적용할 표현식을 입력하세요: ")
filter_str = input("항목 x에 대해 필터링할 조건의 표현식을 입력하세요: ")

map_list = list(map(lambda x: eval(map_str), data_list))
filter_list = list(filter(lambda x: eval(filter_str), map_list))


print("data_list에 대한 map 함수의 적용 결과:  {0}".format(map_list))
print("map_list에 대해 filter 함수의 적용 결과: {0}".format(filter_list))