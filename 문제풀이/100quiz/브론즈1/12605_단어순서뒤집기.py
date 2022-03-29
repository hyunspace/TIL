N = int(input())

for tc in range(1, N+1):
    sentence = list(input().split())
    result = []
    # 순서 바꾸기
    for idx in range(len(sentence)-1, -1, -1):
        result.append(sentence[idx])
    print(f'Case #{tc}:', *result)