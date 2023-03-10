# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые
# встречаются в обоих наборах.

# Пользователь вводит 2 числа.
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

print('Введите количество элементов первого множества n: ')
n = int(input())
print('\n')

print('Введите количество элементов второго множества m: ')
m = int(input())
print('\n')

print('Введите', n,'чисел первого множества через пробел: ')
collectOne = set(map(int, input().split()))
print(collectOne, '\n')

print('Введите', m, 'чисел второго множества через пробел: ')
collectTwo = set(map(int, input().split()))
print(collectTwo, '\n')

repeatColl = collectOne.intersection(collectTwo)
print('Значения, которые встречаются в обоих множествах: ')
print(repeatColl)



# Задача 24: В фермерском хозяйстве в Карелии
# выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности.
# 
# Таким образом, у каждого куста есть ровно
# два соседних.
# 
# Всего на грядке растет N кустов.
# 
# Эти кусты обладают разной урожайностью, поэтому
# ко времени сбора на них выросло различное
# число ягод – на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система
# автоматического сбора черники. Эта система
# состоит из управляющего модуля и нескольких
# собирающих модулей.
# 
# Собирающий модуль за один # заход, находясь
# непосредственно перед некоторым # кустом,
# собирает ягоды с этого куста и с двух # соседних с ним.
# 
# Напишите программу для нахождения максимального
# числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым
# кустом заданной во входном файле грядки.

print('\n')
print('Введите число кустов: ')
n = int(input()) # ввод количества кустов

arr = list() # создание множества для количества ягод на кустах

print('Введите количество ягод на каждом из', n, 'кустов: ')
for i in range(n):  # заполнение множества
    x = int(input())
    arr.append(x)

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])

print('Максимально за один заход можно собрать ягод: ')
print(max(arr_count))