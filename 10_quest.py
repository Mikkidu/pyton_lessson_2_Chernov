'''
Задача 10
Найти количество цифр 5 в числе
'''

integer_number = input("Пожалуйста, введите число: ")
five_count = 0
for i in integer_number:
    if i == '5':
        five_count += 1
print('Количество цифр 5 в вашем числе равно:', five_count)