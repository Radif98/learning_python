'''Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''

# n = int(input('Введите количество элементов с массива: '))
# a_1 = int(input('Введите первый элемент массива: '))
# d = int(input('Введите  разность: '))
#
# some_list = [a_1]
#
# for i in range(2, n):
#     some_list.append(a_1 + (i - 1) * d)
#
# print(*some_list)


''' Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

from random import randint

some_list = sorted([randint(1, 50) for _ in range(20)])
print(some_list)

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

index_list = []
index_dict = {}
for i in range(len(some_list)):
    if start < some_list[i] < end:
        index_list.append(i)
        index_dict[some_list[i]] = f'index:{i}'

print(index_list)
for item in index_dict.items():
    print(item)
