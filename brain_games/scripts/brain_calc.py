from brain_games import engine
from brain_games.games import brain_calc

def main():
    engine.run_game(brain_calc.generate_round, brain_calc.DESCRIPTION) 

if __name__ == '__main__':
    main()

    