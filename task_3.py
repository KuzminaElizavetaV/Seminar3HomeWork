'''Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
 минимальным значением дробной части элементов.

*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''
import math

def DiffMaxMinList(list):
    Diff = max(list) - min(list)
    return Diff

list_float = []
list_float_new = []
list_len = int(input("Введите размер массива: "))
i = 1
j = 0

while i <= list_len:
    list_float.append(float(input("Введите элемент массива (целое или дробное число): ")))
    i += 1

while j < len(list_float):
    d = list_float[j] - math.floor(list_float[j])
    if (d).is_integer() !=True:
        list_float_new.append(round(d, 2))
        j += 1
    else:
        j += 1

print(f"{list_float} => {DiffMaxMinList(list_float_new)}")




