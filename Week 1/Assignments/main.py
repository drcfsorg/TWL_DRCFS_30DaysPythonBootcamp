# exception handling

user_inp = input("enter a number: ")

try:
    user_inp = int(user_inp)
    print(user_inp)
    print(type(user_inp))
except Exception as e:
    # print(e)
    print('#'*80)
    print(f'Please only enter integer value for the given input. "{user_inp}" is not an integer.\n Closing the program...')
    print(('#'*80))
import random
i=0
while i<=4:
    selection = int(input('Enter user throw'))

    if (selection == 1):
        user_throw= "Rock"
    elif selection == 2:
        user_throw="Paper"
    elif selection == 3: 
        user_throw = "Scissors"

    print('Player Throws', user_throw)

    throws= ["Rock", "Paper","Scissors"]
    comp_throw = random.choice(throws)

    print('Computer throws', comp_throw)

    if user_throw == comp_throw:
        print("Tie Game")
    elif user_throw == "Rock":
        if comp_throw == "Paper":
            print("Comp Wins")
        elif comp_throw == "Scissors":
            print("Player Wins")
    elif user_throw == "Paper":
        if comp_throw == "Scissors":
            print("Comp Wins")
        elif (comp_throw == "Rock"):
            print("Player Wins")
    elif user_throw == "Scissors":
        if comp_throw == "Rock":
            print("Comp Wins")
        elif (comp_throw == "Paper"):
            print("Player Wins")
    
    i = i + 1
    
        
