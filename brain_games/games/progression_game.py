from random import randint
from brain_games.game_common import game_common

# Общее приветствие и вывод на экран - что, собственно, надо делать в игре


def greet():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    print('\n')


def progression_game():
    for i in range(3):
        step_pr = randint(1, 10)
        list_pr = list(range(1, step_pr * 10, step_pr))
        # определяем номер элемента для замены
        number_element = randint(0, 9)
        # Создаем переменную с правильным ответом
        answer_correct = list_pr[number_element]
        # Заменяем на точки
        list_pr[number_element] = '..'
        # Преобразуем в строку и убираем лишние символы
        list_pr = str(list_pr)
        list_pr = list_pr.replace(',', '')
        list_pr = list_pr.replace("'..'", '..')
        list_pr = list_pr.replace('[', '')
        list_pr = list_pr.replace(']', '')
        # Формируем строку задачи x y
        expression_txt = list_pr
        # Далее неизменяемый код
        what_to_do = game_common(i, answer_correct, expression_txt)
        if what_to_do == 'continue':
            continue
        elif what_to_do == 'break':
            break
