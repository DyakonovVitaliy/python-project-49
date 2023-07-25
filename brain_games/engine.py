import prompt


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def logic(function, the_task):
    name = greeting()
    quantity_question = 3
    print(the_task)
    for _ in range(quantity_question):
        true_result, answer = function()
        if true_result == answer:
            print('Correct!')
        else:
            return print(f'\'{answer}\' is wrong answer ;(. '
                         f'Correct answer was \'{true_result}\'.'
                         f"\nLet's try again, {name}!")
    print(f'Congratulations, {name}!')
