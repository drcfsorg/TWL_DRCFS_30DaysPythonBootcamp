# random number generator
# user input function. 
# give user 4 guesses
# check if the number is exactly the same -> game end..
# check if the number is greater than the random number
# check is the number is smaller than the random number
# end the game and reveal the number.
import random

random_number = random.randint(1, 10)

# control + / = comment, and _ is used to dispose any unwanted value
# control + ] = indent(4 spaces)
for i in range(4):
    guess = int(input('Enter your guess between 1 and 10 here: '))
    if guess > 10:
        print("Guess a numeber between 1 and 10")
    elif guess == random_number:
        print('*'*50)
        print(f"HORRAY!!! You got the correct guess ")
        print('*'*50)
        break
    elif guess > random_number:
        print('*'*50)
        print("Your guess is greater than the random number")
        print('*'*50)
    elif guess < random_number:
        print('*'*50)
        print("Your guess is less than the random number")
        print('*'*50)
    
    print(f"you have {3-i} tries remaining")
    if i == 3:
        print('*'*50)
        print("You're a bad guesser")
        print('*'*50)