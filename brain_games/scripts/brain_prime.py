from random import randint
from prompt_toolkit import prompt


def brain_prime(name):
    number = randint(1, 100)
    division_counter = 0

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {number}')
    answer = prompt('Your answer: ')

    for i in range(number):
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
    elif division_counter == 2 and answer == 'no': 
        print(f"{answer} is wrong answer ;(. Correct answer is 'yes' ")
        print("Let's try again, {name}!")