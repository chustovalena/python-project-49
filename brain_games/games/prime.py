import random
import math


WELCOME_STRING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Return True if number is Prime and False if number is not Prime"""
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            return False
    return True


def game():
    number = random.randint(0, 99)
    result = "yes" if is_prime(number) else "no"
    question = f'{number}'
    return question, result
