# 5월 9일

arr = list(map(int, input()))
arr = sorted(arr, reverse=True)
ans = ''
for num in arr:
    ans += str(num)
print(ans)