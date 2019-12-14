# Импорт функций из общего файла
from brain_games.game_common import run

# Импорт функций из файла конкретной игры
from brain_games.games.gcd_game import greet
from brain_games.games.gcd_game import gcd_game


def main():
    greet()
    run()
    gcd_game()


if __name__ == '__main__':
    main()
