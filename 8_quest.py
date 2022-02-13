'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = input("Пожалуйста, введите число: ")
answer = "В вашем числе встречается цифра 5."
if '5' in integer_number:
    print(answer)
else:
    print(answer[:13]+" не"+answer[13:])
