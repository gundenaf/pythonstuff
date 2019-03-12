#   Пароль - воспроизведение входа в компьютерную систему

print("""Добро пожаловать к нам в System Security Inc.
-- Security (Безопасность) - наше второе имя""")

password: str = ("secret")
if str(input("Введите пароль: ")) == password:
    print("Доступ открыт")
else:
    print("Доступ запрещен")
input("\n\nHaжмитe Enter. чтобы выйти.")