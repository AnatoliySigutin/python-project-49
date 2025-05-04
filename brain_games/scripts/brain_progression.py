from random import choice, randint
from brain_games.cli import welcome_user
import prompt


def main():
    name = welcome_user()
    prog_counter = 0
    max_counter = 3


    print('What number is missing in the progression?')

    while max_counter > prog_counter:
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
        question_string = ' '.join(map(str, list_range))

        print(f'Question: {question_string}')

        answer = prompt.string('Your answer: ')

        if int(answer) == choose_number:
            print('Correct!')
            prog_counter += 1
        else:
            print(f'Wrong. The correct answer is {choose_number}.')
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == '__main__':
     main()
    