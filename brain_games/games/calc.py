import random


WELCOME_STRING = 'What is the result of the expression?'


def random_operation():
    """Random choosing an operation"""
    list_of_operations = ['-', '+', '*']
    current_oper = random.choice(list_of_operations)
    return current_oper


def operations(first_number, second_number, current_oper):
    """Do math operation with args, return result"""
    if current_oper == '-':
        current_res = first_number - second_number
    elif current_oper == '+':
        current_res = first_number + second_number
    else:
        current_res = first_number * second_number
    return current_res


def game():
    first_number = random.randint(0, 49)
    second_number = random.randint(0, 49)
    current_oper = random_operation()
    question = f'{first_number} {current_oper} {second_number}'
    result = operations(first_number, second_number, current_oper)
    return question, result
