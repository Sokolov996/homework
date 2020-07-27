profit = float(input("Введите выручку фирмы"))
costs = float(input("Введите издержки фирмы"))
if profit > costs:
    print(f"Чистая прибыль составила {profit - costs:.2f}")
    workers = int(input("Введите количество сотрудников в фирме "))
    print(f"Прибыль в расчете на одного сотрудника составялет {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")