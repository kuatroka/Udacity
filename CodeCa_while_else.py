from random import randint

# Generates a number from 1 through 10 inclusive


guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    random_number = randint(1, 10)
    if guess == random_number:
        print "You won!"
        break
    else:
        print "You lose"
        guesses_left -= 1
else:
    print "Game Over!"



