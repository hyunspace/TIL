# def conti_num(first, second, arr): # N 하나만 들어있는 arr
#     if first - second >= 0:
#         arr.append(second)
#         return conti_num(second, first-second, arr)
#     else:
#         arr.append(second)
#         return arr

N = int(input())
max_len = 0
max_result = []

# N부터 1까지 다 골라보자
for n in range(N, -1, -1): # N을 선택해도 된다! (조건 잘 읽기. N을 해야 N==1일 때 정답이 나온다)
    arr = [N] # 우선 N을 미리 리스트에 담아두고
    first = N # while문에서 사용할 변수에 담자
    second = n
    while first - second >= 0: # 음수면 멈춰!
        arr.append(second) # first는 이미 더했으니 second만
        first, second = second, first-second # 새로 할당
    arr.append(second) # 마지막에 음수가 나오더라도 끝값은 더해줘야지

    # 각각의 n에 대한 최대 길이 확인
    if max_len < len(arr):
        max_len = len(arr)
        max_result = arr

print(max_len)
print(*max_result)

#     arr = [N]
#     if max_len < len(conti_num(N, n, arr)):
#         max_len = len(conti_num(N, n, arr))
#         max_result = (conti_num(N, n, arr))
#     else:
#         continue
# print(max_len)
# print(max_result)
