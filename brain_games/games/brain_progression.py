import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    
    x_1 = random.randint(1, 100)
    x_step = random.randint(1, 7)
    max_length = 10
    min_x_2 = x_1 + (max_length - 1) * x_step
    x_2 = random.randint(max(x_1 + 40, min_x_2), x_1 + 140)

    question, correct_answer = progression(x_1, x_2, x_step)

    if not question:
        return generate_round()

    return question, correct_answer


def progression(x_1, x_2, x_step):
    current = x_1
    max_length = 10
    list_range = []

    while current <= x_2 and len(list_range) < max_length:
        list_range.append(current)
        current += x_step

    if not list_range:
        return "", ""

    choose_index = random.choice(range(len(list_range)))
    choose_number = list_range[choose_index]

    question_list = list(list_range)
    question_list[choose_index] = '..'
    question_string = ' '.join(map(str, question_list))

    correct_answer = str(choose_number) 

    return question_string, correct_answer

