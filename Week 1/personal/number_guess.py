# rand no generator
# user input function
# give user 3 guess
# if no found -> end the game
# check if the number is greater than the random number
# check if the number is smaller than the random number
# if the number is not guessed then end the game with reveal the number


# control + 

import random
random_number = (random.randint(1, 10))
for i in range(5):
    user_guess = int(input('Enter your guess here:'))

    # for _ in range(3):
    if user_guess == random_number:
        print('*' *5)
        print(f"yo've done this in {i+1} tries")
        print('*' *5)
        break
    elif user_guess > random_number:
        print('*' *5)
        print("choice is greater than the random number")
        print('*' *5)
    elif user_guess < random_number:
        print('*' *5)
        print("choice is lower than the random number")
        print('*' *5)
    if i == 4:
        print("Better luck next time")



