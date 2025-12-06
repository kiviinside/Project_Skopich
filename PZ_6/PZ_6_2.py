'''
Дан целочисленный список размера N. Если он является перестановкой, то есть
содержит все числа от 1 до N, то вывести 0; в противном случае вывести номер
первого недопустимого элемента.
'''
import random

# N = int(input("Введите размер списка N: "))

lst = [1, 2, 3, 4]
#for i in range(N):
 #   lst.append(random.randrange(1, 50))

visited = [False] * 4 

print('Список:', lst)
for idx in range(4):
    num = lst[idx]

    if num < 1 or num > 4:
        print(idx + 1)
        break

    if visited[num - 1]:
        print(idx + 1)
        break
    visited[num - 1] = True

else:
    print(0)