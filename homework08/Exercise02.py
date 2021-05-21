"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):

    def div_function(self, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} -> На ноль делить нельзя!\n")
        else:
            print(f"{a} / {b} = {res} \n")


my_exception = MyException()

my_exception.div_function(8, 16)
my_exception.div_function(6, 0)
my_exception.div_function(-10, 32)
my_exception.div_function(0, 12)
