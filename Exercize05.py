vyruchka = float(input("Введите значение выручки: "))
izderzhki = float(input("Введите значение издержек: "))
if vyruchka == izderzhki:
    print("Вы ничего не заработали...")
elif vyruchka < izderzhki:
    print("Выручка меньше  издержек.")
elif vyruchka > izderzhki:
    print("Выручка больше издержек.")
    rentab = ((vyruchka - izderzhki) / vyruchka) * 100
    print("Рентабельность выручки составила:", "{0:.2f}".format(rentab), "%")
    chislo_sotr = int(input("Введите количество сотрудников: "))
    vyrucka_na_odnogo = (vyruchka - izderzhki) / chislo_sotr
    print("Прибыль фирмы в расчёте на одного сотрудника: ", "{0:.2f}".format(vyrucka_na_odnogo), " руб.")
