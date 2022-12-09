# Welcome to week 1 of the bootcamp.
This folder contains all assignments that you need to pass to go through the first week.

## Objective
- A computer will generate a random number between 1 - 10, and the user must guess it in five attempts.
- Computer will display the answer along with the number of attempts when the user guesses that the number is high or low. The computer will provide various hints based on the user's guess.

## Write a short program that meets all of the following requirements
1. import the required module
2. From imported module, generate a number between 1 - 10 and then store it the variable
3. Take a player name as an input and store it in the variable
4. Then create a variable and assign it as 0, later we will increase this value on each iteration of the while loop
5. Before starting while loop, print a string that include the player name
6. Now, construct the while loop:
  - Using `while` loop give player 5 attempts to guess the number
  - If the player enters an input, then store it in the guess variable, also ensure that you convert input to an integer before storing it in the variable (it will helps us to perform mathematical calculation)
  - Make 3 conditional statement: In first, check if guess is lower than generated number and if it is low print `Your guess is too low`
  - Similarly, check the guess is greater than generated number and if it is greater print `Your guess is too high`
  - Check the guess is equal to generated number. If it become equal then terminate the loop entirely using `break` keyword
7. The message should be printed for the player along with the number of attempts if they guessed the number correctly. Otherwise, the message should be printed along with the number if they could not guess the number.

---

## Write a python script to make Rock Paper Scissor Game 

To play the rock, paper, scissor game, two players each choose one of three options: rock, paper, or scissors. If both players choose the same option, the game is a tie. Otherwise, the following rules apply:
- Rock beats scissors (rock breaks scissors)
- Scissors beats paper (scissors cuts paper)
- Paper beats rock (paper covers rock)

If player 1 chooses rock and player 2 chooses scissors, player 1 wins. If player 1 chooses paper and player 2 chooses rock, player 1 wins. And if player 1 chooses scissors and player 2 chooses paper, player 1 wins. The game continues until one player reaches a certain number of wins, at which point the game ends and that player is declared the winner.

## Steps to be followed while creating rock, paper, scissor game:
- Initialize the player's score and the number of times they have played. 
- Then use while loop that continues until the player has played 5 times. 
- Inside the loop, we ask the player to choose rock, paper, or scissors and generate the computer's move by randomly choosing one of the three options. 
- We then use if-else statements to check for the different combinations of moves and determine a winner. 
- If the player wins, their score is incremented by one. After the loop, we print the final score.
