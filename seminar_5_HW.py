# Задача 26:  Напишите программу, которая на вход
# принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# Пример: A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def grade(number, gradeNumber):
    if (gradeNumber == 1):
        return number
    if (gradeNumber != 1):
        return (number * grade(number, gradeNumber-1))
    
number = int(input("Введите число для возведения в степень: "))
gradeNumber = int(input("Введите степень возведения числа: "))

print("Результат: ", grade(number, gradeNumber))


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Пример:
# 2 2
#     4 

print()
def sumNumbers(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sumNumbers(a, b)
    else:
        return a

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(sumNumbers(a, b))