n = int(input("Введите целое число"))
max = 0
while n>0:
    c=n%10
    if c >=max: max = c
    n //=10
print(max)
