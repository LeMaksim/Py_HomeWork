# 1. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# input_number = int(input())
# backward_binary_number = []
# while input_number > 0:
#     backward_binary_number.append(input_number%2)
#     input_number //= 2
# backward_binary_number.reverse()
# binary_number = int(''.join(map(str, backward_binary_number)))
# print(binary_number)    

# 2. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    
# number = int(input())
# count = 2
# sheet = [0,1]
# while count <= number:
#     sheet.append(sheet[count-2]+sheet[count-1])
#     count += 1
# count -= 2
# sheet.reverse()
# while count >= 0:
#     sheet.append(sheet[count] * ((-1)**(count+1)))
#     count -= 1
# sheet.reverse()
# print(sheet)

# 3. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве 
#    символа-разделителя используйте пробел.

# import keyboard

# print('Would you like to initiate arra(Y) or use made(N)?')
# def Auto_or_manual():
#     while True:
#         keyboard.wait('n')
#         print('Are you sure?')
#         keyboard.wait('y')
#         return "1 -2 10 55 3 20 6"

# def min_max_in_string(string_numbers):
#     list_string_numbers = list(map(int, string_numbers.split(' ')))
#     print(list_string_numbers)
#     result = {'min': None, 'max': None}
#     result['min'] = list_string_numbers.pop()
#     result['max'] = list_string_numbers.pop()

#     for number in (list_string_numbers):   
#         if result['min'] < number:
#             pass
#         elif result['min'] > number:
#             result['min'] = number

#         if result['max'] > number:
#             pass
#         elif result['max'] < number:
#             result['max'] = number
            
#     return result

# print(min_max_in_string(Auto_or_manual()))

# 4. Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

first_number = int(input())
second_number = int(input())
lmc = None # НОК
if second_number < first_number:
    temp = second_number
    second_number = first_number
    first_number = temp
second_number += 1
for i in range(int(second_number/2), 2, -1):
    if second_number%i == 0:
        if first_number%i == 0:
            lmc = i* second_number
            break
if lmc == None:
    lmc = second_number * first_number
print(lmc)
# работает не всегда