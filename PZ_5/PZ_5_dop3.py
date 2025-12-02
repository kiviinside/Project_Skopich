'''
Написать программу, подсчитывающую количество цифр числа, используя для
этого функцию.
'''

def counting(n):
    count = 0
    n = int(n)
    while n > 0:
        n //= 10
        count += 1
    return count

a = input('Введите число: ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Введите целочисленное значение! ')
        a = input('Введите число: ')

print(f'В числе {counting(a)} цифр')