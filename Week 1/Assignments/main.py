import random
print("Welcome to rock, paper, and scissors game.")
game = ["rock", "paper", "scissors",]
chance = 0
player_score = 0
computer_score = 0
while chance < 5:
    while True:
        player_choice = input("Choose one among rock, paper, and scissors: ").lower()
        if player_choice  in game:
            break
    computer_choice = random.choice(game)
    print(f"Player chooses {player_choice}")
    print(f"Computer chooses {computer_choice}")
    if computer_choice ==  player_choice: 
        print(f"Tie as both player selects {player_choice}")                           #if bother users select same option, It's a tie
    elif player_choice == "rock" :
        if computer_choice == "paper":
            print("computer wins")             #between rock and paper, paper wins
            computer_score+=1
        else:
            print("player wins") 
            player_score+=1                           #only remaining choice for computer is scissors. So between rock and scissors, rocks wins
    elif player_choice == "paper" :
        if computer_choice == "rock":          #between paper and rock, paper wins
            print("player wins")
            player_score+=1      
        else:
            print("computer wins")               #only remaining choice for computer is scissors. So between paper and scissors, scissors wins
            computer_score+=1
    elif player_choice == "scissors" :         
        if computer_choice == "paper":         #between scissors and paper, scissors wins        
            print("player wins")
            player_score+=1      
        else:
            print("computer wins")               #only remaining choice for computer is rock. So between scissors and rock, rock wins
            computer_score+=1
    chance+=1
if computer_score > player_score:
    print(f"Computer wins with score {computer_score}")
elif player_score > computer_score:
    print(f"Player wins with score {player_score}")
else:
    "It's a tie! Nobody wins!"