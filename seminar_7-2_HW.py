# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.
# Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

print("Вычисление элемента по номеру строки и столбца")

def printOperationTable(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows+1):
        for column in range(1, num_columns+1):
            print(operation(row,column), end='\t')
        print()

printOperationTable(lambda x,y: x+y, 3, 5)
print("\n")
printOperationTable(lambda x,y: x-y, 5, 5)
print("\n")
printOperationTable(lambda x,y: x*y, 4, 4)