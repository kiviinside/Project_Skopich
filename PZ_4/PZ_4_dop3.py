'''
Найти и вывести на экран квадраты и кубы чисел от 2 до 5.
'''
print("Число\tКвадрат\tКуб")
num = 2
while num <= 5:
    square = num ** 2
    cube = num ** 3
    print(f"{num}\t{square}\t{cube}")
    num += 1