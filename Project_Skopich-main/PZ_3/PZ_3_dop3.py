'''
Дано двузначное число. Если сумма цифр числа четная, то увеличить число на 2,
в противном случае уменьшить на 2
'''
num = input('Введите число: ')

while True:
    try:
        num = int(num)
        break
    except:
        print('Ошибка! Неверно ввели. ')
        num = input('Введите число: ')

if 10<=num<=99:
    tens = num//10
    ones = num%10
    sum = tens + ones
    if sum % 2 == 0:
        print(num + 2)
    else:
        print(num * 2)
else:
    print('Число не двухзначное. ')