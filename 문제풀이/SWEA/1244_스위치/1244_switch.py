import sys; sys.stdin = open('1244_input.txt')

N = int(input()) # 스위치 개수
switches = list(map(int, input().split()))
M = int(input())
# print(switches)

for m in range(M): # 학생 수만큼 반복
    sex, num = map(int, input().split())
    # print(sex, num)
    # 성별 판정
    if sex == 1: # 남자라면
        for idx in range(N): # 전체 스위치 순회
            if (idx+1) % num == 0: # 0으로 나누어 떨어진다 == num이 약수 == 스위치 번호가 배수
                # 스위치에 따라서 바꾸기
                if switches[idx]: # 1이라면
                    switches[idx] = 0
                else:
                    switches[idx] = 1
        # print(switches)
    elif sex == 2: # 여자라면
        # 자기자신 먼저 바꿔놓기
        if switches[num -1]:  # 1이라면
            switches[num -1] = 0
        else:
            switches[num -1] = 1

        # 양쪽 탐색
        for k in range(1, N-num+1):
            if 0 <= num - 1 - k and num - 1 + k < N and switches[num - 1 - k] == switches[num - 1 + k]:
                if switches[num -1 + k]: # 1이라면
                    switches[num - 1 + k] = 0
                    switches[num - 1 - k] = 0
                else:
                    switches[num - 1 + k] = 1
                    switches[num - 1 - k] = 1
            elif 0 <= num - 1 - k and num - 1 + k < N and switches[num - 1 - k] != switches[num - 1 + k]:
                break
for i in range(N//20 + 1):
    temp = switches[20*i:20*(i+1)]
    print(*temp)