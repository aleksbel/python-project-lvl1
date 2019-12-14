from random import randint
from brain_games.game_common import game_common

# Общее приветствие и вывод на экран - что, собственно, надо делать в игре


def greet():
    print('Welcome to the Brain Games!')
    print('nswer "yes" if given number is prime. Otherwise answer "no".')
    print('\n')


def prime_game():
    # Проверка, просте ли число
    def IsPrime(n):
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    for i in range(3):
        x = randint(1, 1000)
        # Создаем переменную с правильным ответом
        if IsPrime(x):
            answer_correct = 'yes'
        else:
            answer_correct = 'no'
        # print(answer_correct)
        # Формируем строку задачи x y
        expression_txt = str(x)
        # Далее неизменяемый код
        what_to_do = game_common(i, answer_correct, expression_txt)
        if what_to_do == 'continue':
            continue
        elif what_to_do == 'break':
            break
