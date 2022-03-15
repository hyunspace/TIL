# A도시는 전기버스를 운행하려고 한다.
# 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서,
# 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고,
# 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때,
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.
# 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

'''
첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다.
( 1 ≤ K, N, M ≤ 100 )'''

import sys; sys.stdin = open('input.txt')

# 노선 수 T
T = int(input())

# 입력 횟수만큼 반복
for tc in range(1, T + 1): # range 까먹지 마... 제발...좀
    # 한 번에 이동 가능한 정류장 수 K, 종점 번호N, 충전기 개수 M
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    print(station)
    # K 간격만큼 끊고, 그 범위 이내에 가장 멀리에 있는 충전소를 선택
    # 충전하게 되면 해당 충전소 위치를 '새로운 기준'으로 잡고 다시 K간격을 센다!
    # 버스의 위치를 담을 변수 bus
    bus = 0
    # 현재 충전 가능한 충전소의 위치를 임시로 담을 리스트
    avail_station = []
    # 충전 횟수를 담을 변수
    char_num = 0

#     # while bus < N - K:
#     for i in range(bus, bus+K+1):
#         if i in station:
#             if i == station[0]:
#                 continue
#             # i 중에서 제일 큰 수를 뽑아야 함
#             avail_station.append(i)
#         print(avail_station)
#         # bus = avail_station[-1]
#         # char_num += 1
    for i in range(bus, bus+K+1):
        if i in station:
            avail_station.append(i)
        # 지금 세지 말고 나중에 한 꺼번에 세도 된다

