#   Компьютер попробует угадать число
count = 0
num1, num2 = 1, 100
enter = 0
while enter != 'y':
    count += 1
    number = round((num1 + num2) / 2)
    print(number)
    enter = input("Угадал 'y', больше '>' ,меньше '<': ")

    if enter == '<':
        num2 = number
    elif enter == '>':
        num1 = number

print('\n\nТак просто... Всего ' + str(count) + ' попыток :))))\n\n' \
      + '\t\t' + str(number))
input("\n\nHaжмитe Enter. чтобы выйти.")
