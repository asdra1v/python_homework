"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
if month == 1 or month == 12 or month == 2:
    print('Это', seasons_dict.get(1))
    print('Это определённо', seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print('Это', seasons_dict.get(2))
    print('Это определённо', seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print('Это', seasons_dict.get(3))
    print('Это определённо', seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print('Это', seasons_dict.get(4))
    print('Это определённо', seasons_list[3])
else:
    print("Такого месяца не существует")
