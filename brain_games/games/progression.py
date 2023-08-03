from random import randint


TASK = 'What number is missing in the progression?'


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
    list_progression[iter_hidden_number] = '..'
    progression = " ".join(str(i) for i in list_progression)
    question = f'Question: {progression}'
    return right_answer, question
