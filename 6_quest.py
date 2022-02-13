'''
Задача 6
Найти сумму цифр числа.
'''
integer_number = input("Пожалуйста, введите число: ")
sum = 0

for i in range(len(integer_number)):
    if not integer_number[i].isdigit(): # Пропуск точки в нецелых числах
        continue
    sum += int(integer_number[i])
print('Сумма цифр в числе', integer_number, 'равна:', sum)