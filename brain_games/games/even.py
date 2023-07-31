import prompt
from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_right_answer(number):
    return number % 2 == 0


def get_even():
    number = randint(1, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    right_answer = get_right_answer(number)
    if right_answer is True:
        right_answer = 'yes'
    if right_answer is False:
        right_answer = 'no'
    return right_answer, answer
