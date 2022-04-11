alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets_cnt = [0] * 26
word = input().upper()
for w in word:
    for idx in range(26):
        if w == alphabets[idx]:
            alphabets_cnt[idx] += 1
max_cnt = max(alphabets_cnt)
max_idx = 100
cnt = 0
for i in range(26):
    if max_cnt == alphabets_cnt[i]:
        max_idx = i
        cnt += 1

if cnt == 1:
    print(alphabets[max_idx])
else:
    print('?')