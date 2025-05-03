from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import brain_even
from brain_games.scripts.brain_calc import brain_calc
from brain_games.scripts.brain_gcd import brain_gcd
from brain_games.scripts.brain_progression import brain_progression
from brain_games.scripts.brain_prime import brain_prime

def main():
    welcome_user()
    brain_even(name)
    brain_calc(name)
    brain_progression(name)
    brain_prime(name)

if __name__ == '__main__':
    main()