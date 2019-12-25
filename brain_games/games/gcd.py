from random import randint


GAME_TOPIC = 'Find the greatest common divisor of given numbers.'


def training_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def new_round():
    x = randint(1, 100)
    y = randint(1, 10)
    # Correct answer
    correct_answer = str(training_gcd(x, y))
    # We formulate a question
    expression = str(x) + ' ' + str(y)
    return expression, correct_answer
