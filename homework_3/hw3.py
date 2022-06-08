# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# sheet = []
# print("Введи числа, чтобы заполнить список. Введи любой другой символ, чтобы закончить ввод.")
# while (True):
#     try:
#         num = input()
#         sheet.append(int(num))
#     except ValueError:
#         break
# print(sheet, ' ')
# sum = 0
# for i in range(1, len(sheet), 2):
#     sum += sheet[i]
# print(f'Сумма элементов стоящих на нечетных позициях: {sum}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Если остается 1 элемент без пары - 
# умножаем его самого на себя.

# import math
# sheet = []
# mult = []
# print("Введи числа, чтобы заполнить список. Введи любой другой символ, чтобы закончить ввод.")
# while (True):
#     try:
#         num = input()
#         sheet.append(int(num))
#     except ValueError:
#         break
# # print(math.ceil(len(sheet)/2))
# for i in range(math.ceil(len(sheet)/2)):
#     # print(sheet[i])
#     # print(sheet[len(sheet)])
#     # print(f'sheet[{i}] = {sheet[i]}, sheet[{len(sheet)-i}] = {sheet(len(sheet)-i)}')
#     mult.append(sheet[i]*sheet[len(sheet)-i-1])
# print(''.join(str(sheet)) + " => " + ''.join(str(mult)))
 
# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# sheet = []
# max = 0.0
# min = 1.0
# print("Введи числа, чтобы заполнить список. Введи любой другой символ, чтобы закончить ввод.")
# while (True):
#     try:
#         num = input()
#         sheet.append(float(num))
#     except ValueError:
#         break
# for i in sheet:
#     j = i
#     j = j - int(j)
#     if min > j: min = j
#     if max < j: max = j
# print(''.join(str(sheet))+' => '+ str(max-min))
# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19