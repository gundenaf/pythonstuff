#   Зверюшка с аттрибутом
#   Демонстрирует создание атрибутов объекта и доступ к ним

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep
    def talk(self):
        print("Привет. Меня зовут", self.name, "\n")

crit1 = Critter("Бобик")
crit1.talk()
crit2 = Critter("Мурзик")
crit2.talk()
print("Вывод объекта crit1 на экран:", crit1)
print("Непосредственный доступ к атрибуту crit1.name:", crit1.name)
input("\nНажмите Enter, чтобы выйти.")
