import prompt
from random import randint
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'


def get_gcd():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    print(f'Question: {first_number} {second_number}')
    answer = prompt.string('Your answer: ')
    right_answer = str(gcd(first_number, second_number))
    return right_answer, answer
