import random
import prompt


welcome_string = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return random_number % 2 == 0 


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print(welcome_string)


def res():
	number = random.randint(0, 99)
	correct_answer = "yes" if is_even(number) else "no"
	return number, correct_answer



def game_even():
	for i in range(0, 3):
		number1, correct_answer1 = res()
		print(f'Question: {number}')
		user_answer = input()
		if user_answer == correct_answer:
			print('Correct!')
		else:
			print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
			print(f"Let's try again, {name}!")
			break
		if i == 2:
			print(f'Congratulations, {name}!')


game_even()
