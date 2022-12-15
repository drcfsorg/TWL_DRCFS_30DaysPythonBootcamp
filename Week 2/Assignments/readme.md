# Welcome to week 2 of the bootcamp.
This folder contains all assignments that you need to pass to go through the second week.

Create a program to complete the following objective

## Objective 
You goal is to create a Python script (Program) that will present the user with two different options.
1. Open an Input text file (Users-Pwds.txt) that contains usernames and passwords. Then create an
Output text File (Users-Pwds-Chked.txt). The output text file will contain the username, password, and
strength (POOR or Moderate or Strong).
2.  A Password Generator that will prompt the user for a username and randomly generate a STRONG
password. Then it will append the new username and password to the Input text file (Users-Pwds.txt).

## Write a short program that meets all of the following requirements.
1. Present the user with the Title of your program and three menu options (Then select either option 1, 2 or 3).
2. You are to create your own text descriptions for option 1, 2 and 3 to output to the user.
3. If they select Option 1:
4. Open an Input text file (Users-Pwds.txt) stored in the same directory as your Python file.
5. The file contains usernames and passwords (Comma separated and provided with the assignment).
6. BONUS: Use the input function and ask the user for the path to the input file.
7. If they enter "C:\folder\file.txt" you will need to convert to a valid format for python.
8. If they do not enter the correct file extention (.txt) then make the correction as well.
9. Process all the lines in the input file, checking each password string for its strength.
10. The password checking must be done in a function (Your choice of function name)
11. The function must have only one argument, a string that contains the password (not username).
12. It will then rank the strength of the password. POOR / MODERATE / STRONG (See on Page 2)
13. Then return a string with the rank.
14. The program will create an Output text File (Users-Pwds-Chked.txt).
15. The output text file will contain the username, password, and strength.
16. Again the file will be comma separated (chad.h,123abc,POOR) and one user per line.
17. The program will then tell the user the number of passwords checked from the file
and the feedback (output) can be found in the file (provide filename).
18. Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
19. If they select Option 2:
20. Prompt the user for a username (No more the 20 characters in length).
21. Create a Function that will have no (zero) arguments. (Your choice of function name)
22. The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
23. Ask the user if they would like this saved (Y or N).
24. If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
25. If N: Ask if they would like to generate a different password for this user (Y or N).
26. Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
27. If they select Option 3:
End the program and output to the screen: "This program is courtesy of: YourName "

## The following are the requirements for POOR / MODERATE / STRONG password.
Passwords can contain (not required) any of the following requirements:<br>
i. Lower case letters (a – z). &nbsp; iii) Numbers ( 0 – 9 ).<br>
ii. Upper case letters (A – Z). &nbsp; iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )
1. A POOR Password is defined as: <br>
a. Contains less than 3 from the above 4 items ( i – iv ).<br>
b. Less than 8 characters in length.
2. A MODERATE Password is defined as:<br>
a. Contains 3 from the above 4 items ( i – iv )<br>
b. Between 8 to 10 characters in length.
3. A STRONG Password is defined as:<br>
a. Meets all 4 of the above items ( i – iv )<br>
b. Greater than 10 characters in length.

# Solution
The solution to above problem will be provided in solutions.py after everyone submits their file.