#   Арсенал героя
#   Демонстрирует создание кортежа
inventory = ()  # создадим пустой кортеж
if not inventory:  # рассмотрим его как условие
    print("Вы безоружны.")
input("\nНажмите Enter, чтобы продолжить.")
inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")  # теперь создадим кортеж с несколькими элементами
print("\nСодержимое кортежа", inventory)  # выведем этот кортеж на экран
print("\nИтак, в вашем арсенале:")
for item in inventory:  # выведем все элементы последовательно
    print(item)
input("\n\nНажмите Enter, чтобы выйти.")
