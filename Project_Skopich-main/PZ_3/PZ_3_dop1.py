
'''
Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противномслучае увеличить его в 1.5 раза. 
'''
num1 = input('Введите 1 число: ')

while True:
    try:
        num1 = int(num1)
        break
    except ValueError:
        print('Неправильно ввели')
        num1 = input('Введите 1 число: ')

num2 = input('Введите 2 число: ')

while True:
    try:
        num2 = int(num2)
        break
    except ValueError:
        print('Неправильно ввели')
        num2 = input('Введите 2 число: ')

mult = num1 * num2
if mult < 0:
    mult *= 8
    print(mult)
else:
    mult *=1.5
    print(mult)