#   Отгадай число
import random

print("\t\tДобро пожаловать в игру 'Отгадай число'!")

print("""Я загадал натуральное число из диапозона от 1 до 100.
Постарайтесь отгадать его за минимальное число попыток.""")

count: int = 0
number: int = random.randint(1, 100)
print(number)
while count < 3:
    assumption = int(input("Ваше предположение: "))
    count += 1
    if assumption < number:
        print("Меньше...")
    elif assumption > number:
        print("Больше...")
    elif assumption == number:
        print("Вам удалось отгадать число! Это в самом деле %d" % number)
        print("Вы затратили на отгадывание всего лишь %d попыток!" % count)
        break

