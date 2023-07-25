import prompt
from random import randint


the_task = 'What number is missing in the progression?'


def build_progression():
    quantity_number = 10
    first_border = randint(1, 50)
    step = randint(1, 5)
    second_border = first_border + (step * quantity_number)
    list_progression = list(range(first_border, second_border, step))
    return list_progression


def get_progression():
    list_progression = build_progression()
    iter_hidden_number = randint(0, 9)
    right_answer = str(list_progression[iter_hidden_number])
    progression = ''
    for n in list_progression:
        progression += str(n) + ' '
    progression = progression.strip()
    progression = progression.replace(right_answer, '..')
    print(f'Question: {progression}')
    answer = prompt.string('Your answer: ')
    return right_answer, answer
