#   Кости
#   Демонстрирует генерацию случайных чисел
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2
print("При вашем броске выпало", die1, "и", die2, "очков в сумме", total)
input("\n\nHaжмитe Enter. чтобы выйти.")
