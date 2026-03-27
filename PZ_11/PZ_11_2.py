'''
.Из заданной строки отобразить только цифры. Использовать библиотеку string. 
Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
481 feet (147 metres) high.
'''

from string import digits 

string = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."
nums = [i for i in string if i in digits]
print(nums)