from random import choice, randint
from brain_games.cli import welcome_user
import prompt


def main():
    name = welcome_user()

    x_1 = randint(1, 100)
    x_2 = randint(1, 100)
    list_mention = ['+', '-', '*', '/']
    random_mention = choice(list_mention)
    print('What is the result of the expression?')
    print(f'Question: {x_1} {random_mention} {x_2}')
    answer = prompt.string('Your answer: ')

    if random_mention == '+':
        summ = x_1 + x_2
        if summ == int(answer):
            print('Correct!')
        else: 
            print(f'{answer} is wrong answer ;(. Correct answer is {summ}')
            print("Let's try again, {name}!")
            return

    elif random_mention == '-':
        diff = x_1 - x_2
        if diff == int(answer):
            print('Correct!')
        else: 
            print(f'{answer} is wrong answer ;(. Correct answer is {diff}')
            print("Let's try again, {name}!")
            return

    elif random_mention == '*':
        multiplication = x_1 * x_2
        if multiplication == int(answer):
            print('Correct!')
        else: 
            print(f'{answer} is wrong answer ;(. '
      f'Correct answer is {multiplication}')
            print("Let's try again, {name}!")
            return
    
    elif random_mention == '/':
        division = x_1 / x_2
        if division == int(answer):
            print('Correct!')
        else: 
            print(f'{answer} is wrong answer ;(. Correct answer is {division}')
            print("Let's try again, {name}!")
            return


if __name__ == '__main__':
     main()
    

    