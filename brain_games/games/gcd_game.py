from random import randint
from math import gcd
from brain_games.game_common import game_common

# Общее приветствие и вывод на экран - что, собственно, надо делать в игре


def greet():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    print('\n')


def gcd_game():
    for i in range(3):
        x = randint(1, 100)
        y = randint(1, 100)
        # Создаем переменную с правильным ответом
        answer_correct = gcd(x, y)
        #print(answer_correct)
        # Формируем строку задачи x y
        expression_txt = str(x) + ' ' + str(y)
        # Далее неизменяемый код
        what_to_do = game_common(i, answer_correct, expression_txt)
        if what_to_do == 'continue':
            continue
        elif what_to_do == 'break':
            break
