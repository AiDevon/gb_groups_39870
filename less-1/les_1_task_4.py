# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

a_str = str.lower(input("Введите первую букву >>> "))
b_str = str.lower(input("Введите вторую букву >>> "))
letters = "abcdefghijklmnopqrstuvwxyz"
a_index = letters.find(a_str) + 1
b_index = letters.find(b_str) + 1
len_a_b = len(letters[a_index:b_index-1])

print(f"Первая буква рассположена на {a_index} месте алфавита")
print(f"Вторая буква рассположена на {b_index} месте алфавита")
print(f"Между первой и второй буквы находится {len_a_b} букв")