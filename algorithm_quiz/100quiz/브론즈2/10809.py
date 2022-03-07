alphabets = []
alphabets.extend('abcdefghijklmnopqrstuvwxyz')

word = input()
counts = [-1] * 26

for idx in range(len(word)):
    for alpha in range(26):
        if word[idx] == alphabets[alpha] and counts[alpha] == -1:
            counts[alpha] = idx
print(*counts)
