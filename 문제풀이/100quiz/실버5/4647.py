## Safecracker ##

def sub_sets(arr):
    sub_set = [[]]
    for i in arr:
        len_ = len(sub_set)
        for j in range(len_):
            sub_set.append(sub_set[j] + [i])
    return sub_set

# https://programmers.co.kr/learn/courses/4008/lessons/12836
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

while True:
    target, chars = input().split()
    target = int(target) # 정수로 바꿔주기

    # 종료조건
    if target == 0 and chars == 'END':
        break

    alphabets = list('0ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = []
    for char in chars:
        for alpha in range(1, 27):
            if char == alphabets[alpha]:
                numbers.append(alpha)

    # 원수의 개수가 5개인 부분집합 찾기
    subsets = sub_sets(numbers)
    subset = []

    # 5개를 순서를 바꿔가며 순열 배열 찾기
    flag = 0
    for i in range(len(subset)):
        cases = permute(subsets)
        print(cases)
        for j in range(120):
            case = cases[j][0] - cases[j][1]**2 + cases[j][2]**3 - cases[j][3]**4 + cases[j][4]**5
            if case == target:
                flag = 1
                print(cases)
                break
    if flag:
        pass
    else:
        print('no solution')