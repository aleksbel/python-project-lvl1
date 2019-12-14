# Импорт функций из общего файла
from brain_games.game_common import run

# Импорт функций из файла конкретной игры
from brain_games.games.prime_game import greet
from brain_games.games.prime_game import prime_game


def main():
    greet()
    run()
    prime_game()


if __name__ == '__main__':
    main()
