#   Эксклюзивная сеть
#   Демонстрирует составные условия и логические операторы

print("\t\tЭксклюзивная компьютерная сеть")
print("\t\tТолько для зарегистрированных пользователей!\n")
security: int = 0
username: str = ""
while not username:
    username = str(input("Логин: "))
password: str = ""
while not password:
    password = str(input("Пароль: "))
if username == "M.Dawson" and password == "secret":
    print("Привет, Майк.")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Здравствуй, Сид.")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("Доброго времени суток, Сигеру.")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("Как дела, Уилл?")
    security = 3
elif username == "guest" and password == "guest":
    print("Добро пожаловать к нам в гости.")
    security = 1
else:
    print("Войти в систему не удалось. Должно быть, вы не очень-то эксклюзивный гражданин.\n")

input("\n\nHaжмитe Enter. чтобы выйти.")
