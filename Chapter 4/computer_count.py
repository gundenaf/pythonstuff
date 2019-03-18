#   Счёт по просьбе пользователя

first = int(input('Введите начало счёта: '))
last = int(input('Введите конец счёта: '))
gap = int(input('Введите интервал: '))
for i in range(first, last+1, gap):
    print(i, end=' ')
input("\nНажмите Enter, чтобы выйти.")
