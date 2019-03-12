#   Автодилер - ввод стоимости автомобиля без наценок

car_price = float(input("Введите стоимость автомобиля без наценок: "))
taxes: float = car_price / 5.0
filing_fee: float = car_price / 10.0
agent_fee: float = 50.0
delivery_cost: float = 150.0
print("Окончательная цена автомобиля:", car_price + taxes + filing_fee + agent_fee + delivery_cost)

