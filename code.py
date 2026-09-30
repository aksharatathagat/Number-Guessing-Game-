import random

number = random.randint(1, 100)

print("Welcome to the random number generator!")
print("I have chosen a number between 1 and 100.")
print("Try to guess the number.")

guess = int(input("Enter your guess: "))

while guess != number:

    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    guess = int(input("Enter your guess: "))

print("Congratulations!")
print("You guessed the correct number:", number)