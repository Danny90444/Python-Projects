import random

# fucntion to loop through numbers until the guess is correct

def guess(x):
	random_number = random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}:'))
		if guess < random_number:
			print("Sorry, guess again. Too low.")
		elif guess > random_number:
			print("Sorry, guess again. Too high.")
	print(f"Congratulations! You have guess the correct number {random_number}!")
	

guess(10)