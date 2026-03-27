'''
Даны две последовательности. Найти элементы, различные для двух 
последовательностей и их среднее арифметическое.
'''
from functools import reduce

def solve(a, b):
    s1, s2 = set(a), set(b)
    uniqe = (s1 | s2) - (s1 & s2)
    n = len(uniqe)
    avg = list(reduce(lambda acc, x: acc + x, uniqe, 0) / n if n > 0 else 0.0)
    return uniqe, avg

x_str = input("Введите элементы первой последовательности через пробел: ")
y_str = input("Введите элементы второй последовательности через пробел: ")

x = list(map(int, x_str.split()))
y = list(map(int, y_str.split()))

elems, avg = solve(x, y)

print(f'Уникальные элементы: {elems}')
print(f'Среднее арифметическое: {avg}')

