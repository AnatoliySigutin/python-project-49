from random import randint
import prompt
from brain_games.cli import welcome_user


def main():
    name = welcome_user()


    counter_1 = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    total_required = 3

    while counter_1 < total_required:    
        x = randint(1, 100)
        print(f'Question: {x}')
        answer = prompt.string('Your answer: ')

        if x % 2 == 0 and answer == 'yes':
            print('Correct!')
            counter_1 += 1

        elif x % 2 != 0 and answer == 'no':
            print('Correct!')
            counter_1 += 1

        elif x % 2 != 0 and answer == 'yes':
            print(f"{answer} is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return

        elif x % 2 == 0 and answer == 'no': 
            print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            return

    if counter_1 == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
     main()