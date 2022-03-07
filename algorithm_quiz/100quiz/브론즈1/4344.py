C = int(input())
for tc in range(C):
    N, *scores = map(int, input().split())

    # # 내장함수 버전
    # average = sum(scores) / N
    # good = 0
    # for score in scores:
    #     if score > average:
    #         good += 1
    # print(f'{good/N*100:.3f}%')

    total = 0
    for score in scores:
        total += score
    average = total / N

    good = 0
    for score in scores:
        if score > average:
            good += 1

    print(f'{good/N*100:.3f}%')