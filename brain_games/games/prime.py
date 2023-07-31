import prompt
from random import randint
from math import sqrt


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_right_answer(number):
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True


def get_prime():
    number = randint(2, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    right_answer = get_right_answer(number)
    if right_answer is True:
        right_answer = 'yes'
    if right_answer is False:
        right_answer = 'no'
    return right_answer, answer
