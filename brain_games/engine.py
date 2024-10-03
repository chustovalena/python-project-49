import prompt


def engine_func(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.WELCOME_STRING)
    for i in range(0, 3):
        question, res = game.game()
        print(question)
        user = input()
        print(f'Your answer: {user}')
        if user == res:
            print('Correct!')
        else:
            print(f'"{user}" is wrong answer ;(. Correct answer was "{res}".')
            print(f"Let's try again, {name}!")
            break
        if i == 2:
            print(f'Congratulations, {name}!')
