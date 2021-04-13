quantity_user = int(input("Введите количество секунд: "))
quantity_hours = quantity_user // 3600
quantity_minutes = (quantity_user - (quantity_hours * 3600)) // 60
quantity_seconds = quantity_user - (quantity_hours * 3600) - (quantity_minutes * 60)
print("Итого >>> {}:{}:{}".format(quantity_hours, quantity_minutes, quantity_seconds))
