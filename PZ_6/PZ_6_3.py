'''
Дано множество A из N точек на плоскости и точка B (точки заданы своими
координатами х, у). Найти точку из множества A, наиболее близкую к точке B.
Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по
формуле:
R = √(x2 – x1)^2 + (у2 – y1)^2
'''
import math
import random

N = int(input('Введите количество точек N: '))

A = []
for i in range(N):
    Xa = random.randint(-50, 50)
    Ya = random.randint(-50, 50)
    A.append((Xa,Ya))

Xb = random.randint(-50, 50)
Yb = random.randint(-50, 50)
B = (Xb, Yb)

print(f'Множество A из {N} точек: {A}')
print(f'Координаты точки B: {B}')

min_distance = float('inf')
closest_point = None


for i, point in enumerate(A):
    x1, y1 = point
    x2, y2 = B
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance < min_distance:
        min_distance = distance
        closest_point = point

print(f'Близжайшая точка к В: {closest_point}')
print(f'Дистанция: {min_distance}')
