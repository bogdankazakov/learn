# Вввод количества дисков
user_input=int(input('Введите количество дисков: '))
print('колчичество дисков: ', user_input)
#Создаем стэки:


stack1 = list(range(user_input))
stack1.reverse()
stack2 =[]
stack3 =[]

master_stack = [stack1, stack2, stack3]
print ('master_stack', master_stack)

def move (f,t):
    try:
        t.append(f.pop(-1))
        print(master_stack)
    except IndexError:
        return False

def check (f,t):
    try:
        if t==list() and f != list() or t[0]>=f[0] :
            return True
        else:
            return False
    except IndexError:
        return False

def stack1_checker ():
    if check(stack1, stack2):
        return move(stack1, stack2)
    else:
        if check(stack1, stack3):
            return move(stack1, stack3)
        else:
            return False


def stack2_checker ():
    if check(stack2, stack3):
        return move(stack2, stack3)
    else:
        if check(stack2, stack1):
            return move(stack2, stack1)
        else:
            return False

def stack3_checker():
    if check(stack3, stack2):
        return move(stack3, stack2)
    else:
        if check(stack3, stack1):
            return move(stack3, stack1)
        else:
            return False


def chain_checker21():
    while True:
        return stack2_checker()
    else:
        return stack1_checker()


while True:
    stack1_checker()
else:
    print('ds')
    stack2_checker()







'''
    if
                        stack1!=list() and stack2!=list():
    print('sdsdfs')
    while True:
        while True:
            stack1_checker()
        else:
            chain_checker21()
    else:
        stack3_checker()
'''

