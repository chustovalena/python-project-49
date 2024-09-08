import prompt

def invite_str(game, welcome_string):
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
	print(welcome_string)
	for i in range(0,3):
		question, result = game()
		print(question)
		user_answer = input()
		print(f'Your answer: {user_answer}')
		if user_answer == result:
			print('Correct!')
		else:
			print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{result}".')
			print(f"Let's try again, {name}!")
			break
		if i == 2:
			print(f'Congratulations, {name}!')

