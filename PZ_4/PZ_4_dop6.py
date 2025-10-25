'''
Ввести N чисел. Посчитать и вывести количество чисел равных нулю.
'''
n = input('Введите количество чисел N: ')
while type(n) != int:
    try:
        n = int(n)
        if n > 0:
            break
        else:
            print('Ошибка! Введите положительное число.')
            n = input('Введите количество чисел N: ')
    except:
        print('Ошибка!')
        n = input('Введите количество чисел N: ')

zero = 0
count = 0
while count < n:
    try:
        num = float(input('Введите число: '))
        if num == 0:
            zero += 1
        count += 1
    except ValueError:
        print('Ошибка!')

print('Количество чисел, равных нулю:', zero)

