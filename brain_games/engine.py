import prompt

QUANTITY_QUESTION = 3

def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def logic(function, task):
    name = greet()
    print(task)
    for _ in range(QUANTITY_QUESTION):
        true_result, answer = function()
        if true_result == answer:
            print('Correct!')
        else:
            return print(f'\'{answer}\' is wrong answer ;(. '
                         f'Correct answer was \'{true_result}\'.'
                         f"\nLet's try again, {name}!")
    print(f'Congratulations, {name}!')
