'''
Write a Python function called read_file() that takes a single parameter
filename, and opens the specified file in read-only mode. 
The function should read the entire contents of the file and return the contents as a string.
'''
import string, random
lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
extra = "!+-=?#%*@&^$_"
def password_generator():
    password = lower + upper + number + extra
    while True:
        password = ''.join(random.sample(password,random.randint(0,len(password))))
        if strength_checker(password) == "Strong password":
            return password
            

def strength_checker(password):
    l,u,e,n = False, False, False, False
    
    strength = 0
    for p in password:
        if p in lower and l == False:
            l = True
            strength+=1
        elif p in upper and u == False:
            u = True
            strength+=1
        elif p in number and n == False :
            n = True
            strength+=1
        elif p in extra and e == False:
            e = True
            strength+=1
    
    if strength == 4 and len(password) > 10:
        return "Strong password"

    elif strength == 3 and (len(password) >= 8 and len(password) <= 10):
        return "Moderate password"

    elif strength < 3 or (len(password) < 8):
        return "Weak password"
print("Welcome to password strength checker and creater program.")
option = input("Enter 1 for checking strength of password, 1 for generating password for username and 3 for exiting the program: ")
if option == "1":
    def read_file(filename):
        firstfile =  open('Users-Pwds(200).txt','r') 
        
        return firstfile
        # TODO: Open the file in read-only mode and read its contents. Return the contents of the file.
        
    contents = read_file("my_file.txt")

    #print(contents)  # Output: "Hello, world!\nI just did my first Assignment of week 2."
    def write_file(contents):
        with   open('Final-Users-Pwds(10).txt', 'a') as writefile:
            count = 0
            for content in contents:
                username, password = content.split(",")
                password = password.rstrip()
                strength = strength_checker(password)
                writefile.write(f"{username},{password},{strength}")
                writefile.write("\n")
                count+=1
        print(f"The number of passwords checked from the file is {count}")
    write_file(contents)

if option == "2":
    
    while True:
        username = input("Enter the username you want to. It can only be of length 20: ")
        if len(username) <= 20:
            break
    while True:
        password = password_generator()
        choice = input("Password has been generated. Do you like this information to be saved? ")
        if choice == "Y":
            with open("Users-Pwds.txt", "a") as file:
                file.write(f"{username},{password}")
                file.write("\n")
                break
        if choice == "N":
            choice = input("Would you like to generate a different password for this user?")
            if choice == "Y":
                pass
            if choice == "N":
                break
if option == "3":
    print("This program is courtesy of: Saurav")
    
