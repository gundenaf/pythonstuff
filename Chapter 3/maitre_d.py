#   Метрдотель
#   Демонстрирует условную интерпретацию значений

print("Добро пожаловать в Шато-де-Перекуси!")
print("Кажется, нынешним вечером у нас все столики заняты.")
tips = int(input("Сколько долларов вы готовы дать метрдотелю на чай? "))
if tips:
    print("""Прошу прощения, мне сейчас сообщили, что есть один свободный столик."
          Сюда, пожалуйста.""")
else:
    print("Присаживайтесь, будьте добры. Придётся подожать.")
input("\n\nHaжмитe Enter. чтобы выйти.")