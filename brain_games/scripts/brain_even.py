from brain_games.engine import game_engine
from brain_games.games.game_even import (
    game_rules, game
)
#все относительный пути заменить на абсолютные


def main():
    game_engine(game, game_rules)



if __name__ == "__main__":
    main()







