#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():

    return prompt.string('May I have your name? ')


def get_right_answer(number):
    if number % 2 == 0:
        right_answer = 'yes'
    elif number % 2 != 0:
        right_answer = 'no'
    return right_answer

def main():
    print('Welcome to the Brain Games!')
    the_task = 'Answer "yes" if the number is even, otherwise answer "no".'
    quantity_question = 3
    name = welcome_user()
    print(f'Hello, {name}')
    print(the_task)
    for _ in range(quantity_question):
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        right_answer = get_right_answer(number)
        if number % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif number % 2 != 0 and answer == 'no':
            print('Correct!')
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'. \nLet's try again, {name}!")
    print(f'Congratulations, {name}!')


if __name__ == '__main__':

    main()