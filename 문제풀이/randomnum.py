import random

N = int(input('총 인원을 입력해주세요: '))
candidates = list(range(1, N + 1))
picked_num = list(random.sample(candidates, 3))
print('당첨 번호는...')
for num in picked_num:
    print(f'{num}번!')
