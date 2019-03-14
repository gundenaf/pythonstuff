#   "Орёл и решка!"
import random

count = 1
heads = 0
tails = 0
while count <= 100:
    coin: int = random.randint(0, 1)
    if coin == 0:
        heads += 1
    elif coin == 1:
        tails += 1
    count += 1
print("Монету подбросили 100 раз!")
print("Орлов выпало: %d раз" % heads)
print("Решек выпало: %d раз" % tails)
input("\n\nHaжмитe Enter. чтобы выйти.")


