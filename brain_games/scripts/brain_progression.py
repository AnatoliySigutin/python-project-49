from random import choice, randint

import prompt


def brain_progression(name):
    x_1 = randint(1, 100)
    x_2 = randint(1, 100)
    if x_2 <= x_1 + 10:
        x_2 = x_1 + 15

    list_range = []
    x_step = randint(1, 5)

    max_length = 10  
    current = x_1

    while current <= x_2 and len(list_range) < max_length:
        list_range.append(current)
        current += x_step

    choose_index = choice(range(len(list_range)))
    choose_number = list_range[choose_index] 

    list_range[choose_index] = '..'

    print('What number is missing in the progression?')
    print(f'Question: {list_range}')

    answer = prompt.string('Your answer: ')

    if int(answer) == choose_number:
        print('Correct!')
    else:
        print(f'Wrong. The correct answer is {choose_number}.')
        print(f"Let's try again, {name}")
    

    