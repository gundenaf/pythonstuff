#   Кто твой папа?

father = {"Сергей": "Юрий Сергеевич",
          "Александр": "Вадим Александрович",
          "Алексей": "Святослав Алексеевич",
          "Иван": "Сергей Иванович",
          "Роман": "Егор Романович",
         }

choice = None
while choice != "0":
    print(
        """
        Кто твой папа?
        0 - Выйти
        1 - Найти отца по имени сына
        2 - Добавить отца по имени сына
        3 - Изменить имя отца по имени сына
        4 - Удалить отца по имени сына
        """
    )
    choice = input("Ваш выбор: \n")
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        son = input("Введите имя сына ")
        if son in father:
            definition = father[son]
            print("\n", son, "сын", definition)
        else:
            print("\nУвы, мы не можем найти отца по имени сына:", son)
    elif choice == "2":
        son = input("Добавьте отца по имени сына ")
        if son not in father:
            definition = input("\nВпишите имя и отчество отца ")
            father[son] = definition
            print("\nОтец", son, "добавлен в список")
        else:
            print("\nУвы, мы не можем найти отца по имени сына:", son)
    elif choice == "3":
        son = input("Впишите имя сына для изменения имени отца ")
        if son in father:
            definition = input("Впишите имя и отчество отца ")
            father[son] = definition
            print("\nДанные по отцу", son, "изменены.")
        else:
            print("\nТакого отца пока нет! Попробуйте добавить его в список.")
    elif choice == "4":
        son = input("Введите имя сына для удаления пары? ")
        if son in father:
            del father[son]
            print("\nОтец", son, "удален.")
        else:
            print("\nНичем не могу помочь, такого отца", son, "нет в списке")
    else:
        print("Извините, в меню нет такого пункта", choice)

input("\n\nHaжмитe Enter. чтобы выйти.")

