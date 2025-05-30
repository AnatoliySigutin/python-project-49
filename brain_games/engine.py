import prompt

from brain_games import cli
from brain_games.constants import MAX_ROUNDS


def run_game(generate_round_function, description):

    name = cli.welcome_user()

    print(description)

    wins_count = 0
    while wins_count < MAX_ROUNDS:
        question, correct_answer = generate_round_function()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            wins_count += 1
        else:
            print(f'{user_answer} is wrong answer ;(. '
            f'Correct answer is {correct_answer}')
            print(f"Let's try again, {name}!")
            return
        
    print(f'Congratulations, {name}!')