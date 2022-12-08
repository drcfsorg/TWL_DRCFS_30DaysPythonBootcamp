import random
random_number = random.randint(1, 10)
guess = int(input("enter your guess number: "))

# control + / = comment  and _ is used to dispose any unwanted value
# shortcut Control + ] = indent(4 spaces)
for i in range (5):
    if guess == random_number:
        print(' *'*50)
        print('horray !! you got the correct guess in {i+1} tries ')
        break # to break the guess
    elif guess > random_number:
        print(' * '* 50)
        print('great')