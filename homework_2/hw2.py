# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр(отсекаем минус, считаем все в плюс).

# number = input('Введи число: ')
# sum = 0
# for i in number:
#     if i != '.' and i != ',':
#         sum += int(i)
# print(sum)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from ntpath import join
import random

# number = int(input('Введи число: '))
# mult = 1
# sheet_fac = []
# str_fac = ', '
# sheet_num = ['']
# str_num = ', '
# for i in range (1,number+1):
#     sheet_fac.append(str(i*mult))
#     sheet_num.append(sheet_num[i-1]+str(i))
#     mult *= i
# sheet_num.remove('')
# print(f'Пусть N = {number}, тогда ' + '[' + ', '.join(sheet_fac) + '] (' + ', '.join(sheet_num) + ')')

# 3. Реализуйте случайное перемешивания списка.

stih = ['Шла','Саша','по','шоссе','и','сосала','сушку']
print(' '.join(stih))
input('Хочешь перемешать этот стишок?\n')
random.shuffle(stih)
print(' '.join(stih))