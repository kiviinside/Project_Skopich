'''
Составить функцию, которая выполнит суммирования числового ряда
'''
def sum_list(nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total

nums = [1, 2, 3, 4]
result = sum_list(nums)
print('Cумма ряда от 1 до 4:', result)