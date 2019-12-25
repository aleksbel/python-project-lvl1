from random import randrange


GAME_TOPIC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def new_round():
    # Odd numbers only
    x = randrange(1, 1000, 2)
    # Correct answer
    if is_prime(x):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    # We formulate a question
    expression = str(x)
    return expression, correct_answer
