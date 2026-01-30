# OPERATORS
# An operator is a symbol that performs a certain operation between operands

# TYPES

# 1. Arithmetic Operator (+,-,*,/,%,**,//)
# Arithmetic operators are used with numeric values to perform common mathematical operations.

x = 15
y = 4

print("Arithmetic Operator")
print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor divion


# 2. Assignment Operators (=,+=,-=,*=,/=,%=,//=,**=,&=,|=,^=,>>=,<<=,:=)
# Assignment operators are used to assign values to variables.

# Example	    Same As	 
# x = 5 	    x = 5	
# x += 3	    x = x + 3	
# x -= 3	    x = x - 3	
# x *= 3	    x = x * 3	
# x /= 3	    x = x / 3	
# x %= 3	    x = x % 3	
# x //= 3	    x = x // 3	
# x **= 3	    x = x ** 3	
# x &= 3	    x = x & 3	
# x |= 3	    x = x | 3	
# x ^= 3	    x = x ^ 3	
# x >>= 3	    x = x >> 3	
# x <<= 3	    x = x << 3	
# print(x := 3)	x = 3 print(x)


# 3. Comparison Operators (==,!=,>,<,>=,<=)
# Comparison operators are used to compare two values.

x = 5
y = 3

print("Comparision Operator")
print(x == y) # Equal
print(x != y) # Not equal
print(x > y) # Greater than
print(x < y) # Less than
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to


# 4. Logical Operators (and,or,not)
# Logical operators are used to combine conditional statements.

x = 5

print("Logical Operators")
print(x > 0 and x < 10) # Returns True if both statements are true
print(x < 5 or x > 10) # Returns True if one of the statements is true
print(not(x > 3 and x < 10)) # Reverse the result, returns False if the result is true


# 5. Identity Operators (is,is not)
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

print("Identity Operators")
print("The is operator returns True if both variables point to the same object:")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal

print("The is not operator returns True if both variables do not point to the same object:")

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


# 6. Membership Operators (in,not in)
# Membership operators are used to test if a sequence is presented in an object

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits) # Returns True if a sequence with the specified value is present in the object
print("pineapple" not in fruits) # Returns True if a sequence with the specified value is not present in the object


# 7. Bitwise Operators (&,|,^,~,<<,>>)
# Bitwise operators are used to compare (binary) numbers

print("Bitwise Operators")
print(6 & 3) # Sets each bit to 1 if both bits are 1

"""The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the & operator compares the bits and returns 0010, which is 2 in decimal."""

print(6 | 3) # Sets each bit to 1 if one of two bits is 1

"""The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the | operator compares the bits and returns 0111, which is 7 in decimal."""

print(6 ^ 3) # Sets each bit to 1 if only one of two bits is 1

"""The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the ^ operator compares the bits and returns 0101, which is 5 in decimal."""

print(~2) # Inverts all the bits
print(6 << 2) # Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(6 >> 3) # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
