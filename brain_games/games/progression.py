import random
from brain_games.invitation import invite_str


welcome_string = 'What number is missing in the progression?'


def oper_progression(start_prog, step_prog):
    res_prog = []
    for i in range(10):
        res_prog.append(start_prog + i * step_prog)
    result = random.choice(res_prog)
    index = res_prog.index(result)
    res_prog[index] = '..'
    prog = ' '.join(map(str, res_prog))
    return prog, result


def game():
    start_prog = random.randint(1, 9)
    step_prog = random.randint(1, 9)
    prog, result = oper_progression(start_prog, step_prog)
    question = f'Question: {prog}'
    return question, str(result)


def go():
    invite_str(game, welcome_string)
