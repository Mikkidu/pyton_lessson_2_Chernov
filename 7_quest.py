'''
Задача 7
Найти произведение цифр числа.
'''
integer_number = input("Пожалуйста, введите число: ")
mult = 1

for i in range(len(integer_number)):
    if not integer_number[i].isdigit(): # Пропуск точки в нецелых числах или пробелов
        continue
    mult *= int(integer_number[i])
print('Произведение цифр в числе', integer_number, 'равно:', mult)