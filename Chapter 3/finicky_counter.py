#   Привередливая система
#   Демонстрирует работу команд break и continue

count = 0
while True:
    count += 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)
input("\n\nHaжмитe Enter. чтобы выйти.")
