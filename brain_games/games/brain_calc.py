import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2

    question = f'{num1} {operator} {num2}'
    correct_answer = str(result) 

    return question, correct_answer