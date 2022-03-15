import sys; sys.stdin = open('input.txt')

T = int(input()) #테스트 케이스 수

for tc in range(1, T+1):
    N = int(input()) #노선의 개수
    # print(N)
    ab = [list(map(int, input().split())) for _ in range(N)] # A와 B에 대한 값
    # print(ab) # 각 노선이 멈추는 정류장 범위에 대한 정보 (ex. [[A1, B1], [A2, B2]])
    P = int(input()) # 확인할 정류장 개수 != 전체 정류장 개수
    c = [int(input()) for _ in range(P)] # 확인할 정류장 번호
    # print(c)


    stops = [0] * 5000 # 전체 정류장
    # print(stops)
    for i in range(N): # 0, 1
        start = ab[i][0]-1
        end = ab[i][1]
        for stop in range(start, end):
            stops[stop] += 1

    result = [stops[stop_num-1] for stop_num in c]
    # print(result)

    print(f'#{tc}', *result)