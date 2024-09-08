import random
import prompt
from brain_games.invitation import invite_str


welcome_string = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return random_number % 2 == 0 


def game():
	number = random.randint(0, 99)
	correct_answer = "yes" if is_even(number) else "no"
	question = f'Question: {number}'
	return number, correct_answer


invite_str(game, welcome_string)
