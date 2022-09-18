"""Вычислить число c заданной точностью d"""

d = int(input('Введите количество знаков числа π после запятой: '))
import math
print(round((math.pi), d))



"""Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""

import sympy
n = int(input('Введите натуральное число: '))
if n == 1:
    print('Число не имеет простых множетелей.')
else:
    print('Простые множители этого числа:', end= ' ')
    for i in range(1, n+1):
        if sympy.isprime(i) == True and n % i == 0:
            print(i, end= ' ')



"""Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности."""

list = [int(i) for i in input('Введите ряд чисел: ').split()]
print('Неповторяющиеся элементы в этом ряду: ')
for i in list:
    if list.count(i) == len(list):
        print('отсутствуют.')
        break
    elif list.count(i) == 1:
        print(i, end= ' ')
print()
