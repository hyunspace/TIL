'''
영어 대소문자와 공백으로 이루어진 문자열이 주어진다.
이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
'''


### Feb 13, 2022 ###

# sentence = input()

# 내장함수와 메서드 써서 해결하기
# words = list(input().split())
# print(len(words))

# 반복문을 활용해서 내장함수와 메서드 대신하기

def cnt_word(sentence):
    # 길이 구하기
    length = 0
    for i in sentence:
        length += 1
    # 길이를 순회하면서 띄어쓰기가 나올 때마다 숫자 세기
    space = 0
    for j in range(length):
        if sentence[j] == ' ':
            space += 1
    # 단어의 수는 띄어쓰기 + 1 (마지막 단어 뒤에는 띄어쓰기가 없으므로)
    return space + 1

print(cnt_word(input()))

# => 앞 뒤의 필요 없는 띄어쓰기의 경우엔 어떻게 할래 .. 흑 띄어쓰기 두번씩 한 바보들도 있다면??