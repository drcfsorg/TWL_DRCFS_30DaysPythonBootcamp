import random
random_number = random.randint(1, 10)
Player_name = input("Enter your name: ")
print("The name of the player is " + Player_name )
guess = int(input("enter your guess number: "))
attempts = 0

while attempts == 5:
    attempts = attempts + 1
    if guess < random_number:
        print("Your value is too low")
    elif guess > random_number:
        print("Your value is too low")
    elif guess == random_number:
        print("Hurrah! Your did it")
    else:
        break
