''' 
FUNCTIONS, TYPEHINTING AND HEADERS. 
Dashing December Python Bootcamp, Dec 12 class. 
'''


# In Python, a function is a block of code that performs a specific task. 
# Here's an example of a simple function in Python that takes in a number and prints out that number plus one:
# This is a function definition

def add_one(num):
  # This is a comment inside the function
  # The code below will add one to the input number
  result = num + 1
  
  # The next line will print the result
  print(result)

# This is the end of the function definition

# Now we can call the function and pass it an argument
add_one(5)  # This will print 6

# In the example above, we define the function using the def keyword, 
# followed by the function name (add_one) and the function's parameters (num) inside parentheses. 
# We then use a colon (:) to indicate the start of the function block.
# Inside the function, we have a comment that explains what the code does, followed by the code itself, which adds one to the input number and assigns the result to the result variable. 
# We then use the print() function to print out the result.
# To call the function, we simply use the function name followed by the arguments we want to pass to the function inside parentheses.
#  In this case, we call the add_one() function and pass it the number 5, which will cause the function to print out 6.











# This is a function named "greet" that takes in a parameter called "name"
def greet(name):
  # This line prints a greeting using the name parameter
  print("Hello, " + name + "!")
  
# Now we can call the function and pass it a name
# greet("Krishna")
# This will print "Hello, Krishna!"








# This is a function named "square" that takes in a parameter called "number"
def square(number):
  # This line calculates the square of the number parameter and stores it in a variable called "result"
  result = number * number
  
  # This line returns the value stored in the "result" variable
  return result
  
# Now we can call the function and pass it a number
x = square(5)
# This will call the function and pass 5 to the "number" parameter.
# The function will return the square of 5, which is 25.
# The returned value will be stored in the variable "x".

# We can then use the "x" variable to access the returned value
# print(x)
# This will print 25




# This is a function named "add" that takes in two parameters, "x" and "y"
def add(x, y):
  # This line calculates the sum of x and y
  result = x + y
  # This line returns the result of the calculation
  return result
  
# Now we can call the function and pass it values for x and y
result = add(2, 3)
# This will assign the value 5 to the "result" variable



# This is a function named "greet" that takes in a parameter called "name"
# The type hint for the "name" parameter is "str" (string)
def greet(name: str) -> str:
  # This line returns a greeting using the name parameter
  return "Hello, " + name + "!"

# Now we can call the function and pass it a name
greet("Ashim")
# This will return the string "Hello, Ashim!"



def add(a: int, b: int, c: int) -> int:
    """
    This function adds three numbers together and returns their sum.
    
    Args:
        a: The first number to add.
        b: The second number to add.
        c: The third number to add.
        
    Returns:
        The sum of the three numbers.
    """
    return a + b + c

# In this example, the typehint int specifies that the function expects 
# the inputs to be integers and the output to be an integer. 
# This can help other developers who use your function understand 
# how to use it, and it can also help some static analysis tools catch potential bugs in your code.

# The function also includes comments that provide additional information 
# about what the function does and how to use it. These comments are enclosed in 
# triple quotes (""") and can be placed either before or after the function's definition. 
# They can be very useful for explaining the purpose and behavior of your function to other developers who might use it.