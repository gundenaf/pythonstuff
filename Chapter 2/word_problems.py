# Текстовые задачи
# Демонстрирует математические операции
print("""Ecли беременная самка бегемота массой 800 кг родит детеныша массой 40 кг,
нo затем съест 20 кг корма, то сколько она будет после всего этого весить?""")
hippo = 800 - 40 + 20
input("Чтобы узнать, нажмите Enter.")
print("800 - 40 + 20: " + str(hippo))

print("""Ecли студент, возвращаясь с успешно сданного экзамена, на радостях
купил каждому из 6 друзей по 3 бутылки пива, то сколько всего бутылок пива
куплено?""")
beer = 6 * 3
input("Чтобы узнать, нажмите Enter.")
print("6 * 3: " + str(beer))

print("""Ecли в ресторане вам с приятелями принесли счёт на 19 долларов (считая чаевые),
и вы решили скинуться поровну на четверых, то сколько придётся с каждого?""")
restaraunt = 19 / 4
input("Чтобы узнать, нажмите Enter.")
print("19 / 4: " + str(restaraunt))

print("""Ecли четверо пиратов найдут ларчик, в котором ровно 107 золотых монет, и
решат разделить добычу поровну на четверых, то сколько придётся с каждого?""")
capture = 107 // 4
input("Чтобы узнать, нажмите Enter.")
print("107 // 4: " + str(capture))

print("""Ecли те же самые четверо пиратов разделят те же 10 монет из ларчика поровну,
то сколько останется ничейных монет?""")
capture_double = 107 % 4
input("Чтобы узнать, нажмите Enter.")
print("107 % 4: " + str(capture_double))

input("\n\nНажмите Enter, чтобы выйти")

