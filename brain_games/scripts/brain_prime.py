from brain_games import engine
from brain_games.games import brain_prime

def main():
    engine.run_game(brain_prime.generate_round, brain_prime.DESCRIPTION) 

if __name__ == '__main__':
    main()