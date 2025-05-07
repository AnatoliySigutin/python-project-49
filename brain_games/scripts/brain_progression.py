from brain_games import engine
from brain_games.games import brain_progression


def main():
    engine.run_game(brain_progression.generate_round, brain_progression.DESCRIPTION) 

if __name__ == '__main__':
    main()