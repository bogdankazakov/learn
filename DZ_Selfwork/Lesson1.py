# Lesson 1   ==========================================
# Задание один   ==========================================
# Программа спрашивает текущий месяц и проверяет правильность ответа. Ответ не чувствителен в регистру.
# Вопрос - если делать на русском, то код возвращает на октябрЬ, а октябрЯ - как это можно исправить?

import datetime

d = datetime.date.today()
month = d.strftime('%B').lower()
print(month)

while True:
    users_input = str(input('What is the current month? '))

    if users_input.lower() == str(month):
        print('Ok')
        break
    else:
        print('Error')
        continue


# Lesson 1  ==========================================
# Задание два  ==========================================
# Вопрос - вижу что есть недоработка в том, что после ввода символа появлется промежуточная сумма, что не соот-ет заданию. Но как исправить пока не понимаю.

# проверяльщик типа значения
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


operation = 1
sum = 0

while True:
    users_input = input('Введите действие или число: ')

    if users_input == '':
        print('Итоговый результат: ', sum)
        break
    else:
        if isfloat(users_input):
            try:
                if operation == 1:
                    sum = old + float(users_input)
                    old = sum
                    print(sum)
                elif operation == 2:
                    sum = old - float(users_input)
                    old = sum
                    print(sum)
                elif operation == 3:
                    sum = old * float(users_input)
                    old = sum
                    print(sum)
                elif operation == 4:
                    sum = old / float(users_input)
                    old = sum
                    print(sum)
                continue
            except:
                old = 0
                if operation == 1:
                    sum = old + float(users_input)
                    old = sum
                    print(sum)
                elif operation == 2:
                    sum = old - float(users_input)
                    old = sum
                    print(sum)
                elif operation == 3:
                    sum = old * float(users_input)
                    old = sum
                    print(sum)
                elif operation == 4:
                    sum = old / float(users_input)
                    old = sum
                    print(sum)
                continue
        else:
            try:
                old
                if str(users_input) == '+':
                    operation = 1
                elif str(users_input) == '-':
                    operation = 2
                elif str(users_input) == '*':
                    operation = 3
                elif str(users_input) == '/':
                    operation = 4
                else:
                    print('Только дейстие или число!')
            except NameError:
                print('Сначала введите число')
