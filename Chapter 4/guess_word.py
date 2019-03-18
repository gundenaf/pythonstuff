#   Угадай слово

import random

WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
print(len(word))
count = 5
while count > 0:
    guess_letter = str(input("Попробуйте отгадать букву: "))
    if guess_letter.lower() in word:
        print("Такая буква есть.")
        guess_word = str(input("Хотите отгадать слово целиком?"))
        if guess_word.lower() == word:
            print("Вы угадали слово!")
            break
        count -= 1
    if count == 0:
        print("Попытки закончились.")
input("\nНажмите Enter, чтобы выйти.")
