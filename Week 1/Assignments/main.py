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