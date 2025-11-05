'''
Ввести число. Если оно четное , разделить его на 4, если нечетное - умножить на 5
'''
num = input('Введите число: ')
while True:
    try:
        num = int(num)
        break
    except:
        print('Ошибка! Неверно ввели. ')
        num = input('Введите число: ')

if num%2 == 0:
    print(num/4)
else:
    print(num*5)
