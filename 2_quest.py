'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

print("Введите 10 цифр")
kol = 0
for i in range(10):
    number = 0
    while True:
        number = input(str(i+1) + "-я: ")
        if not number.isdigit(): #проверка на целое число
            print('Введена не цифра, попробуйте ещё раз')
            continue
        if 0 <= int(number) < 10: #проверка на цифры. Не придумал ничего изящного)
            break
        print('Введена не цифра, попробуйте ещё раз')
    if number == "5":
        kol +=1
print("Количество введённых цифр 5: ", kol)
