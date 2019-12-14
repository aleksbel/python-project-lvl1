# Импорт функций из общего файла
from brain_games.game_common import run

# Импорт функций из файла конкретной игры
from brain_games.games.progression_game import greet
from brain_games.games.progression_game import progression_game


def main():
    greet()
    run()
    progression_game()


if __name__ == '__main__':
    main()
