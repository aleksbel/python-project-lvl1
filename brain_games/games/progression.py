from random import randint


GAME_TOPIC = 'What number is missing in the progression?'


def game_function():
    # Step progression
    step_pr = randint(1, 10)
    # Build a progression with the selected step
    list_pr = list(range(1, step_pr * 10, step_pr))
    # determine the item number to replace
    number_element = randint(0, 9)
    # Correct answer
    answer_correct = list_pr[number_element]
    # Replace the number with points
    list_pr[number_element] = '..'
    # Convert to string
    list_pr = str(list_pr)
    # Remove extra characters
    list_pr = list_pr.replace(',', '')
    list_pr = list_pr.replace("'..'", '..')
    list_pr = list_pr.replace('[', '')
    list_pr = list_pr.replace(']', '')
    #  We formulate a question
    expression_txt = list_pr
    return expression_txt, answer_correct
