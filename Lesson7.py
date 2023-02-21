'''Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
если с ритмом все не в порядке

Ввод:

пара-ра-рам рам-пам-папам па-ра-па-да

Вывод:
Парам пам-пам'''

# some_str = input('Введите стих: ')
# vowels_list = ["а", "у", "о", "ы", "э", "я", "ю", "ё", "и", "е"]
# count_list = []
# def count_vowels(some_str, count = 0):
#     phrase_list = some_str.split()
#     for phrase in phrase_list:
#         for i in range(len(phrase)):
#             if phrase[i] in vowels_list:
#                 count += 1
#         count_list.append(count)
#         count = 0
#     return count_list
# def checking(some_list):
#     if len(set(some_list)) == 1:
#         return 'Парам пам-пам'
#     else:
#         return 'Пам парам'
#
# count_list = count_vowels(some_str)
# print(checking(count_list))


'''Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
(подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
как, например, у операции умножения.

Ввод:     
print_operation_table(lambda x, y: x * y) 
Вывод:
1 2 3 4 5 6

2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36'''

import time

# start = time.perf_counter()
# def operation(some_object, len_columns):
#     table_list = []
#     write_list = list(some_object)
#     for i in range(2, len_columns + 1):
#         for j in range(len(some_object)):
#             write_list[j] = some_object[j] * i
#         table_list.append(tuple(write_list))
#     return table_list
# def print_operation_table(a, b):
#     for i in range(b - 1):
#         print(*list(a[i]))
#
# num_rows = int(input("Введите номер строки: "))
# num_columns = int(input("Введите номер столбца: "))
# rows = tuple([i for i in range(1, num_columns + 1)])
# print(*rows)
# table_list = operation(rows, num_rows)
# print()
# print(print_operation_table(table_list, num_rows))
# end = time.perf_counter()
# print(end - start)

start = time.perf_counter()
def operation(x, y):
    table_list = []
    for i in range(1, len(y)):
        for j in range(len(x)):
            table_list.append(y[i] * x[j])
    return table_list

def print_operation_table(some_list, x, y):
    a = 0
    for _ in range(x):
        print(*some_list[a:y + a])
        a += y

num_rows = int(input("Введите номер строки: "))
num_columns = int(input("Введите номер столбца: "))
first_rows = [i for i in range(1, num_columns + 1)]
print(*first_rows)
print()
first_columns = [i for i in range(1, num_rows + 1)]
table_list = operation(first_rows, first_columns)
print_operation_table(table_list, num_rows, num_columns)
end = time.perf_counter()
print(end - start)