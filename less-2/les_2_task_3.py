# Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

a = input("Введите число a >>> ")
i = len(a) - 1
rev_a = ""
while i >= 0:
    rev_a += a[i]
    i -= 1

print(rev_a)