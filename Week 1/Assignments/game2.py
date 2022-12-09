import random
user_action = input("Enter a choice(rock, paper, scissors):")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
if user_action == computer_action:
    print("Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("You win")
    else:
        print("paper covers rock! you lose ")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers the rock, You win")
    else:
        print("Scissors cut paper! you lose")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Paper cut by scissors, You win")
    else:
        print("Scissors placed on rock ! you lose")



