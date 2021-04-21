"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


arg1_in = int(input('Введите первый аргумент: '))
arg2_in = int(input('Введите второй аргумент: '))
arg3_in = int(input('Введите третий аргумент: '))
print(f"Результат >>> {my_func(arg1_in, arg2_in, arg3_in)}")
