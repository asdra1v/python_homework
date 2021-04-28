"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def summary():
    try:
        with open('test_for_ex05.txt', 'w+', encoding="utf-8") as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
        my_numbers = line.split()

        print(f"Сумма введённых чисел >>> {sum(map(int, my_numbers))}")
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()
