# 4월 28일

def go_to_festival(n):
    beer = 20
    for idx in range(n+1):
        distance = abs(maps[idx][0]-maps[idx+1][0]) + abs(maps[idx][1]-maps[idx+1][1])
        while beer > 0: # 가진 맥주를 일단 다 써보자
            beer -= 1
            distance -= 50
        if distance <= 0: # 도착완료
            beer = 20
            continue
        else: # 맥주가 부족해
            return print('sad')
    print('happy')


t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n = int(input()) # 편의점 개수
    maps = []
    for _ in range(n+2):
        x, y = map(int, input().split())
        maps.append([x, y])

    go_to_festival(n)
