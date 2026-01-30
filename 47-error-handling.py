"""ERROR OR EXCEPTION HANDLING"""
#   Exception handling in Python helps a program deal with errors without stopping suddenly. When something goes wrong, like wrong input or a missing file, Python allows the program to catch the error, handle it properly and continue running instead of crashing.

# Example :

n = 10
try:
    res = n/0
except ZeroDivisionError:
    print("Can't be divided by zero!")

# Explanation : When a number is divided by 0, Python raises a ZeroDivisionError. The code that might cause this error is placed inside a try block, and the except block catches the error and prints message instead of stopping the program.

"""Difference b/w error and Exceptions"""
"""
Error (cannot be handled, program crashes)"""
#   Errors are serious problem in a program.
#   They usually happen due to wrong program structure or logic.
#   Errors cannot be handled using exception handling.
#   The program stops immediately
# Example : SyntaxError, MemoryError

"""
Exceptions (can be handled, program continues)"""
#   Exceptions are less serious problems.
#   They occur while the program is running.
#   Exceptions can be handled using try and except.
#   The program can continue execution.
# Example : ZeroDivisionError, FileNotFoundError, ValueError.

# Example :

# Syntax Error (Error)
# print("Hello world" # Missing closing parenthesis

# ZeroDivisionError (Exception)
# n = 10
# res = n/0
# print(res)

# Explaination : A syntax error prevents the program from running at all because the code is written incorrectly. An exception like ZeroDivisionError happens while the program is running and can be handled using exception handling.

"""Syntax and Usage"""
#   Python uses four main keyword for handling exception: try, except, else and finally. Each keyword has a different role in managing errors and keeping the program running safely.

"""
try:
    # Code
except SomeException:
    # Code
else:
    # Code
finally:
    # Code"""

# try : Runs the risky code that might cause an error
# except : Caatches and handles the error if one occurs
# else : Executes only if no exception occurs in try
# finally : Runs regardlessof what happens useful for cleanup tasks like closing files

# Example :

try:
    n = 0
    res = 100/n

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Enter a valid number!")

else:
    print("Result is", res)

finally:
    print("Execution Complete.")

# Explanation : The try block runs the code that may cause an error. The except block catches specific errors if they occur. The else block runs only when no error happens. The finally block always runs and makrs the end of execution.

"""Python Catching Exceptions"""
#   In Python, we can handle errors more effectively by catching specific types of exceptions. This makes the code safer, easier to understand, and simpler to debug.

"""
1. Catching Specific Exceptions"""
#   Catching specific exceptions allows the program to respond differently to different errors. It makes the code safer, easier to understand, and easier to debug. By handling only excepted errors, it also prevents hiding other bugs.

# Example : The below code handles ValueError and ZeroDivisionError with different messages.

try:
    x = int("str")
    inv = 1/x
except ValueError:
    print("Invaild!")
except ZeroDivisionError:
    print("Zero has no inverse!")

# Explanation : A ValueError occurs because "str" cannot be converted to an integer. If conversion had succeeded but x were 0, a ZeroDivisionError would have been  caught instead.

"""
2. Catching Multiple Exceptions"""
#   We can catch multiple exceptions in one block if they need the same handling, or use separate except blocks when different errors need different actions.

# Example : This code attempts to convert list elements and handles ValueError, TypeError and IndexError.

a = ["10", "Twenty", 30] # Mixed list of integers and strings
try:
    total = int(a[0] + int(a[1])) # 'Twenty' cannot be converted to int

except(ValueError, TypeError) as e:
    print("Error:",e)

except IndexError:
    print("Index out of range.")

# Explanation : The ValueError is raised when trying to convert "Twenty" to an integer. A TypeError could occur if incompatible type were used, while IndexError would trigger if the list index was out of range.

"""
3. Catch-All Handlers and Their Risks"""
#   Sometimes we use a catch-all exception handler to catch any error, but this can hide important debugging details, so it should be used carefully.

# Example : This code tries dividing a string by a number, which causes a TypeError.

try:
    res = "100"/20 # Risky operation: dividing string by number

except ArithmeticError:
    print("Arithmatic Problem.")
except:
    print("Something went wrong!")

# Explanation : A TypeError happens because a string cannot be divided by a number. A bare except block catches this error, but it hides the real error type, which makes debugging harder. A bare except should be used only as a last option when no specific exception is known.


"""Raise an Exception"""
#   In Python, we use the raise keyword to manually trigger an exception. We can raise a built-in exception or create our own custom exception by inheriting from Python's Exception class.

"""
Basic Syntax:
rasie ExceptionType(""Error Message)"""

# Example : This code raises a ValueError if an invaild age is given.

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)

# Explanation : The function checks if age is invaild. If it is, it raises a ValueError. This prevents invaild states from entering the program.

"""Custom Exceptions"""
#   We can create custom exceptions in Python by defining a new class that inherits from the built-in Exception class. This is useful when we want to handle specific errors related to our application.

# Example : This code defines a custom AgeError and uses it for validation.

class AgeError(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except AgeError as e:
    print(e)

# Explanation : Here, AgeError is a custom exception type. This makes error messages more meaningful in larger apllications.


"""Advantges"""

#   Improved reliability : Programs don't crash on unexpected input.
#   Seperation of concerns : Error-handling code stays separate from business logic
#   Cleaner code : Fewer conditional checks scattered in code.
#   Helpful debugging :  Tracebacks show exactly where the problem occured.

"""Disadvantages"""

#   Performance overhead : Handling exceptions is slower than simple condition checks 
#   Added complexity : Multiple exception types may complicate code
#   Security risk : Poorly handled exceptions might leak sensitive details