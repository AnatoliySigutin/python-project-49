from random import choice, randint

from prompt_toolkit import prompt


def brain_calc(name):
    x_1 = randint(1, 100)
    x_2 = randint(1, 100)
    list_mention = ['+', '-', '*', '/']
    random_mention = choice(list_mention)
    print('What is the result of the expression?')
    print(f'Question: {x_1} {random_mention} {x_2}')
    answer = prompt('Your answer: ')

    if random_mention == '+':
        summ = x_1 + x_2
        if summ == int(answer):
            print('Correct!')
        else: 
            print(f'{answer} is wrong answer ;(. Correct answer is {summ}')
            print("Let's try again, {name}!")

    elif random_mention == '-':
        diff = x_1 - x_2
        if diff == int(answer):
            print('Correct!')
        else: 
            print(f'{answer} is wrong answer ;(. Correct answer is {diff}')
            print("Let's try again, {name}!")

    elif random_mention == '*':
        multiplication = x_1 * x_2
        if multiplication == int(answer):
            print('Correct!')
        else: 
            print(f'{answer} is wrong answer ;(. '
      f'Correct answer is {multiplication}')
            print("Let's try again, {name}!")
    
    elif random_mention == '/':
        division = x_1 / x_2
        if division == int(answer):
            print('Correct!')
        else: 
            print(f'{answer} is wrong answer ;(. Correct answer is {division}')
            print("Let's try again, {name}!")
    

    