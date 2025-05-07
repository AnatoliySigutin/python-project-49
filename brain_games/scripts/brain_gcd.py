from brain_games import engine
from brain_games.games import brain_gcd


def main():
    engine.run_game(brain_gcd.generate_round, brain_gcd.DESCRIPTION) 


if __name__ == '__main__':
    main()
    