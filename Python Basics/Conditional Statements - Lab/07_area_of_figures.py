import math
from math import pi

figura = input()
area = 0


if figura == 'square':
    a = float(input())
    area = a * a
elif figura == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif figura == 'circle':
    r = float(input())
    area = math.pi * r * r
elif figura == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2

print(f'{area:.3f}')