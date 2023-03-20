# Задача 38: Дополнить телефонный справочник возможностью
# изменения и удаления данных. Пользователь также может
# ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных

# ЭТАП 1 - СОЗДАНИЕ ТЕЛЕФОННОЙ КНИГИ
# phonebook = []
# data = open('PhoneBook.txt', 'a', encoding='utf-8')
# data.writelines(phonebook)
# data.close


# ЭТАП 2 - ЗАПОЛНЕНИЕ ТЕЛЕФОННОЙ КНИГИ
# with open ('PhoneBook.txt', 'w', encoding='utf-8') as phoneBook:
#     line1 = "Иванов, Иван, 111, описание для Ивана \n"
#     line2 = "Петров, Пётр, 222, описание для Петра \n"
#     line3 = "Василисова, Василиса, 333, описание для Василисы \n"
#     line4 = "Питонов, Питон, 777, описание для Питона \n"
#     phoneBook.writelines([line1, line2, line3, line4])

# ЭТАП 3 - УДАЛЕНИЕ СТРОКИ ДАННЫХ ИЗ ТЕЛЕФОННОЙ КНИГИ
# with open('PhoneBook.txt', 'r',  encoding='utf-8') as phoneBook:
#     lines = phoneBook.readlines()
# del lines[1]
# with open('PhoneBook.txt', 'w', encoding='utf-8') as phoneBook:
#     phoneBook.writelines(lines)

# ЭТАП 4 - ЗАМЕНА ДАННЫХ В ТЕЛЕФОННОЙ КНИГЕ
with open('PhoneBook.txt', 'r',  encoding='utf-8') as phoneBook:
    print(phoneBook.readlines())
