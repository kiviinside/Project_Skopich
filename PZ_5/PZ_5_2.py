'''
Описать функцию Power1(A, B) вещественного типа, находящую величину AB по
формуле AB = exp(B*ln(A)) (параметры A и B — вещественные). В случае нулевого
или отрицательного параметра A функция возвращает 0. С помощью этой функции
найти степени A^P, B^P, C^P, если даны числа P, A, B, C.
'''
import math

def Power1(A, B):
    if A <= 0:
        return 0
    return math.exp(B * math.log(A))

try:
    P = float(input("Введите степень P: "))
    A = float(input("Введите число A: "))
    B = float(input("Введите число B: "))
    C = float(input("Введите число C: "))
    
    result_A = Power1(A, P)
    result_B = Power1(B, P)
    result_C = Power1(C, P)
    
    print(f"\nРезультаты:")
    print(f"A^P = {result_A}")
    print(f"B^P = {result_B}")
    print(f"C^P = {result_C}")
    
except ValueError:
    print("Ошибка! Пожалуйста, вводите только числа.")

