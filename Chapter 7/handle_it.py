#   Обработаем
#   Демонстрирует обработку исключительных ситуаций
#   try/except

try:
    num = float(input("Введите число: "))
except ValueError as e:
    print("Это не число! Интерпретатор как бы говорит нам:")
    print(e)

print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я умею преобразовывать только строки и числа!")
    except ValueError:
        print("Я умею преобразовывать только строки, составленные из цифр!")

try:
    num = float(input("\nВведите число: "))
except ValueError:
    print("Вы ввели число ", num)

input("\n\nНажмите Enter, чтобы выйти.")
