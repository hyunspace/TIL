'''
알파벳 소문자로만 이루어진 단어 S가 주어진다.
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
'''

### Feb 13 ###

S = input()

# 알파벳을 원소로 하는 리스트
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l',
             'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
# alphabet = list(map(str, 'abcdefghijklmnopqrstuvwxyz'))

# 알파벳 첫 등장 인덱스를 담을 리스트
cnt_char = [-1] * 26

# 주어진 단어를 순회하면서
for i in range(len(S)):
    for idx in range(26):
        # 주어진 알파벳이 리스트 내 알파벳과 일치하고, 첫 등장일 때
        if S[i] == alphabets[idx] and cnt_char[idx] == -1:
            # alpahbets 내 인덱스를 찾아서 cnt_char에 반영
            cnt_char[idx] = i

for ans in cnt_char:
    print(ans, end=' ')