from random import randint
from brain_games.cli import welcome_user
import prompt


def main():
    name = welcome_user()
    division_counter = 0
    prime_counter = 0
    max_counter = 3

    print('Answer "yes" if given number is prime. Otherwise answer "no".')


    while prime_counter < max_counter:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        for i in range(1, number):
            if number % i == 0:
                division_counter += 1
            else:
                division_counter = division_counter

        if division_counter == 2 and answer == 'yes':
            print('Correct!')

        elif division_counter >= 2 and answer == 'no':
            print('Correct!')

        elif division_counter >= 2 and answer == 'yes': 
            print(f"{answer} is wrong answer ;(. Correct answer is 'no' ")
            print("Let's try again, {name}!")
            return
        
        elif division_counter == 2 and answer == 'no': 
            print(f"{answer} is wrong answer ;(. Correct answer is 'yes' ")
            print("Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!") 


if __name__ == '__main__':
     main()