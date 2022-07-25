# *-* coding: utf-8 -*-

# 08-21.py

PI = 3.14

def input_radius():
    radius_stir = input("반지름을 입력하세요: ")
    return float(radius_stir)

def calc_circle_area(r):
    return PI * r * r

def calc_circumference(r):
    return 2 * PI * r

radius = input_radius()
circle_area = calc_circle_area(radius)
circumference = calc_circumference(radius)
print("원의 면적: {0:0.2f}, 원의 둘레: {1:0.2f}".format(circle_area, circumference))