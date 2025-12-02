'''
Дан целочисленный список размера N. Если он является перестановкой, то есть
содержит все числа от 1 до N, то вывести 0; в противном случае вывести номер
первого недопустимого элемента.
'''

N = int(input("Введите размер списка N: "))

lst = []
print(f"Введите {N} целых чисел:")
for i in range(N):
    num = int(input(f"Элемент {i + 1}: "))
    lst.append(num)

visited = [False] * N  

for idx in range(N):
    num = lst[idx]

    if num < 1 or num > N:
        print(idx + 1)
        break

    if visited[num - 1]:
        print(idx + 1)
        break
    visited[num - 1] = True

else:
    print(0)