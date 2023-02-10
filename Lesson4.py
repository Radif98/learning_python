'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.'''

# from random import randint
#
# n = int(input('Введите количество элементов первого множества: '))
# m = int(input('Введите количество элементов второго множества: '))
#
# list_first = [randint(1, 100) for i in range(n)]
# list_second = [randint(1, 100) for i in range(m)]
# print(*list_first)
# print()
# print(*list_second)
# print()
#
# '''set_first = set(list_first)
# set_second = set(list_second)
# print(*list(sorted(set_first.intersection(set_second))))'''
#
# set_third = set()
# for i in list_first:
#     for j in list_second:
#         if i == j:
#             set_third.add(i)
# print(*list(set_third))
#
# list_third = list(set_third)
# for k in range(len(list_third)):'''Написал пузырьковую сортировку по памяти'''
#     for i in range(len(list_third)-1):
#         if list_third[i] > list_third[i + 1]:
#             list_third[i + 1] = list_third[i] + list_third[i + 1]
#             list_third[i] = list_third[i + 1] - list_third[i]
#             list_third[i + 1] = list_third[i + 1] - list_third[i]
# print()
# print(*list_third)

'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
'''
from random import randint

N = int(input("Введите количество кустов: "))
list_bushes = []
for i in range(N):
    list_bushes.append(f"Куст_{i + 1}")

generator_yield = [randint(3, 10) for i in range(N)]
dict_bushes = {}
for i in range(len(list_bushes)):
    dict_bushes[list_bushes[i]] = generator_yield[i]
print(dict_bushes)

list_summa = []
for value in dict_bushes.values():
    print(f'Урожайность: {value}')
    list_summa.append(value)
print(list_summa)
summa = 0
joke = len(list_summa) - 1
for k in range(len(list_summa) - joke):
    summa = list_summa[len(list_summa) - 2] + list_summa[len(list_summa) - 1] + list_summa[0]
    for i in range(len(list_summa) - 1):
        if summa < list_summa[i - 1] + list_summa[i] + list_summa[i + 1]:
            summa = list_summa[i - 1] + list_summa[i] + list_summa[i + 1]
print(f'Максимальное число ягод, который может собрать собирающий модуль за один заход: {summa} ')



