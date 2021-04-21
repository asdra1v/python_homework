"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_sum(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        return print("На ноль делить нельзя !")


print("Деление двух чисел >>> ")
number_1 = float(input("Введите число 1 : "))
number_2 = float(input("Введите число 2 : "))
print(my_sum(number_1, number_2))
