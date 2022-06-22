# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
import random
from random import randint


degree = int(input('Введи натуральную степень\n'))
data = open('C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_5/polynomial.txt', 'w+')
funk = []
oper = ['-','+']
for i in range(degree, 0, -1):
    if i != 0:
        if i == 1:
            funk.append(f'{random.randint(0,100)}x')
        funk.append(f'{random.randint(0,100)}x^{i} {random.choice(oper)}')
data.write((' '.join(funk)).rstrip(funk[-1]) + ' = 0')
data.close()

# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# number = None
# nabor = []
# data = open('C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_5/int_array.txt', 'w+')

# try:
#     number = input('Хочешь сам задать количество чисел? Если "да", то лучше 50-100. Если лень - пиши "нет" или сразу число.\n')
#     if number.lower() == "да":
#         chislo = 0
#         print('Напиши "стоп" чтобы перестать.')
#         while True:
#             chislo += 1
#             pre_ar = input(f'{chislo}: ')
#             if pre_ar.lower() == "стоп":
#                 data.write(' '.join(map(str, nabor)))
#                 data.close()
#                 break
#             if pre_ar.isdigit() == True:
#                 nabor.append(int(pre_ar))
#     elif number.lower() == 'нет':
#         for i in range(30):
#             nabor.append(randint(-10, 10))
#         data.write(' '.join(map(str, nabor)))
#         data.close()
#     elif number.isdigit():
#         for i in range(int(number)):
#             nabor.append(randint(-10, 10))
#         data.write(' '.join(map(str, nabor)))
#         data.close()
# except ValueError:
#     data.write(' '.join(map(str, nabor)))
#     data.close()
# except IndexError:
#     data.write(' '.join(map(str, nabor)))
#     data.close()
# except KeyboardInterrupt:
#     data.write(' '.join(map(str, nabor)))
#     data.close()
# data = open('C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_5/int_array.txt', 'r+')
# som_str = data.read().split(' ')
# another_string = list(map(int, som_str))
# data.close()
# print(nabor)
# for i in range(1,len(nabor)):
#     if (another_string[i-1]) == ((another_string[i]) - 1):
#         print(f'Условие A[i] - 1 = A[i-1] (или, проще: A[i] = A[i-1] + 1) выполняется у {i} элемента: {int(som_str[i-1])} ({i+1} элемент = {int(som_str[i])})')
#         break
#     elif (another_string[i-1]) != ((another_string[i]) - 1) and (i == len(nabor) - 1): print("К сожалению, тебе не повезло. Не отчаивайся! Попробуй ещё!")


# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# spisok = [randint(-5, 5) for i in range(10)]
# print(spisok)
# unique = []
# count = 0
# for i in spisok:
#     count = spisok.count(i)
#     if count == 1:
#         unique.append(i)
# print(f'Список: {spisok}')
# if len(unique) != 0:
#     print(f'Уникальные символы: {unique}')
# else: print('В списке нет уникальных элементов.')