from math import gcd
import random


WELCOME_STRING = 'Find the greatest common divisor of given numbers.'


def gcd_gen(number1, number2):
    result = gcd(number1, number2)
    return result


def game():
    first_number = random.randint(0, 99)
    second_number = random.randint(0, 99)
    question = f'Question: {first_number} {second_number}'
    result = gcd_gen(first_number, second_number)
    return question, str(result)
