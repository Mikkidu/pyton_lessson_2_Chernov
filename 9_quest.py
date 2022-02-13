'''
Задача 9
Найти максимальную цифру в числе
'''

integer_number = input("Пожалуйста, введите число: ")
max_number = 0
for i in integer_number:
    if int(i) > max_number:
        max_number = int(i)
print('Наибольшая цифра в вашем числе:', max_number)
