"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_file = open('test_for_ex01.txt', 'w', encoding="utf-8")
line = input('Введите текст или нажмите ввод для выхода >>> \n')
while line:
    my_file.writelines(line + '\n')
    line = input('Введите текст или нажмите ввод для выхода>>> \n')
    if not line:
        break

my_file.close()
my_file = open('test_for_ex01.txt', 'r', encoding="utf-8")
for content in my_file.readlines():
    print(content.replace('\n', " "))
my_file.close()
