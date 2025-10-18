'''
Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).
'''

n = input('Введите целое число N: ')
while type(n) != int:
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
    
total_sum = 0
current_factorial = 1

for i in range(1, n + 1):
    current_factorial *= i 
    total_sum += current_factorial

print(f'S = 1! + 2! + ... + {n}! = {total_sum}')