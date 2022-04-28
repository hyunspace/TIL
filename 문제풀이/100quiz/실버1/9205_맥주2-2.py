# 4월 28일
# https://letalearns.tistory.com/96

from collections import deque
import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수
for _ in range(t):
    n = int(input()) # 편의점 개수
    home = list(map(int, input().split())) # 집
    stores = [list(map(int, input().split())) for _ in range(n)] # 편의점 정보
    festival = list(map(int, input().split())) # 최종 목적지

    location = deque() # 방문한 곳
    location.append(home)
    visited = [0 for _ in range(n)] # 편의점 방문 체크
    flag = 1
    while location:
        x, y = location.popleft() # 현재 위치
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000: # 맥주 20병으로 갈 수 있는 거리
            print('happy')
            flag = 0
            break
        # 갈 수 없는 거리라면, 편의점을 찾아봐야한다
        for idx in range(n):
            if visited[idx] == 0: # 아직 안 들린 편의점
                if abs(x - stores[idx][0]) + abs(y - stores[idx][1]) <= 1000: # 현 위치-편의점 거리 계산
                    location.append(stores[idx]) # 갈 수 있다면 추가
                    visited[idx] = 1             # 방문 표시
    if flag:
        print('sad')