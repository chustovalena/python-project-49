import random
from brain_games.invitation import invite_str


welcome_string = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
	prime_row_base = [2,3,5,7]
	result = '-'
	if number in prime_row_base and number != 2:
		result = 'yes'
		return result 
	for itera in prime_row_base:
		if number % itera == 0:
			result = 'no'
			break
	if result == '-':
		result = 'yes'
	return result


def game():
	number = random.randint(0, 99)
	result = is_prime(number)
	question = f'Question: {number}'
	return question, result


def go():
	invite_str(game, welcome_string)