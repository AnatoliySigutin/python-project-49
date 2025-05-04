from random import randint

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    division_counter = 0
    prime_counter = 0
    max_counter = 3

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while prime_counter < max_counter:
        number = randint(1, 100)
        print(f'Question: {number}')

        answer = prompt.string('Your answer: ').lower()

        division_counter = 0

        for i in range(1, number + 1):
            if number % i == 0:
                division_counter += 1
            
        if division_counter == 2 and answer == 'yes' or division_counter > 2 and answer == 'no':
            print('Correct!')
            prime_counter += 1

        elif division_counter > 2 and answer == 'yes' or division_counter == 2 and answer == 'no': 
            print(f"{answer} is wrong answer ;(. Correct answer is 'no' ")
            print(f"Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!") 


if __name__ == '__main__':
    main()