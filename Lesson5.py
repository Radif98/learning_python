'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''

# def pow_my_version(A, B):
#     if B == 0:
#         return 1
#     elif B == 1:
#         return A
#     else:
#         return A * pow_lol(A, B - 1)
#
# print(pow_lol(3, 5))


'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
2 2
4'''

def summa_my_version(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return summa_my_version(a - 1, b - 1) + 1 + 1


print(summa_my_version(2, 2))

