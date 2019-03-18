#   Текст наоборот

user_text = str(input("Введите какой-либо текст: "))
while user_text:
    print(user_text[len(user_text) - 1], end='')
    user_text = user_text[:(len(user_text) - 1)]

input("\nНажмите Enter, чтобы выйти.")
