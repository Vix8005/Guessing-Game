import random
difficulty = input("Choose a difficulty level (easy, medium, hard): ")
if difficulty == "easy":
    number = random.randint(1, 10)
    print("You have 3 tries to guess the number between 1 and 10.")

elif difficulty == "medium":
    number = random.randint(1, 20)
    print("You have 3 tries to guess the number between 1 and 20.")

else:
    number = random.randint(1, 50)
    print("You have 3 tries to guess the number between 1 and 50.")
guess= int(input("Guess the number: "))
tries = 1
while tries < 3 and guess != number:
    if guess < number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))
    tries += 1
if guess==number or tries ==3:
    print(f"The number was {number}. You guessed {guess}.")