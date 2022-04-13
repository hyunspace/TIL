chars = input()
dials = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

sec = 0

for car in chars:
    for index in range(3, 11):
        if car in dials[index]:
            sec += index
print(sec)