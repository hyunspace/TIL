# 4월 28일
import sys
input = sys.stdin.readline

# 입력값 정리
N = int(input())
meetings = []
for _ in range(N):
    begin, end = map(int, input().split())
    meetings.append([begin, end])

# 끝나는 시간을 기준으로 정렬 해보자...! 람다...!
ans = 0
meetings.sort(key = lambda x : (x[1], x[0]))    # 끝나는 시간+시작시간을 기준으로 정렬

finish = 0                              # 시작은 0
for meeting in meetings:                # 순회하면서 확인하기
    if finish <= meeting[0]:            # 끝나는 시간보다 시작시간이 늦으면 채택
        ans += 1                        # 회의 횟수 세기
        finish = meeting[1]             # 끝나는 시간 갱신
        # print(meeting)
    else:
        continue
print(ans)