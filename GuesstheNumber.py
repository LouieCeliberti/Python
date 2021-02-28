import random

for guesses in range(10):
    print("Guess a number")
    guess = input()
    correctnumber = random.randint(1,5)

    print(correctnumber)

    if guess == correctnumber:
        print("Congrats you guessed the number")
    else:
        print("Guess again")

