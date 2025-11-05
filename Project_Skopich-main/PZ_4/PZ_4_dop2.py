'''
Ввести 4 числа. Найти и вывести на экран количество четных чисел
'''

a = input('Введите целое число A: ')
while type(a) != int:
    try:
        a = int(a)
        break
    except ValueError:
        print('Что-то не так, введите снова!')
        a = input('Введите целое число A: ')

b = input('Введите целое число B: ')
while type(b) != int:
    try:
        b = int(b)
        break
    except ValueError:
        print('Что-то не так, введите снова!')
        b = input('Введите целое число B: ')

c = input('Введите целое число C: ')
while type(c) != int:
    try:
        c = int(c)
        break
    except ValueError:
        print('Что-то не так, введите снова!')
        c = input('Введите целое число C: ')

d = input('Введите целое число D: ')
while type(d) != int(d):
    try:
        d = int(d)
        break
    except ValueError:
        print('Что-то не так, введите снова!')
        d = input('Введите целое число D: ')

quan = 0
if a % 2 == 0:
    quan = quan + 1
if b % 2 == 0:
    quan = quan + 1
if c % 2 == 0:
    quan = quan + 1
if d % 2 == 0:
    quan = quan + 1

print('В ряде есть', quan, 'четных чисел.')