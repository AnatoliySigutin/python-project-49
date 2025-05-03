from random import randint
from prompt_toolkit import prompt


def brain_gcd(name):
    x_1 = randint(2, 100)
    x_2 = randint(2, 100) 

    print('Find the greatest common divisor of given numbers.')
    print('Question: {x_1} {x_2}')

    answer = prompt('Your answer: ')

    correct_answer = node_gcd(x_1, x_2)

    if int(answer) == correct_answer:
        print('Correct!')
    else:
        print(f'Wrong. The correct answer is {correct_answer}.')
        print(f"Let's try again, {name}")

# Вызов функции (например, с именем пользователя)
brain_gcd('User')

def node_gcd(x_1, x_2):
    while x_1 != 0 and x_2 != 0:
        if x_1 > x_2:
            x_1 = x_1 % x_2
        else:
            x_2 = x_2 % x_1
        
        return x_1 + x_2  
    
    