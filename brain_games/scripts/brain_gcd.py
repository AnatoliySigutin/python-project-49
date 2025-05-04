from random import randint
import prompt
from brain_games.cli import welcome_user

def main():
    name = welcome_user()
    gcd_counter = 0
    max_counter = 3


    print('Find the greatest common divisor of given numbers.')

    x_1 = randint(2, 100)
    x_2 = randint(2, 100) 

    while max_counter > gcd_counter:
        print(f'Question: {x_1} {x_2}')

        answer = prompt.string('Your answer: ')

        correct_answer = node_gcd(x_1, x_2)

        if int(answer) == correct_answer:
            print('Correct!')
            gcd_counter += 1
        else:
            print(f'Wrong. The correct answer is {correct_answer}.')
            print(f"Let's try again, {name}")
            return

    print(f"Congratulations, {name}!") 


if __name__ == '__main__':
     main()
    


def node_gcd(x_1, x_2):
    while x_1 != 0 and x_2 != 0:
        if x_1 > x_2:
            x_1 = x_1 % x_2
        else:
            x_2 = x_2 % x_1
        
    return x_1 + x_2  
    
    