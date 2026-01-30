"""FUNCTIONS"""
# Functions are a block of statements that does a specific task. The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

"""Code Reuseability, Modularity (breaking big problem into small, manageable parts), Readability and Maintainability"""

"""
• () tells Python to execute the function

• Inside () we pass values (arguments) if needed

• Even if there are no arguments, () is still required
"""


"""Defining a Function"""
# Function can be defined using def keyword.
# A function might take input in the form of parameters.
"""Syntax:
def function_name(parameters):
    #statement
    return expression"""

def hello():
    print("Hello, Welcome to python")

hello() # Driver code to call a function
# A driver drives the program, tells Python what to run. Without it, function would just be defined, not executed


"""Function Arguments"""
# Arguments are the vales passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

def evenOdd(x):
    if(x%2) == 0:
        return "Even"
    else:
        return "Odd"
print(evenOdd(16))
print(evenOdd(1))


"""Types of function arguments"""
"""
1. Default Argument"""
#   A default argument is a parameter that assumes a default value if a value is not provided in the funtion call for that argument.
#   We give default values form last.

def myfn(x,y=50): # Here y=50 is the default argument, it will change once we provide the value of y.
    print("x=",x)
    print("y=",y)
myfn(10)


"""
2. Keyword Arguments"""
#   Here values are passed by explicitly specifying the parameter names, so the order doesn't matter.

def student(fname, lname):
    print(fname, lname)

student(fname='Aman', lname='Singh') # Aman to fname and Singh to lname (not by order)
student(lname='Singh', fname='Aman') # Aman to fname and Singh to lname (not by order)


"""
3. Positional Arguments"""
#   Here values are assigned to parameters based on their order in the function call.

def nameAge(name, age):
    print("Hi, I am",name)
    print("My age is",age)

print("Case-1:")
nameAge("Aman",27) # Here Aman will be assigned to name and 27 to age (by order)

print("Case-2:")
nameAge(27,"Aman") # Here Aman will be assigned to age and 27 to name (by order)


"""
4. Arbitrary Arguments"""
#   Arbitrary arguments are used when you don’t know in advance how many arguments will be passed to a function. It allow a function to take many values without defining them one by one.
"""
*args : lets a function accept any number of arguments, the arguments are received as a tuple
**kwargs : Used when you don’t know how many keyword arguments will be passed, the arguments are stored as a dictionary
"""

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(66,21,44,22))
print(add_numbers(64,61,24,100,112,321)) # No specific number of argument

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Alice", age=20, city="New York") # No specific number of keyword arguments


"""Function within Functions"""
#   A nested (inner) function is a function written inside another function. it can use the variable of outer function and is usually used to keep the code organized and safe by hiding internal logic.

def f1():
    s = "I am the best." # Step 2 : Text is assigned to s 
    def f2():
        print(s) # Step 4 : Text inside s is printed
    f2() # Step 3 : f2 function is called
f1() # Step 1 : calls f1 function


"""Anonymous Function / lambda function"""
#   An anonymous function is a function without a name. It is created using lambda keyword.
#   It is a small one-line funtion, it has no name, used for short, simple operations.
"""Syntax:
lambda argument : expression"""
#   It is used where a function is needed only once

add = lambda a,b : a+b
print(add(34,6))


"""Return Statement in Function"""
#   The return statement is used to send a value back from a function to the place where it was called.
#   It is used to get a result from a function, use that result later in the program, stop the function after returning a value

def add(a, b):
    return a + b

result = add(3, 4)
print(result)

def calc(a, b):
    return a + b, a - b # Returns a tuple

result = calc(5, 3)
print(result)


"""Pass by Value"""
# A copy of the value is passed to the function, chnages inside the function do not affect the original value, happens with immutable types (int, float, string, tuple)

def change(x):
    x=10
a = 5
change(a) 
print(a) # The original value does not change


"""Pass by Reference"""
# A reference (address) of the object is passed, changes inside the function affect the original object, happens with mutable types(list, dictonary, set).

def add_item(lst):
    lst.append(4)

number = [1,2,3]
add_item(number)
print(number)

"""Technically, Python uses "pass-by-object-reference". Mutable objects behave like pass by reference, while immutable objects behave like pass by value"""


"""Recursive Functions"""
# A recursive function is a function that calls itself to solve a problem. it often used for problems that can be borken into smaller parts, such as mathematical problems. A base case is always needed to stop the funtion; without it, the function will run forever. 

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))

"""
factorial(4) calls factorial(3)

factorial(3) calls factorial(2)

factorial(2) calls factorial(1)

When n == 1, the function stops (base case)

Values are returned back step by step
"""
