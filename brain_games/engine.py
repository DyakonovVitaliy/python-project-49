import prompt

QUANTITY_QUESTION = 3


def greet_and_invite():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(function, task):
    name = greet_and_invite()
    print(task)
    for _ in range(QUANTITY_QUESTION):
        true_result, question = function()
        print(question)
        answer = prompt.string('Your answer: ')
        if true_result == answer:
            print('Correct!')
        else:
            return print(f'\'{answer}\' is wrong answer ;(. '
                         f'Correct answer was \'{true_result}\'.'
                         f"\nLet's try again, {name}!")
    print(f'Congratulations, {name}!')
