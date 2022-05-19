# 5월 15일 시간초과

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# users = []
# cnt = 0
# for _ in range(N):
#     user = input()
#     if user == 'ENTER':
#         users = []
#     else:
#        if user in users:
#            continue
#        else:
#            users.append(user)
#            cnt += 1
# print(cnt)

#######################################################

# 5월 19일

N = int(input())
chatting = set()
cnt = 0

for _ in range(N):
    chat = input()
    if chat == 'ENTER':
        cnt += len(chatting)
        chatting = set()
    else:
        chatting.add(chat)
cnt += len(chatting)
print(cnt)