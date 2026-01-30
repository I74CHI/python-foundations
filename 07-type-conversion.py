# TYPE CONVERSION
# Type conversion in Python is the process of changing a value from one data type to another.
"""
Helps ensure correct operations and calculations.
Examples include converting an integer to a float or a numeric string to an integer.
Python supports two types of type conversion: Implicit Conversion and Explicit Conversion.
"""

# 1. Implicit Type Conversion or Type Conversion
"""
Implicit conversion in Python happens automatically when different data types are used together in an expression.

Python converts a smaller data type to a larger one when needed.
Commonly occurs when integers and floats are combined.
Conversion happens at runtime to keep results accurate.
"""

x = 10          # Integer
y = 10.6        # Float
z = x + y     

print("x:", type(x))
print("y:", type(y))
print("z =", z)
print("z :", type(z))


# 2. Explicit Type Conversion or Type Casting
"""
Explicit conversion, also called type casting, is when a programmer manually changes a value from one data type to another.

Done using Python’s built-in functions like int(), float(), and str().
Gives full control over how data is interpreted or processed.
Used when automatic conversion is not suitable.

Common type casting functions:
1. int() converts a value to an integer
2. float() converts a value to a floating point number
3. str() converts a value to a string
4. bool() converts a value to a Boolean (True/False)
"""

s = "100"  # String
a = int(s)             
print(a)
print(type(a))
