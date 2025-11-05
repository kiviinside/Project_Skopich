'''
Дано два числа. Если их сумма кратна 5, то прибавь 1, иначе вычесть 2
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

sum = num1 + num2
if sum % 5:
    print(sum + 1)
else:
    print(sum - 2)