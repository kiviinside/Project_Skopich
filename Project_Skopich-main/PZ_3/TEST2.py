'''
Найдите факториал числа x
'''
x = int(input('Введите X: '))

if x < 0:
    print('факториал отрицательного числа найти невозможно!')
else:
    factorial = 1
    i = 1

    while i <= x:
        factorial *= i
        i += 1
    print('Факториал числа', x, ':', factorial)
