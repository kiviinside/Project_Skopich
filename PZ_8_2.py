'''
Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16', отражающая 
продажи продукции по дням в кг. Преобразовать информацию из строки в словари, 
с использованием функции найти максимальные продажи по каждому виду 
продукции, результаты вывести на экран. 
'''
data = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
parts = data.split()

sales = {}
current_product = None

for part in parts:
    if part.isdigit():
        sales[current_product].append(int(part))
    else:
        current_product = part
        sales[current_product] = []

def find_max_sales(sales_dict):
    max_sales = {}
    for product, values in sales_dict.items():
        max_sales[product] = max(values)
    return max_sales

max_sales = find_max_sales(sales)


for product, max_value in max_sales.items():
    print(f"{product}: {max_value} кг")
