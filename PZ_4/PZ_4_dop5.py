'''
Ввести N чисел. Найти и вывести их среднее арифметическое.
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

total_sum = 0
count = 0
while count < n:
    try:
        num = float(input(f'Введите число {count+1}: '))
        total_sum += num
        count += 1
    except ValueError:
        print('Введите снова!')
average = total_sum / n

print(f'Среднее арифметическое {n} чисел: {average}')