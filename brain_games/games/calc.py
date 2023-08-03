from random import randint, choice
from operator import add, sub, mul

TASK = 'What is the result of the expression?'


def get_operator(operator):
    OPERATORS = {'+': add, '-': sub, '*': mul}
    return OPERATORS[operator]


def get_right_answer(first_operand, OPERATOR, second_operand):
    right_answer = get_operator(OPERATOR)(first_operand, second_operand)
    return right_answer


def get_calc():
    first_operand = randint(1, 50)
    second_operand = randint(1, 50)
    OPERATOR = str(choice(['+', '-', '*']))
    question = f'Question: {first_operand} {OPERATOR} {second_operand}'
    right_answer = str(get_right_answer(first_operand,
                                        OPERATOR, second_operand))
    return right_answer, question
