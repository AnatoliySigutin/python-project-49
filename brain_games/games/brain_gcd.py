import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    
    num1 = random.randint(2, 100)  # //NOSONAR
    num2 = random.randint(2, 100)  # //NOSONAR
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
