import prompt


def run(game_module):
    greet(game_module)
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print()
    engine(game_module, user_name)


def greet(game_module):
    print('Welcome to the Brain Games!')
    print(game_module.GAME_TOPIC)
    print()


def engine(game_module, user_name, num_rounds=3):
    for i in range(num_rounds):
        # Get the question and the correct answer from the game module
        expression, correct_answer = game_module.new_round()
        # We formulate a question and get an answer
        print('Question: ' + expression)
        answer = prompt.string('Your answer: ')
        # Answer is correct
        if answer == correct_answer:
            print('Correct!')
            # All answers are correct
            if i == num_rounds - 1:
                print("Congratulations, {}!".format(user_name))
                break
            continue
        # Answer is incorrect
        else:
            var_t = ' is wrong answer ;(. Correct answer was '
            print("'{}'{}'{}'".format(answer, var_t, correct_answer))
            print("Let's try again, {}!".format(user_name))
            break
