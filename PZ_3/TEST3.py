'''
Если число делится только само на себя и 1 вывести true, иначе - false
'''
x = int(input('Введите X: '))
if x < 2:
    print(False)
else:
    lala = True
    i = 2
    while i * i <= x:
        if x % i == 0:
            lala = False
            break
        else:
            i+= 1
            continue
    print(lala)