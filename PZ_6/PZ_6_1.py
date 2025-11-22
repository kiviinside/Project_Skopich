'''
Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму всех
элементов списка, кроме элементов с номерами от K до L включительно.
'''
N = int(input('Введите размер списка: '))
lst = []
print(f'Введите {N} целых чисел по одному: ')

for i in range(N):
    num = int(input(f'Введите {i + 1} элемент: '))
    lst.append(num)

K = int(input('Введите K (1 < K < L < N): '))
L = int(input('Введите L (1 < K < L < N): '))

if not (1 < K < L < N):
    print('Вы неправильно ввели!')
else:
    total_sum = 0
    
    for i in range(0, K - 1):
        total_sum += lst[i]
    
    for i in range(L, N):
        total_sum += lst[i]

    print('Сумма всех элементов, кроме элементов с номерами от K до L включительно:', total_sum)