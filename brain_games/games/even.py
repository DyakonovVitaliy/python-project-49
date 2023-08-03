from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(number):
    return number % 2 == 0


def get_even():
    number = randint(1, 100)
    question = f'Question: {number}'
    right_answer_boolean = is_even_number(number)
    if right_answer_boolean is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, question
