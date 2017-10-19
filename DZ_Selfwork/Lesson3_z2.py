# Lesson 3  ==========================================
# Задание два: поле чудес  ===================

# Вводим значение
word=('Funny').lower()

# Формируем 2 списка
list_word=[]
for item in word:
    list_word.append(item)
print (list_word)

list_word2=[]
for item in word:
    list_word2.append(item)
print (list_word2)


list_print=[]
for item in word:
    list_print.append('_ ')
print (list_print)


# Функция формирует выводимое сообщение
def printer(i, item):
    a=0
    for letter in list_print:
        if a==i:
            list_print[a] = item
        a += 1
    return list_print

# Начинаем игру


print('Начнем игру: ', list_print)
remember = list()
while len(list_word2)!=0:
    users_input = str(input ('Введите букву: ').lower())
    i=0

    if users_input in remember and users_input not in list_word:
        print ('Вы ее уже называли. Такой буквы нет в слове или УЖК нет ;)! ')
    else:
        if users_input in list_word:
            for item in list_word:
                if users_input == item:
                    list_word[i] = None
                    del list_word2 [0]
                    print(printer(i, item))
                    break
                i += 1
        else:
            print('Такой буквы в слове нет! ')
        remember.append(users_input)

print('Победа')




