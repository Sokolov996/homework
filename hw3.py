print("Сложение по формуле 'n+nn+nnn' ")
n = int(input("Введите любую цифру"))
answer = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(answer)