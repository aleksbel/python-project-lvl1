from random import randint
from random import choice


GAME_TOPIC = 'What is the result of the expression?'


def game_function():
    x = randint(1, 100)
    y = randint(1, 100)
    # Select the type of arithmetic operation
    list_operation = ['x + y', 'x - y', 'x * y']
    expression = choice(list_operation)
    # Correct answer
    answer_correct = eval(expression)
    # We formulate a question x (+ - *) y
    expression_txt = str(x) + ' ' + str.split(expression)[1] + ' ' + str(y)
    return expression_txt, answer_correct
