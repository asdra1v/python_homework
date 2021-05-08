"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('test_for_ex03.txt', 'r', encoding="utf-8") as my_file:
    salary = []
    poor = []
    my_list = my_file.readlines()
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        salary.append(i[1])
print(f'Сотрудники с окладом менее 20.000 руб.: {", ".join(poor)}. \n'
      f'Cредний доход: {round(sum(map(float, salary)) / len(salary), 2)} руб.')