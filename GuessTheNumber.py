import random

print('I am thinking of a number between 1 and 20.')
res = random.randint(1, 21)
guessCount = 0
while True:
    print("Take a guess.")
    num = int(input())
    if num < res:
        print("Your guess is too low.")
        guessCount += 1
    elif num > res:
        print("Your guess is too high.")
        guessCount += 1
    else:
        print("Good job! You guessed my number in " + str(guessCount) + " guesses!")
        break
