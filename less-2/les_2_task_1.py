# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    a = int(input("Введите число a >>> "))
    b = int(input("Введите число b >>> "))
    c = input("Введите знак операции >>> ")

    if c == "-":
        print(f"a - b = {a - b}")

    elif c == "*":
        print(f"a * b = {a * b}")

    elif c == "/":
        print(f"a / b = {a / b}")

    elif c == "+":
        print(f"a + b = {a + b}")

    elif c == "0":
        print("Конец")
        break
    else:
        print("Ошибка ввода знака")