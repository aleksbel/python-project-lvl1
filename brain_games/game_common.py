import prompt


# Запрос имени и персональное приветствие
def run():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('\n')
    return name


def game_common(i, answer_correct, expression_txt):
    answer = prompt.string('Question: ' + expression_txt + '\nYour answer: ')
    # Разбираемся с ответом
    # Если ответ правильный: идем на новую итерацию
    if i < 2 and str(answer) == str(answer_correct):
        print('Correct!')
        return 'continue'
        # Если все три ответа правильные - прекращаем работу программы
    elif i == 2 and str(answer) == str(answer_correct):
        print('Correct!')
        print("Congratulations, {}!".format(name))
        return 'break'
    # Если ответ НЕ правильный, пробел или произвольные символы
    else:
        var_t = ' is wrong answer ;(. Correct answer was '
        print("'{}'{}'{}'".format(answer, var_t, answer_correct))
        print("Let's try again, {}!".format(name))
        return 'break'
