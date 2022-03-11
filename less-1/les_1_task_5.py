# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

a_int = int(input("Введите номер букву в алфавите >>> "))
letters = "abcdefghijklmnopqrstuvwxyz"

print(f"{a_int} = {letters[a_int-1]}")