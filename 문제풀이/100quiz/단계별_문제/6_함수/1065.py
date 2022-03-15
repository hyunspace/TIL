'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고,
N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
'''

def hansu(N):
    # 자연수 1부터 N까지를 순회하면서
    result = 0 # 한수의 개수 세기
    for n in range(1, N+1):
        if 1 <= n <= 99:
            result += 1
        else:
            # 최댓값이 1000이므로 세자리가 최대임
            fir = n % 10 # 일의 자리수
            ten = n // 10 - (n // 100) * 10 # 십의 자리수
            hund = n // 100 # 백의 자리수
            if fir - ten == ten - hund:
                result += 1
    return result

print(hansu(int(input())))