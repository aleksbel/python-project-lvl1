from random import randint
from random import choice
from operator import add, mul, sub


GAME_TOPIC = 'What is the result of the expression?'


def new_round():
    x = randint(1, 100)
    y = randint(1, 100)
    # Select the type of arithmetic operation
    options_operation = {
        '+': add(x, y),
        '-': sub(x, y),
        '*': mul(x, y)
        }
    operand = choice(list(options_operation.keys()))
    # Correct answer
    correct_answer = str(options_operation[operand])
    # We formulate a question x (+ - *) y
    expression = "{} {} {}".format(str(x), operand, str(y))
    return expression, correct_answer
