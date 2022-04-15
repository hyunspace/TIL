def delivery(s):
    ans = 0
    if s % 5 == 0:
        ans = s // 5
        return print(ans)
    else:
        while s > 0:
            s -= 3
            ans += 1
            if s == 0:
                return print(ans)
            elif s % 5 == 0:
                ans += s // 5
                return print(ans)
            elif 3 < s < 5 or s < 3:
                return print(-1)

sugar = int(input())

delivery(sugar)