#random number generator
#user input function
#give user 4 guesses
#check if the number is exactly the same -> game end
#check if the number is greater than the random number 
#check if the number is smaller than the random number
#end the game and reveal the number

import random 
random_number = random.randint(1, 10)

#control + / = comment, and _ is used to dispose any unwanted value
#control + ] = indent (4 spaces)

for i in range(4):
    guess = int(input('Enter your guess between 1 and 10 here'))
    if guess>10:
        print('Guess a number between 1 and 10')
    elif guess == random_number:
        print('*'*50)
        print(f'hurray!! you got the correct guess in {i+1} tries')
        print('*'*50)
        break
    elif guess > random_number:
        print('guess a smaller number')
    elif guess < random_number:
        print("guess a bigger number")
    print (f'you have {3-i} tries remaining')
    if i==3:
        print('Your are a bad guesser')

# for _ in range(4):
#     guess = int(input('Enter your guess between 1 and 10 here'))
#     if guess>10:
#         print('Guess a number between 1 and 10')
#     elif guess == random_number:
#         print('*'*50)
#         print('hurray!! you got the correct guess')
#         print('*'*50)
#         break  
#     elif guess > random_number:
#         print('Your guess is greater than the random number ')
#     elif guess < random_number:
#         print("Your guess is smaller than the random number ")
    