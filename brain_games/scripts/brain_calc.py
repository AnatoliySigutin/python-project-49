from random import choice, randint

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    calc_counter = 0
    max_counter = 3
    right_answer = 'Correct!'

    print('What is the result of the expression?')

    while calc_counter < max_counter:
        x_1 = randint(1, 100)
        x_2 = randint(1, 100)
        list_mention = ['+', '-', '*']
        random_mention = choice(list_mention)

        if random_mention == '+':
            correct_answer = x_1 + x_2
        elif random_mention == '-':
            correct_answer = x_1 - x_2
        elif random_mention == '*':
            correct_answer = x_1 * x_2

        print(f'Question: {x_1} {random_mention} {x_2}')
        answer = prompt.string('Your answer: ')

        if int(answer) == correct_answer:
            print(right_answer)
            calc_counter += 1
        
        else: 
            print(f'{answer} is wrong answer ;(. '
            f'Correct answer is {correct_answer}')
            print(f"Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!") 


if __name__ == '__main__':
    main()
    

    