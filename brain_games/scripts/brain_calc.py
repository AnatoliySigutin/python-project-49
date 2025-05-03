from random import choice, randint
from brain_games.cli import welcome_user
import prompt


def main():
    name = welcome_user()
    calc_counter = 0
    max_counter = 3


    x_1 = randint(1, 100)
    x_2 = randint(1, 100)
    list_mention = ['+', '-', '*']
    random_mention = choice(list_mention)
    print('What is the result of the expression?')
    print(f'Question: {x_1} {random_mention} {x_2}')
    answer = prompt.string('Your answer: ')

    while calc_counter < max_counter:
        if random_mention == '+':
            summ = x_1 + x_2
            if summ == int(answer):
                print('Correct!')
                calc_counter += 1
            else: 
                print(f'{answer} is wrong answer ;(. Correct answer is {summ}')
                print(f"Let's try again, {name}!")
                return

        elif random_mention == '-':
            diff = x_1 - x_2
            if diff == int(answer):
                print('Correct!')
                calc_counter += 1
            else: 
                print(f'{answer} is wrong answer ;(. Correct answer is {diff}')
                print(f"Let's try again, {name}!")
                return

        elif random_mention == '*':
            multiplication = x_1 * x_2
            if multiplication == int(answer):
                print('Correct!')
                calc_counter += 1
            else: 
                print(f'{answer} is wrong answer ;(. '
                f'Correct answer is {multiplication}')
                print(f"Let's try again, {name}!")
            return
    if calc_counter == 3:
        print(f"Congratulations, {name}!") 


if __name__ == '__main__':
     main()
    

    