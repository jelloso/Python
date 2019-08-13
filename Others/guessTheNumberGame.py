import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1,10)
print('Well ' + name + ', I am thinking of a number between 1 and 10.')

for guessesTaken in range(1,6):
	print('Take a guess.')
	guess = int(input())
	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is too high')
	else:
		break # This condition is for the corret guess!

if guess == secretNumber:
	print('Good job ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('Nope loser. The number I was thinking of was ' + str(secretNumber) + '.')