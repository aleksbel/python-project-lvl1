from random import randint


GAME_TOPIC = 'Answer "yes" if number even otherwise answer "no"'


def game_function():
    random_number = randint(1, 100)
    # Correct answer
    if random_number % 2 == 0:
        answer_correct = 'yes'
    else:
        answer_correct = 'no'
    # We formulate a question
    expression_txt = str(random_number)
    return expression_txt, answer_correct
