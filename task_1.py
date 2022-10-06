'''Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
    *Пример:*

    - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

import random

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

n = int(input("Задайте размер массива: "))
list = [random.randint(1, 9) for _ in range(n)]
list_new = list[1::2]
print(f"{list} -> на нечетных позициях элементы {list_new}, ответ: {listsum(list_new)}")
