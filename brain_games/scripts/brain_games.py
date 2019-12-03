from brain_games.cli import run

def greet():
    print('Welcome to the Brain Games!')

def main():
    greet()
    run('May I have your name? ')

if __name__ == '__main__':
    main()
