import random

print("-------------------------------------------------------------------------------------------------------")

input("Welcome to Guess the number, a game which requires you to guess the given number from 1-100. Good Luck!")

print("-------------------------------------------------------------------------------------------------------")

randomNumber = random.randint(0,100)

# If statements ->

while True:
    guess = input("Please enter a number from 1-100 as your guess: ")

    guess = int(guess)

    # Here Computer is checking for correct number
    
    if guess> randomNumber:
        print("Invalid, number too high. Please try again")

    if guess< randomNumber:
        print("Invalid, number too low. Please try again")

    if guess == randomNumber:
        print("Great Job, you got my number. " + "My number was " + str(randomNumber) + ".")
        print("( ͡❛ ͜ʖ ͡❛)👌")
        break

   
    
