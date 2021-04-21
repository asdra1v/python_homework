"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
"""

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Год рождения: ')
city = input('Город проживания: ')
email = input('Введите адрес эл.почты: ')
phone = input('Введите номер телефона: ')


def user_data(name1, surname1, year1, city1, email1, phone1):
    return ' '.join([name1, surname1, year1, city1, email1, phone1])


print(user_data(name, surname, year, city, email, phone))
