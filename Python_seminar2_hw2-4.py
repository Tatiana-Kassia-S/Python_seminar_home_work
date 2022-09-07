"""Напишите программу, которая принимает на вход число N 
и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""

n = int(input('Введите число: '))
res = 1
for i in range(1, n):
    res *= i
    print(res, end= ', ')
print(res*n)


"""Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
и выведите на экран их сумму.
Пример:
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}"""

n = int(input('Введите число: '))
res = 0
for i in range(1, n):
    res += (1 + 1 / i) ** i
print(round(res, 2))


"""Реализуйте алгоритм перемешивания списка."""

list = []
print("Список 1: ", end= ' ')
import random
for i in range(10):
    list.append (random.randint(0, 10))
    print(list[i], end=' ')
random.shuffle(list)
print()
print("Cписок 2: ", end= ' ')
print(*list)