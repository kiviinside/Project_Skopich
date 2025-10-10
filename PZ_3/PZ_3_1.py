'''
Дано трехзначное число. Проверить истинность высказывания: «Все цифры данного числа различны».
'''
print('Проверка высказывания «Все цифры данного числа различны».')
num = input('Введите трехзначное число: ')
while type(num) != int:
    try: 
        num = int(num)
    except ValueError:
        print('Неправильно ввели! ')
        num = input('Введите трехзначное число: ')

if 99<num<1000:
    hund = num//100
    tens = (num//10)%10
    ones = num%10
    if hund == tens or hund == ones or tens == ones:
        print('Высказывание ложно')
    else:
        print('Высказывание верно')
elif num<=99 or num>=1000:
    print('Число не трехзначное!')
