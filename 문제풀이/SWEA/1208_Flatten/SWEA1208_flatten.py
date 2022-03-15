import sys; sys.stdin = open('SWEA1208_input.txt')

for tc in range(1, 11):
    dump_chance = int(input())
    boxes = list(map(int, input().split()))
    heights = [0] * 100

    # counting sort
    for box in boxes:
        for idx in range(100):
            if box == idx+1:
                heights[idx] += 1

    min_h = max_h = 0
    # 최소 인덱스는 앞에서부터 순서대로 탐색
    for idx in range(100):
        if heights[idx] > 0:
            min_h = idx
            break
    # 최대 인덱스는 뒤에서부터 거꾸로 탐색
    for idx in range(99, -1, -1):
        if heights[idx] > 0:
            max_h = idx
            break

    # dump하면서 가장 높은 박수의 개수 줄이고, 가장 낮은 박스의 개수도 줄이자
    for dump in range(dump_chance):
        # 가장 높은 곳과 가장 낮은 곳의 차이가 1이하라면
        # 더이상 덤프하지 않아도 되므로 break
        if max_h - min_h <= 1:
            break

        # 2 이상의 차이가 난다면 평탄화 작업 ㄱ
        else:
            # 가장 높은 곳에서 상자를 뺀다 == 가장 높은 곳-1개인 곳이 한 개 생긴다
            heights[max_h] -= 1
            heights[max_h - 1] += 1
            # 가장 높은 곳 상자를 다 썼다면
            if heights[max_h] == 0:
                # 인덱스를 옮겨서 한칸 앞으로(왼쪽 방향으로)
                max_h -= 1

            # 가장 낮은 곳에 상자를 더한다 == 가장 낮은 곳+1개인 곳이 한 개 생긴다
            heights[min_h] -= 1
            heights[min_h + 1] += 1
            # 가장 낮은 곳에 상자가 없다면(다 하나씩 많아져서)
            if heights[min_h] == 0:
                # 인덱스를 한칸 뒤로 옮긴다(오른쪽 방향으로)
                min_h += 1

    print(f'#{tc} {max_h - min_h}')