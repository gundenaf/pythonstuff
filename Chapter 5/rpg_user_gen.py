#   Генератор персонажей

points = 30
health = 0
agility = 0
wisdom = 0
strength = 0

choice = None
while choice != "0":
    print(
        """
        Закиньте характеристики:
        0 - Выйти
        1 - Добавить здоровья
        2 - Добавить силы
        3 - Добавить мудрость
        4 - Добавить ловкость
        5 - Отобразить значения
        """
    )
    choice = input("Ваш выбор: \n")
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        print("У вас осталось %d очков для распределения" % points)
        health = int(input("Впишите количество скилла: "))
        if points > 0 and points > health:
            points -= health
            print("У вас осталось %d очков для распределения" % points)
        else:
            print("Вы вводите неккоректное значение!")
    elif choice == "2":
        print("У вас осталось %d очков для распределения" % points)
        strength = int(input("Впишите количество скилла: "))
        if points > 0 and points > strength:
            points -= strength
            print("У вас осталось %d очков для распределения" % points)
        else:
            print("Вы вводите неккоректное значение!")
    elif choice == "3":
        print("У вас осталось %d очков для распределения" % points)
        wisdom = int(input("Впишите количество скилла: "))
        if points > 0 and points > wisdom:
            points -= wisdom
            print("У вас осталось %d очков для распределения" % points)
        else:
            print("Вы вводите неккоректное значение!")
    elif choice == "4":
        print("У вас осталось %d очков для распределения" % points)
        agility = int(input("Впишите количество скилла: "))
        if points > 0 and points > agility:
            points -= agility
            print("У вас осталось %d очков для распределения" % points)
        else:
            print("Вы вводите неккоректное значение!")
    elif choice == "5":
        print("Оставшееся количество очков: %d" % points)
        print("Очки здоровья: %d" % health)
        print("Очки силы: %d" % strength)
        print("Очки мудрости: %d" % wisdom)
        print("Очки ловкости: %d" % agility)

