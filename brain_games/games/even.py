import prompt
from random import randint


the_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_right_answer(number):
    if number % 2 == 0:
        right_answer = 'yes'
    elif number % 2 != 0:
        right_answer = 'no'
    return right_answer


def get_even():
    number = randint(1, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    right_answer = get_right_answer(number)
    return right_answer, answer
