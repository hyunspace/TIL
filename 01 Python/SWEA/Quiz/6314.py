# 문제 6314

# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 
# filter 함수와 람다식을 이용해
# 짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.


# 1~10까지의 정수를 항목으로 갖는 리스트 객체
list1 = list(range(1, 11))
# print(list1)

list1_even = list(filter(lambda x : x % 2 ==0, list1))
print(list1_even)