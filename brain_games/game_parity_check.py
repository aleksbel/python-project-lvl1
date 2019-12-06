from random import randint
import prompt


def greet():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n\n')


def run():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n\n'.format(name))
    return name


def game_parity_check(name_of_run):
    # Если пользователь сразу Enter, вопрос повторяется с тем же числом
    name = name_of_run
    for i in range(3):
        # Задаем разные переменные для удобства
        random_number = randint(1, 100)
        answer_correct = 'Correct!'
        parity_of_number = random_number % 2
        # Задаем число и получаем ответ, четное или нет
        # qn - чтобы сделать < 79 символов в след. строке
        qn = 'Question: '
        answer = prompt.string(qn + str(random_number) + '\nYour answer:')
        # Правильные ответы
        if answer == 'yes' and parity_of_number == 0:
            print(answer_correct)
            continue
        elif answer == 'no' and parity_of_number != 0:
            print(answer_correct)
            continue
        # неправильные ответы, пробел или произвольные символы
        else:
            # неправильные ответы
            if answer == 'yes' and parity_of_number != 0:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            elif answer == 'no' and parity_of_number == 0:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            else:
                # var_answer - чтобы сделать < 79 символов в строке print
                var_answer1 = "It is wrong answer ;(. "
                var_answer2 = "Correct answer was 'yes' or 'no'."
                print(var_answer1 + var_answer2)
            print("Let's try again, {}!".format(name))
            break
    else:
        print("Congratulations, {}!".format(name))
