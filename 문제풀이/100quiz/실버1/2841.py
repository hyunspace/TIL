import sys
input = sys.stdin.readline
N, P = map(int, input().split())
strings = 0  # 줄 정보
frets = []   # 프렛 스택

# 멜로디 연주하기
change = 0
for i in range(N):
    string, fret = map(int, input().split())

    # 맨 처음 연주는 조건 없이 시작
    if strings == 0 and len(frets) == 0:
        strings = string
        frets.append(fret)
        change += 1
        continue

    # 같은 줄일 때
    if strings == string:
        # 프렛만 확인
        if frets[-1] == fret:   # 같은 프렛이면
            continue            # 아무것도 할 필요 없음
        elif frets[-1] < fret:  # 새 프렛이 더 높으면
            frets.append(fret)  # 더하고
            change += 1         # 손가락 변화
        else:                   # 새 프렛이 더 낮으면(연주 가능할 때까지 빼 줘야함)
            while frets:
                frets.pop(-1)
                change += 1
                if len(frets) == 0: # 아무것도 없으면
                    frets.append(fret)
                    change += 1
                    break
                elif frets[-1] < fret: # 더 높아졌으면
                    frets.append(fret)
                    change += 1
                    break
                elif frets[-1] == fret: # 같아졌으면
                    break
                else:                   # 아직 작으면
                    continue

    # 다른 줄일 때
    else:
        strings = string # 줄 갱신
        if frets and frets[-1] == fret:
            continue
        elif frets and frets[-1] < fret:
            change += 1
        else:
            while frets:
                frets.pop(-1)
                change += 1
                if len(frets) == 0: # 아무것도 없으면
                    frets.append(fret)
                    # change += 1 # 다른 줄이니까 상관 X
                    break
                elif frets[-1] < fret: # 더 높아졌으면
                    frets.append(fret)
                    change += 1
                    break
                elif frets[-1] == fret: # 같아졌으면
                    break
                else:                   # 아직 작으면
                    continue
print(change)

