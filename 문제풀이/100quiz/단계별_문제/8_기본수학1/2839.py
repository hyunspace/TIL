'''
5kg과 3kg의 설탕을 골라서 최소한의 설탕 봉지로
주어진 kg을 맞추기
불가능하면 -1 출력하기
'''

### Feb 13 ###

# N = int(input())

# 3의 배수도 5의 배수도 아니라면 -1 출력
def sugar(n):
    # if n%3 != 0 and n%5 != 0:
    #     return -1
    a = 0
    b = 0
    if (n%5)%3 == 0:
        a = n//5
        b = (n-a*5)//3
        return a+b
    elif n%3 == 0:
        return n//3
    else:
        return -1

print(sugar(int(input())))

## 엣지케이스 11...