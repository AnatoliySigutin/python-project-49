from brain_games import engine
from brain_games.games import brain_even

def main():
    engine.run_game(brain_even.generate_round, brain_even.DESCRIPTION) 

if __name__ == '__main__':
    main()