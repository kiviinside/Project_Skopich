'''
Найти и вывести на экран квадраты и кубы чисел от 2 до 5.
'''
print("Число, Квадрат, Куб")
num = 2
while num <= 5:
    square = num ** 2
    cube = num ** 3
    print(num, square, cube)
    num += 1