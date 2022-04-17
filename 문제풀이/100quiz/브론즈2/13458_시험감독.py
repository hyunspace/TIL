import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = len(A) # 총감독관은 1명 씩

for students in A:
    students -= B       # 총 감독관이 감독하는 학생의 수
    if students <= 0:   # 감독관 배치 완료 => 다음 시험장으로
        continue
    else:               # 부감독관 배치 필요함
        if 0 < students <= C:
            ans += 1
            continue
        else:
            share = students // C
            if students > share * C:
                ans += (share + 1)
            elif students == share * C:
                ans += share
            else:
                ans += (share - 1)

        # while students > 0: => 시간 초과
        #     students -= C
        #     ans += 1
print(ans)