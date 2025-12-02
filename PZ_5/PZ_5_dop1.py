'''
Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
результата предусмотреть в основной программе. Расчет суммы цифр оформить в
функции.
'''

def summ(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

a = input('Введите 1 число: ')
while type(a) != int:
    try:
        a = int(a)
        break
    except ValueError:
        print('Что-то не так, введите снова!')
        a = input('Введите 1 число: ')

b = input('Введите 2 число: ')
while type(b) != int:
    try:
        b = int(b)
        break
    except ValueError:
        print('Что-то не так, введите снова!')
        b = input('Введите 2 число: ')

c = input('Введите 3 число: ')
while type(c) != int:
    try:
        c = int(c)
        break
    except ValueError:
        print('Что-то не так, введите снова!')
        c = input('Введите 3 число: ')

SummA = summ(a)
SummB = summ(b)
SummC = summ(c)

if SummA>SummB and SummA>SummC:
    print('Наибольшая сумма у 1 числа')

if SummB>SummA and SummB>SummC:
    print('Наибольшая сумма у 2 числа')

if SummC>SummA and SummC>SummB:
    print('Наибольшая сумма у 3 числа')