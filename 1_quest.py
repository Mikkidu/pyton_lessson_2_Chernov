'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
zero = "000000"
i = 0
while i < 5:
    i += 1
    print(i, zero, sep=". ")
