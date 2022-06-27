# 34. Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
# from re import X
# from this import d
# from tkinter import N

from gettext import find
"""
В общем такое дело:
Я использовал сгенерированную библиотеку формата {'x^0' : 0}, {'x^1': 0}, {'x^2': 0} и так далее, для удобного, кмк, анализа(ключи) и записи(значения)
каждого члена многочлена. Но я не учёл особенности чтения подстроки из словаря в элементке списка  и прох
"""


oper = ['-','+']
path_1 = 'C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_6/first_polynomial.txt'
path_2 = 'C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_6/second_polynomial.txt'
"""
Будущий метод.
"""
# def preobrazovatel(path, data):
#     data = path.read()
#     some_list = (data.rstrip(data[-1])).rsprip(some_list[-3:-1])
#     if len(pre_list) > 1:
#         final_list = [pre_list[0]]
#         for i in range(1, len(pre_list), 2):
#             final_list.append(pre_list[i]+pre_list[i+1])
#     return final_list
"""
"""
with open(path_1,'r') as first_pol, open(path_2,'r') as second_pol:
    data_1 = first_pol.read()
    pre_list = data_1.rstrip(data_1[-1])
    # столкнулся с проблемой удаления последних символов: программа не хочет удалять сразу диапазон [-3:-1] в той же переменной pre_list, получаемой из data_1.
    # пришлось перезаписать переменную
    pre_list = pre_list.rstrip(pre_list[-3:-1])
    # создаем список без пробелов
    first_list = pre_list.split(' ')
    # если многочлен состоит из более одного члена, то каждый четный элемент списка, являющийся знаком, соединяем с последующим, создавая новый список
    if len(first_list) > 1:
        third_list = [first_list[0]]
        for i in range(1,len(first_list), 2):
            third_list.append(first_list[i]+first_list[i+1])
    # когда разберусь с проблемой безостановочного прохода цикла, использую метод preobrazovatel() и, вероятно, назову его более лаконично 
    # first_list = preobrazovatel(path_1, first_pol)
    # second_list = preobrazovatel(path_2, second_pol)
    data_2 = second_pol.read()
    pre_list_2 = data_2.rstrip(data_2[-1])
    pre_list_2 = pre_list_2.rstrip(pre_list_2[-3:-1])
    second_list = pre_list_2.split(' ')
    if len(second_list) > 1:
        fourth_list = [second_list[0]]
        for i in range(1,len(second_list), 2):
            fourth_list.append(second_list[i] + second_list[i+1])
    # просто вывод многочленов до и после присоединения знаков
    print(f'{first_list} + {second_list} \n {third_list} + {fourth_list}')
"""
Создание словаря
"""

dic = {f'x^{x}': 0 for x in range(0,8)}

"""
Будущий метод
"""
# def delegating(array, ):
#     while len(third_list) > 1:
#         for i in third_list:
#             for key in dic.keys():
#                 if key in i:
#                     dic[key] += int(third_list.pop(third_list.index(i)).replace(key,''))
#                 elif i.replace(i[0],'').isdigit():
#                     dic['x^0'] += int(i)
#                     break
#     res = 0
#     return res

"""
Вот здесь мне непонятно: внешний цикл из элементов списка членов многочлена и внутренний из ключей списка.
Т.о., если подстрока (ключ) входит в элемент многочлена, программа удалит этот элемент и, отбросив ключ в элементе, добавит в значение по ключу.
С первым элементом проблем не возникло, но дальше, почему-то, программа не выходит из цикла, а продолжает перебирать все ключи...эта задача меня истощила.
Чучут передохну и снова в бой!  
"""
while len(third_list) > 1:
    # print(f'{third_list}')
    # input()
    for i in third_list:
        # print(f'{i}')
        # input()
        for key in dic.keys():
            # print(f'After getting key, i: {key}, {i}')
            # input()
            if key in i:
                dic[key] += int(third_list.pop(third_list.index(i)).replace(key,''))
                break
            elif i.replace(i[0],'').isdigit():
                i = i[1:]
                dic['x^0'] += int(third_list.pop())
                break
# for i in third_list:
#     for key in dic.keys():
#         if i not in dic.keys():
#             print(f'if i not in dic.keys(): {key} {i}')
#             i = i[1:]
#             dic['x^0'] += int(third_list[0])
#             print(dic)
#             break
# dic['x^1'] += int(third_list[0].replace('x', ''))

"""
Абсолютно та же история, что и в предыдщем блоке.
"""
while len(fourth_list) > 1:
    for i in fourth_list:
        for key in dic.keys():
            # print(f'After getting key, i: {key}, {i}')
            if i in key:
                # print(f'start:{key in i}')
                # print(i.replace(i[0],'').isdigit())
                # print('second one, key in i')
                # print(key, i)
                # print(f'dic[key]: {dic[key]}')
                dic[key] += int(fourth_list.pop(fourth_list.index(i)).replace(key,''))
                # print(f'end: {fourth_list}')
                break
            else:
                if i.replace(i[0],'').isdigit():
                    # print(i, i.replace(i[0],'').isdigit(), fourth_list)
                    try:
                        # print('second one, i.replace(i[0])')
                        # print(key, i)
                        dic['x^0'] +=int(fourth_list.pop())
                        # print(f'4th list: {fourth_list}')
                        # print(i.replace(i[0],'')).replace(i[len(i)-1],'')
                        break
                    except AttributeError:
                        pass
                elif i.find('x') == 1 and i.find('^') == 0:
                    # print(f'X: {fourth_list}')
                    # print(i.replace(i[0],'')).replace(i[len(i)-1],'')
                    dic['x^1'] +=int(fourth_list.pop(i.find('x')))
# dic['x^1'] += int(fourth_list[0].replace('x', ''))


# Здесь мы меняем ключи, чтобы красивее записать в файл результат.
dic['x'] = dic['x^1']
del dic['x^1']
dic['a'] = dic['x^0']
del dic['x^0']

# Здесь собирается результат суммы многочленов
stri =''
for key, value in dic.items():
    if value != 0 and len(stri) == 0:
        stri += str(value)
        stri += key
    elif value != 0 and len(stri) > 0:
        if str(value)[0] == '-':
            stri += (f' - {str(value*(-1))}')
            stri += key
        else:
            stri += ' + '
            stri += str(value)
            stri += key
print(stri)
with open('C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_6/solve.txt','w') as solving:
    solving.write(stri + ' = 0')

# 39. Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 

# 42. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
"""
def encode():
    with open('C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_6/string_to_encode.txt','r') as data_1, open('C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_6/string_after_encode.txt','w') as data_2:
        enc_string = data_1.read()
        encoding = [] # сохраняет выходной список
        i = 0
        while i < len(enc_string):
            # подсчитывает количество вхождений символа в индексе `i`
            count = 1
            while i + 1 < len(enc_string) and enc_string[i] == enc_string[i + 1]:
                count = count + 1
                i = i + 1
                # добавляет к результату текущий символ и его количество
            encoding.append(count)
            encoding.append(enc_string[i])
            i = i + 1
        # так как записать в текстовый файл можно строку, используем метод .join для записи строки. данный метод работает только со string форматом,
        # так что необходимо преобразовать все целочисленные элементы списка в строковые
        writeable_string = ' '.join(map(str, encoding))
        return data_2.write(writeable_string)

def decode():
    with open('C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_6/string_after_decode.txt','w') as data_1, open('C:/Users/LevitskiyMD/PYHW/Py_HomeWork/homework_6/string_after_encode.txt','r') as data_2:
        decode = ''
        encoded_string = data_2.read().split(' ')
        # используем противоположный вышеуказанному метод и "сплитим" строку для последущей работы не построчно, а по элементам
        for i in range(len(encoded_string)-1):
            if i%2 == 0:
                decode += int(encoded_string[i]) * str(encoded_string[i+1])
        return data_1.write(decode)

encode()
decode()
"""