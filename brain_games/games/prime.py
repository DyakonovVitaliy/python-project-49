from random import randint
from math import sqrt


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_simple_number(number):
    if number == 0 or number == 1:
        return False
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True


def get_prime():
    number = randint(0, 100)
    question = f'Question: {number}'
    right_answer_boolean = is_simple_number(number)
    if right_answer_boolean is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, question
