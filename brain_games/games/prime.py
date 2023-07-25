import prompt
from random import randint
from math import sqrt


the_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_right_answer(number):
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            return 'no'
        i += 1
    return 'yes'


def get_prime():
    number = randint(2, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    right_answer = get_right_answer(number)
    return right_answer, answer
