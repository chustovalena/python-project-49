import random


WELCOME_STRING = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    """Return True if number is even, False if numer is not even"""
    return random_number % 2 == 0


def game():
    number = random.randint(0, 99)
    correct_answer = "yes" if is_even(number) else "no"
    question = f'{number}'
    return question, correct_answer
