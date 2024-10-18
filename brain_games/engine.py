import prompt


ROUNDS = 3


def invite_str():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def engine_func(game):
    name = invite_str()
    print(game.WELCOME_STRING)
    for _ in range(ROUNDS):
        question, res = game.game()
        print(question)
        user = input()
        print(f'Your answer: {user}')
        if user != res:
            return print(f'"{user}" is wrong answer ;(.'
                         f' Correct answer was "{res}".'
                         f'\nLet\'s try again, {name}!')
        print('Correct!')
    return print(f'Congratulations, {name}!')
