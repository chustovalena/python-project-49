import prompt

ROUNDS = 3


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_engine(game):
    name = greet_user()
    print(game.WELCOME_STRING)
    for _ in range(ROUNDS):
        question, res = game.game()
        print('Question: ' + question)
        user = input()
        print(f'Your answer: {user}')
        if user != str(res):
            print(f'"{user}" is wrong answer ;(.'
                  f' Correct answer was "{res}".'
                  f'\nLet\'s try again, {name}!')
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
