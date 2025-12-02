'''
Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в
функции.
'''
def permtr(a,b):
    per = 2 * (a + b)
    return per

def square(a,b):
    sqr = a * b
    return sqr

a = input('Введите ширину: ')
while type(a) != int:
    try:
        a = int(a)
        break
    except ValueError:
        print('Что-то не так, введите снова!')
        a = input('Введите ширину: ')

b = input('Введите высоту: ')
while type(b) != int:
    try:
        b = int(b)
        break
    except ValueError:
        print('Что-то не так, введите снова!')
        b = input('Введите высоту: ')

print('Периметр прямоугольника: ', permtr(a,b))
print('Площадь прямоугольника: ', square(a,b))