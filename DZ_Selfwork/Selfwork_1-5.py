# Lesson 3  ==========================================
# Задание один  ==========================================

import random


def error(c=random.randint(0, 2)):
    if c == 0:
        raise RuntimeError('New runtime error')
    elif c == 1:
        raise ValueError('New Value error')
    elif c == 2:
        raise TypeError('New Type error')


try:
    error()
except ValueError:
    print('Обработано ValueError')
except TypeError:
    print('Обработано TypeError')
except RuntimeError:
    print('Обработано RuntimeError')

# Lesson 4  ==========================================
# Задание один  ==========================================

# Игра Угадай число
import random

target_num = random.randint(1, 100)


def check(users_input):
    if users_input < target_num:
        print('Задуманное число большое указанного вами', target_num)
        work = True
    if users_input > target_num:
        print('Задуманное число меньше указанного вами', target_num)
        work = True
    if users_input == target_num:
        print('Угадали')
        work = False
    return work


def main():
    start = False
    work = True
    while True:
        if start == False:
            users_input = int(input('Введите число от 1 до 100: '))
            work = check(users_input)
            if work == True:
                start = True
            else:
                break
        else:
            users_input = int(input('Попробуйте еще раз: '))
            work = check(users_input)
            if work == True:
                start = True
            else:
                break


main()