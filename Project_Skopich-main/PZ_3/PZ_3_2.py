'''
Даны два числа. Вывести порядковый номер меньшего из них.
'''
num1 = input('Введите 1 число: ')
while True:
    try:
        num1 = int(num1)
        break
    except ValueError:
        print('Число введено не правильно')
        num1 = input('Введите 1 число: ')

num2 = input('Введите 2 число: ')
while True:
    try:
        num2 = int(num2)
        break
    except ValueError:
        print('Число введено не правильно')
        num2 = input('Введите 2 число: ')

if num2 < num1:
    print('1')
elif num1<num2:
    print('2')
else:
    print('Числа равны')