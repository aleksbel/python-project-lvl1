from random import randint
from random import choice
from brain_games.game_common import game_common

# Общее приветствие и вывод на экран - что, собственно, надо делать в игре


def greet():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    print('\n')


def calculator():
    for i in range(3):
        x = randint(1, 100)
        y = randint(1, 100)
        # Выбираем рандомно тип операции
        list_operation = ['x + y', 'x - y', 'x * y']
        expression = choice(list_operation)
        # Создаем переменную с правильным ответом
        answer_correct = eval(expression)
        # Формируем строку задачи x (+ - *) y
        expression_txt = str(x) + ' ' + str.split(expression)[1] + ' ' + str(y)
        what_to_do = game_common(i, answer_correct, expression_txt)
        if what_to_do == 'continue':
            continue
        elif what_to_do == 'break':
            break
