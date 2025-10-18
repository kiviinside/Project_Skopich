'''
Дано целое число N (>0). Если оно является степенью числа 3, 
то вывести TRUE, если не является — вывести FALSE.
'''

n = input('Введите целое число N: ')
while type(n) != int(n):
    try:
        n = int(n)
        if n > 0:
            break
        elif n <= 0:
            print('Неправильно, число должно быть положительным!')
            n = input('Введите целое число N: ')
    except ValueError:
        print('Что-то не так, введите снова!')
        n = input('Введите целое число N: ')

if n == 1:
    print(True)

else:
    t = n
    while t % 3 == 0:
        t = t//3
    
    if t == 1:
        print(True)
    else:
        print(False)
    
