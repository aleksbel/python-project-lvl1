import prompt


def run(game_name):
    greet(game_name)
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print('\n')
    engine(game_name, user_name)


def greet(game_name):
    print('Welcome to the Brain Games!')
    print(game_name.GAME_TOPIC)
    print('\n')


def engine(game_name, user_name):
    for i in range(3):
        # Get the question and the correct answer from the game module
        expression_txt, answer_correct = game_name.game_function()
        # We formulate a question and get an answer
        # answer_txt - to do  next line shorter
        answer_txt = '\nYour answer: '
        answer = prompt.string('Question: ' + expression_txt + answer_txt)
        # The first/second answer is correct
        if i < 2 and str(answer) == str(answer_correct):
            print('Correct!')
            continue
        # All answers are correct
        elif i == 2 and str(answer) == str(answer_correct):
            print('Correct!')
            print("Congratulations, {}!".format(user_name))
            break
        # Answer is incorrect
        else:
            var_t = ' is wrong answer ;(. Correct answer was '
            print("'{}'{}'{}'".format(answer, var_t, answer_correct))
            print("Let's try again, {}!".format(user_name))
            break
