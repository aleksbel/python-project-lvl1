from random import randint
from math import gcd


GAME_TOPIC = 'Find the greatest common divisor of given numbers.'


def game_function():
    x = randint(1, 100)
    y = randint(1, 10)
    # Correct answer
    answer_correct = gcd(x, y)
    # We formulate a question
    expression_txt = str(x) + ' ' + str(y)
    return expression_txt, answer_correct
