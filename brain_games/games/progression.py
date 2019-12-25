from random import randint


GAME_TOPIC = 'What number is missing in the progression?'


def new_round():
    progression_element = 1
    progression = ''
    # Step progression
    step = randint(1, 10)
    # determine the item number to replace
    element_index = randint(0, 9)
    # Build a progression with the selected step
    for i in range(10):
        # Replace the number with points
        if i == element_index:
            correct_answer = str(progression_element)
            progression += '..' + ' '
        else:
            progression += str(progression_element) + ' '
        progression_element += step
    expression = progression
    return expression, correct_answer
