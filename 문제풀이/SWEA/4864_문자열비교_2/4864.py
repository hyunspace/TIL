# 5월 17일

T = int(input())
for tc in range(T):
    str1 = input()
    N = len(str1)
    str2 = input()
    M = len(str2)

    start = ans = 0
    while start <= M - N:
        for idx in range(0, N):
            if str2[start + idx] == str1[idx]:
                ans += 1
                continue
            else:
                start = idx
                ans = 0
                break
        if ans == N:
            ans = 1
            break
    print(f'#{tc} ans')




