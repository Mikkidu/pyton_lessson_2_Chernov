'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
mult = 1

for i in range(2,11):
    mult*=i
print("10! =", mult)