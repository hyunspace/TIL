# -*- coding: utf-8 -*-

# 15-15.py

class Student:

    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self):
        return "{0}(name: {1}, gender: {2}, height: {3})"\
            .format(self.__class__.__name__, self.name, self.gender, self.height)

# s1 = Student("홍길동", "남", 188)
# print(s1)


students = [
    Student("홍길동", "남", 188),
    Student("이순신", "남", 190),
    Student("강감찬", "남", 187)
]

for student in students:
    print(student)

# sorting 하기(오름차순)
print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name):
    print(student)

# 내림차순으로
print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=True):
    print(student)

# 키 오름차순
print("height로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height):
    print(student)

# 키 내림차순
print("height로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height, reverse=True):
    print(student)