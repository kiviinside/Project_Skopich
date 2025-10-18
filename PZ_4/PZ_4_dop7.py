'''
Даны два целых числа А и В (А < В). Вывести в порядке убывания 
все целые числа, расположенные между А и В (включая сами числа А и В), 
а также количество этихчисел (использовать оператор цикла).
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

if a < b:
    total = 0
    current = a
    while current <= b:
        total += current
        current += 1
    
    print('Сумма всех чисел от', a, 'до', b, 'включительно:', total)
else:
    print('Ошибка!')
