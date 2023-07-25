import prompt
from random import randint, choice
from operator import add, sub, mul

the_task = 'What is the result of the expression?'
OPERATORS = {'+': add, '-': sub, '*': mul}


def get_right_answer(first_operand, OPERATOR, second_operand):
    right_answer = OPERATORS[OPERATOR](first_operand, second_operand)
    return right_answer


def get_calc():
    first_operand = randint(1, 50)
    second_operand = randint(1, 50)
    OPERATOR = str(choice(['+', '-', '*']))
    print(f'Question: {first_operand} {OPERATOR} {second_operand}')
    answer = prompt.string('Your answer: ')
    right_answer = str(get_right_answer(first_operand,
                                        OPERATOR, second_operand))
    return right_answer, answer
