# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Введите чтсло a = "))
b = int(input("Введите чтсло b = "))
c = int(input("Введите чтсло c = "))

if c > a > b or b > a > c:
    print(f"Среднее число a = {a}")
elif c > b > a or a > b > c:
    print(f"Среднее число b = {b}")
else:
    print(f"Среднее число c = {c}")