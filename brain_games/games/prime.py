from random import randrange


GAME_TOPIC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_function():
    def inner_IsPrime(n):
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    x = randrange(1, 1000, 2)
    # Correct answer
    if inner_IsPrime(x):
        answer_correct = 'yes'
    else:
        answer_correct = 'no'
    # We formulate a question
    expression_txt = str(x)
    return expression_txt, answer_correct
