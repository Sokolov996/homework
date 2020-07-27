a = int(input("Ваш результат в км?"))
b = int(input("Ваш желаемый результат?"))
days = 1
km = a
while km < b:
    a = a + 0.1 * a
    days += 1
    km = km + a
print(f"Вы достигните желаемого результата на %.d день" %days)