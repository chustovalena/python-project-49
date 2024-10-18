import random
import math


WELCOME_STRING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    res = '-'
    if number <= 1:
        res = 'no'
        return res
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            res = 'no'
            return res
    if res == '-':
        res = 'yes'
    return res


def game():
    number = random.randint(0, 99)
    result = is_prime(number)
    question = f'Question: {number}'
    return question, result
