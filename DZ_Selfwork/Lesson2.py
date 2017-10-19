# Lesson 2  ==========================================
# Задание один  ==========================================
# Программа генерит случайный вопрос. Проверяет ответ. Нажание на Enter завершает работу.

qa = {'сумма 2 и 3 ': '5', 'разница 5 и 3 ': '2', 'как меня зовут ': 'Богдан'}
l = list()
for i in qa.keys():
    l = l + [i, ]

import random

while True:
    r = random.randint(0, 2)
    q = l[r]
    users_input = input(q)

    if users_input == '':
        print('Всего хорошего!')
        break
    elif users_input == qa[q]:
        print('Ok')
        continue
    else:
        print('Error')
        continue

# Lesson 2  ==========================================
# Задание два  ==========================================

# Начало

txt = 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?  '

# выводим без знаков

znaki = ['.', ',', '!', '?', ':', ';', '-']
new_txt = ''

for symb in txt:
    if symb not in znaki:
        new_txt += str(symb)

print(new_txt)

# делим на слова и считаем

words = tuple(txt.split())
counter = dict()

for word in words:
    if counter.get(word):
        counter[word] += 1
    else:
        counter[word] = 1

# ищем и выводи TOP10
comparisonlist = list(counter.values())
m = max(comparisonlist)
comparisonlist.sort(reverse=True)
top10 = comparisonlist[0:10]
top = list()

i = 0
ll = 9
while i < ll:
    for w, q in counter.items():
        if q == top10[i]:
            counter[w] = "used"
            top += (w, q)
            if i < ll:
                i += 1
            else:
                break

print('вывод top10 и количества повторений: ', top)