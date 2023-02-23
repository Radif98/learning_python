'''Напишите функцию read_last(lines, file),
которая будет открывать определенный файл file
и выводить на печать построчно последние строки в количестве lines
(на всякий случай проверим, что задано положительное целое число)'''

# def read_last(lines, file):
#     if lines < 0:
#         print('error')
#     else:
#         for string in file[len(file) - lines:]:
#             print(string)
#
#
# lines = int(input("Введите какое количество строк нужно вывести: "))
# with open('article.txt', 'r', encoding='utf-8') as file:
#     read_last(lines, file.read(). splitlines())


'''Требуется реализовать функцию longest_words(file), которая выводит слово, 
имеющее максимальную длину (или список слов, если таковых несколько).'''

# def longest_words(file):
#     words_list = []
#     max_len_word = ''
#     for word in file:
#         if len(word) > len(max_len_word):
#             max_len_word = word
#     for word in file:
#         if len(word) == len(max_len_word):
#             words_list.append(word)
#     for word in words_list:
#         print(word)
#
#
# with open('article.txt', 'r', encoding='utf-8') as file:
#     longest_words(file.read().rsplit())

'''Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. 
У нас труб будет больше.
Бассейн можно заполнить из N труб. 
В файле pipes.txt записаны времена заполнения всего бассейна 
только одной данной работающей трубой (в часах). 
Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.
Сколько минут на это потребуется?
Номер трубы соответствует номеру строки, в которой записана ее производительность.

Результат запишите в файл time.txt

Пример
Ввод

1
2
3
(пустая строка)
1 2 3

Вывод
32.72727272727273'''

def correct_list(some_list):
    for i in range(len(some_list)):
        if some_list[i] == '':
            some_list.pop(i)
            break
    return data_list


def creat_num_pipes_list(some_list):
    for el in some_list[-1:]:
        num_pipes = el.split()
    return num_pipes


def find_time(list_1, list_2):
    speed = 0
    for num in list_2:
        speed += 1 / (int(list_1[int(num) - 1]) * 60)
    return 1 / speed

with open('pipes.txt', 'r', encoding='utf-8') as file:
    data_list = file.read().splitlines()
    data_list = correct_list(data_list)
    num_pipes_list = creat_num_pipes_list(data_list)
    print(find_time(data_list, num_pipes_list))
