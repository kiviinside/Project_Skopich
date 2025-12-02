'''
Составить функцию, которая выполнит суммирования числового ряда
'''
def sum_numbers():
    while True:
        try:
            n = int(input("Сколько чисел вы хотите ввести? "))
            if n < 0:
                print("Количество чисел не может быть отрицательным. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")
    total = 0
    count = 0
    while count < n:
        try:
            number = float(input(f"Введите число {count + 1}: "))
            total += number
            count += 1
        except ValueError:
            print("Это не число. Попробуйте снова.")
    print(f"Сумма введённых чисел: {total}")

sum_numbers()