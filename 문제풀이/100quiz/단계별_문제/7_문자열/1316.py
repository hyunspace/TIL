'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서,
각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
'''

### Feb 13, 2022 ###


N = int(input())
# 최종 반환할 변수
result = 0

for n in range(N):
    words = list(input())
    # 등장한 알파벳을 따로 담을 리스트
    appear = []
    # 문제 없는지 카운트 할 체커
    checker = 1 # True
    for idx in range(len(words)):
        # 이전에 나온 적 없는 알파벳이 나오면 OK
        if words[idx] not in appear:
            appear.append(words[idx])
        # 이전에 나온 적이 있는 알파벳이 나왔다면
        else:
            # 바로 앞에 같은게 있는지(연속) 확인
            if words[idx] == words[idx-1]:
                continue # 연속이라면 문제X 계속 진행
            # 바로 앞에 나온 적 없음 => 그룹XX
            else:
                checker = 0
    if checker: # checker == 0, True
        result += 1
print(result)