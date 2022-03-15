import sys; sys.stdin = open('input.txt')

T = int(input())
alphabet_dict = {
    'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5,
    'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11,
    'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17,
    'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25
}
# test = 'ABCD'
# for i in test:
#     print(alphabet_dict[i])

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_cnt = [0] * 26 # 알파벳 등장 숫자를 셀 빈 리스트1
    str2_cnt = [0] * 26 # 알파벳 등장 숫자를 셀 빈 리스트2
    for i in str1:      # 기준이 되는 단어에 등장하는 알파벳을 먼저 세고
        str1_cnt[alphabet_dict[i]] += 1
    for j in str2:      # str1에서 등장한 알파벳의 개수만 센다
        if str1_cnt[alphabet_dict[j]] > 0:
            str2_cnt[alphabet_dict[j]] += 1
    str_max = 0         # 리스트 요소의 인덱스를 변경하기 싫어서 변수 설정
    for idx in range(26):
        if str_max < str2_cnt[idx]:
            str_max = str2_cnt[idx]
    print(f'#{tc} {str_max}')