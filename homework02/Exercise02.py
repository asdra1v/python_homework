"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
user_input = input('Введите ряд произвольных данных для создания списка: ')
user_list = list(user_input)
el_count = 0
for elem in range(int(len(user_list) / 2)):
    user_list[el_count], user_list[el_count + 1] = user_list[el_count + 1], user_list[el_count]
    el_count += 2
print('Результат обмена: ', user_list)
