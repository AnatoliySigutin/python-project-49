from random import randint

import prompt


def brain_even(name):
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
        else:
            print('Wrong! Try again.')
            counter_1 = 0
    if counter_1 == 3:
        print(f"Congratulations, {name}!")
