'''
Password Checker in python by Ashim Dahal.
Dec 04, 2022.
'''
import os
import random #randomly select characters for password
import string #to get alphabets, special characters and numbers to generate password
dirname = os.path.dirname(__file__)

def rank(pwd: str) -> str:
    '''
    Ranker function that ranks the password based on the assigned criteria
    Input: pwd -> character or string
    Returns: rank of password; POOR / MODERATE / STRONG
    '''

    def has_lowecase(pwd) -> bool:
        '''
        Helper Function: checks if the given password has at least one lowercase character
        Returns: True if condition is satisfied otherwise false
        '''
        return True if any(char.islower() for char in pwd) else False

    def has_uppercase(pwd) -> bool:
        '''
        Helper Function: checks if the given password has at least one uppercase character
        Returns: True if condition is satisfied otherwise false
        '''
        return True if any(char.isupper() for char in pwd) else False

    def has_chars(pwd) -> bool:
        '''
        Helper Function: checks if the given password has at least one special character
        Returns: True if condition is satisfied otherwise false
        '''
        symbols = '! + - = ? # % * @ & ^ $ _'.split(' ')
        return True if any(char in symbols for char in pwd) else False

    def has_nums(pwd) -> bool:
        '''
        Helper Function: checks if the given password has at least one number
        Returns: True if condition is satisfied otherwise false
        '''
        return True if any(char.isdigit() for char in pwd) else False

    # check for the given condition I, II, III and IV along with password GREATER THAN 10 characters condition
    if has_lowecase(pwd) and has_uppercase(pwd) and has_chars(pwd) and has_nums(pwd) and len(pwd) > 10:
        return 'STRONG'
    # Same as above but for moderate password
    if (has_chars(pwd) + has_lowecase(pwd) + has_nums(pwd) + has_uppercase(pwd)) >= 3 and len(pwd) >= 8:
        return "MODERATE"
    # If password is neither of above then it must be poor
    else:
        return "POOR"
    # Just in case the password is empty or any other error occurs
    return 'ERROR RATING PASSWORD'

def write_file(checked_file , line: tuple):
    '''
    Writes the given line(tuple containing username, password and strength of password or username, password) to the 
    given file and adds newline at the end
    '''
    try:
        checked_file.write(','.join(line))
        checked_file.write('\n')
    except IOError:
        print('IOError occured, restarting the program...')
        pass

def option1():
    '''
    Helper function that will be executed when user selects option 1.
    '''

    print('-'*80)
    print('Please select one of 2 options')
    print('option 1. rank passwords from Users-Pwds(200).txt \t option 2. rank passwords from Users-Pwds(10).txt \noption 3. Enter your own path')

    option = input('Enter your option: ')
    option = check_int_type(option)

    if option == 1:
        checked = open(os.path.join(dirname,'Users-Pwds-Chked.txt'),'w')
        # directly read and use split on the file so it doesn't need to be closed later on
        usrpwds = open(os.path.join(dirname,'Users-Pwds(200).txt'),'r').read().split()

        for userpwd in usrpwds:
            username, password = userpwd.split(',')
            strength = rank(password) # give rank to the current password

            line = (username,password,strength)
            write_file(checked, line) # use helper function to write the line in given file

        # close the file after the work is done
        checked.close()
        print('#'*80)
        print('[INFO] '+'Number of passwords checked:',str(len(usrpwds)))
        print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
        print('#'*80)


    elif option == 2:
        # same as option 1 but for a different file
        checked = open(os.path.join(dirname,'Users-Pwds-Chked.txt'),'w')
        usrpwds = open(os.path.join(dirname,'Users-Pwds(10).txt'),'r').read().split()
        for userpwd in usrpwds:
            username, password = userpwd.split(',')
            strength = rank(password)

            line = (username,password,strength)
            write_file(checked, line)
        
        checked.close()
        print('#'*80)
        print('[INFO] '+'Number of passwords checked:',str(len(usrpwds)))
        print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
        print('#'*80)

    elif option == 3:
        # Bonus question for custom file path
        path = input("Enter your absolute (not relative) filepath: ")
        if path[-3:].upper() == 'TXT':
            try:
                usrpwds = open(path,'r').read().split()
                checked = open(os.path.join(dirname,'Users-Pwds-Chked.txt'),'w')
                for userpwd in usrpwds:
                    username, password = userpwd.split(',')
                    strength = rank(password)

                    line = (username,password,strength)
                    write_file(checked, line)
                checked.close()
                print('#'*80)
                print('[INFO] '+'Number of passwords checked:',str(len(usrpwds)))
                print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
                print('#'*80)
            except FileNotFoundError:
                print('\n'+'*'*80)
                print("Sorry we couldnot find your file in the given path:")
                print(path + 'IS INVALID, restarting the program...')
                print('*'*80+ '\n')
        else:
            try:
                path = path+'.txt'
                usrpwds = open(path,'r').read().split()
                checked = open(os.path.join(dirname,'Users-Pwds-Chked.txt'),'w')
                for userpwd in usrpwds:
                    username, password = userpwd.split(',')
                    strength = rank(password)

                    line = (username,password,strength)
                    write_file(checked, line)
                checked.close()
                print('#'*80)
                print('[INFO] '+'Number of passwords checked:',str(len(usrpwds)))
                print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
                print('#'*80)
            except FileNotFoundError:
                print('\n'+'*'*80)
                print("Sorry we couldnot find your file in the given path:")
                print(path + 'IS INVALID, restarting the program...')
                print('*'*80+ '\n')

    else:
        print('Please choose between 1 and 3')

def option2():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    '''
    def gen_pass() -> str:
        '''
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        '''
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits
        pwd = ''
        while True:
            pwd+=random.choice(Ualphabets)
            pwd+=random.choice(Lalphabets)
            pwd+=random.choice(chars)
            pwd+=random.choice(digits)
            if rank(pwd) == "STRONG":
                break
        return pwd
    username = input("Enter your username: ")
    if len(username) > 20:
        print("username length is more than 20, please re enter it")
        option2()
    else:
        pass
    password = gen_pass()
    print('#'*80)
    print('[Username]: '+ username)
    print('[Password]: '+ password)
    print('#'*80)

    print('Do you want to save the password?')
    answer = input("please return Y to save and N to not save: ").upper()

    if answer == 'Y':
        print('Do you want to save the password in your custom file location?')
        ques = input("please return Y  or N: ").upper()
        if ques == "Y":
            path = input('Enter your absolute path here: ') 
            if path[-3:].upper() == 'TXT':
                try:
                    f = open(path,'a')
                    write_file(f, (username,password))
                    f.close()
                except Exception as e:
                    print('\n'+'*'*80)
                    print('Exception:' + str(e))
                    print("Invalid file path, please enter a valid file path")
                    print('*'*80+'\n')
            else:
                try:
                    path = path+'.txt'
                    f = open(path,'a')
                    write_file(f, (username,password))
                    f.close()
                except Exception as e:
                    print('\n'+'*'*80)
                    print('Exception:' + str(e))
                    print("Invalid file path, please enter a valid file path")
                    print('*'*80+'\n')

        else:
            # write to the file as suggested in the question prompt
            print('-'*10 + 'SAVING USERNAME AND PASSWORD in Users-Pwds.txt' + '-' * 10)
            f = open(os.path.join(dirname,'Users-Pwds.txt'),'a')
            write_file(f,(username,password))
            f.close()
            
    elif answer == 'N':
        print('-'*10 + 'Would you like to generate a new password?' + '-' * 10)
        answer = input("please return Y or N : ").upper()
        if answer == "Y":
            option2()
        else:
            print('-'*10 + 'Restarting the program...' + '-' * 10)

            pass 
    else: 
        print('Either choose Y or N, restarting the program...')


def check_int_type(inp):
    '''
    Helper function:
    Converts the given input to integer if possible if, else returns exception.
    Parameter: inp -> input
    Returns inp as int or exception
    '''
    try:
        inp = int(inp)
        return inp
    except Exception as exception:
        print('\n'+'*'*80)
        print('Exception:' + str(exception))
        print("Invalid option, please only enter the number of option and omit other details. Restarting the program....")
        print('*'*80+'\n')

def main():
    print('Welcome to my password ranking program')

    while True:
        print('-'*40)
        print('Please select one of 3 options')
        print('option1. Rank password of existing file \t option2. Generate a strong password \noption3. exit the program')
        inp = input("Enter your option here:")
        inp = check_int_type(inp)

        if inp == 1:
            option1()
        elif inp == 2:
            option2()
        elif inp ==3:
            print('-'*45)
            print('Closing the program \nThis program was built by: Ashim Dahal')
            break
        else:
            print("Please choose a number between 1 and 3.")

if __name__=='__main__':
    main()