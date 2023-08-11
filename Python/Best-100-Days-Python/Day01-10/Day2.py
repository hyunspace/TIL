# 데이터 형식 이해 및 문자열 조작
# 프로젝트: 계산기 만들기

# print(len(12352)) => 오류
print(len('12352'))


######################
# # # Data Types # # #

#String
print("Hello"[-1])
print("Hello"[4])


a = 123
type(a)

print(8/3)
print(int(8/3))
print(round(8/3))
print(round(8/3, 2))

print("-------------------------")

print(type(4/2))
result = 4/2
result /= 2
print(result)

print("-------------------------")

score = 0
height = 1.8
isWinning = True
# f-String
print(f"Your score is {score}, your height is {height}, your are winning is {isWinning}.")