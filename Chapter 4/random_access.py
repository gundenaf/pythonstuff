#   Случайные буква
#   Демонстрирует работу строк

import random
word = "индекс"
print("В переменной word хранится слово: ", word, "\n")
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])
input("\n\nНажмите Enter, чтобы выйти.\n")
