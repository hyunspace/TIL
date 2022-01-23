# lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
# print(lux1)
# print(type(lux1))

# # a = dict('김'=25, '이'=26, '박'=24)
# # print(a)
# # print(type(a))

# b = dict(김=25, 이=26, 박=24)
# print(b)
# print(type(b))

def my_all(elements):
    for el in elements:
        if el == True:
            pass
        else:
            return False
    return True
print(my_all([1, 2, 5, '6']))
