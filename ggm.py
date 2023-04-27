from random import randint

num = randint(1, 100)

print('GUESSING GAME CHALLENGE\nGuess a number between 1 and 100')

ng = 0

guess = int(input('Enter your guess: '))
if guess < 1 or guess > 100:
    print('OUT OF BOUNDS!')
    ng += 1

i = abs(num-guess)

if i <= 10:
    print('WARM!')
    ng+=1
else:
    print('COLD!')
    ng+=1

while(True):
    guess = int(input('Enter again: '))
    ng += 1
    j = abs(num-guess)
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS!')
    elif guess == num:
        print("Congratulations! You've guessed correctly\nNumber of guesses =",ng)
        break
    elif j<i:
        print('WARMER!')
        i=j
    else:
        print('COLDER!')
