from random import randint


GAME_TOPIC = 'Answer "yes" if number even otherwise answer "no"'


def new_round():
    random_number = randint(1, 100)
    # Correct answer
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    # We formulate a question
    expression = str(random_number)
    return expression, correct_answer
