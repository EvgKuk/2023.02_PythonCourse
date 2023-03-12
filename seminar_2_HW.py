# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой,
# а некоторые – гербом.
# Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все
# монетки были повернуты вверх одной и
# той же стороной.
# Выведите минимальное количество монет,
# которые нужно перевернуть

print()
print('введите число монет лежащих гербом вверх: ')
g = int(input())
print('введите число монет лежащих решкой вверх: ')
r = int(input())
sum = g + r
if 0 < sum:
    if g > r:
        print('минимально перевернуть монет:', r, end='\n')
    elif r > g:
        print('минимально перевренуть монет:', g, end='\n')
print()

# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает
# две подсказки. Он называет сумму этих чисел S и 
# их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print()
print('введите сумму чисел: ')
sum = int(input())
print('введите произведение чисел: ')
mult = int(input())

for x in range(1, 1001):
    for y in range (1, 1001):
        if x + y == sum and x * y == mult:
            print('Возможная комбинация: ')
            print('Загаданное число X: ', x)
            print('Загаданное число Y: ', y)

# Задача 14: Требуется вывести все целые степени
# двойки (т.е. числа вида 2k), не превосходящие числа N.
print()
print('введите целое число N: ')
n = int(input())
k = 1
while k < n:
    print(k, end='\n')
    k = 2 * k