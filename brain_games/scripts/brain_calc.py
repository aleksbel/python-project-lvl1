# Импорт функций из общего файла
from brain_games.game_common import run

# Импорт функций из файла конкретной игры
from brain_games.games.calculator import greet
from brain_games.games.calculator import calculator


def main():
    greet()
    run()
    calculator()


if __name__ == '__main__':
    main()
