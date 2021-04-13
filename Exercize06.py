first_day = int(input("Введите результат спортсмена в первый день >>> "))
final_distance = int(input("Введите необходимый результат >>> "))
day = 1
while first_day < final_distance:
    first_day = first_day * 1.1
    day = day + 1

print("На ", day, "-й день спортсмен достигнет результата в", final_distance, "км")
