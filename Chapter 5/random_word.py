#   Вывод списка слов в случайном порядке без повторений

import random

WORDS = ["Соколиный глаз", "Капитан Америка", "Сорвиголова", "Каратель"]

check = set()
while len(check) != len(WORDS):
    check.add(random.choice(WORDS))
print(check)
print("\n\nНажмите Enter, чтобы выйти.")
