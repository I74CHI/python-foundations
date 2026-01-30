# INPUT
# input() function is used to accept values (using keyboard) from the user.
"""
The program pauses until the user provides some input.
You can optionally provide a prompt message (e.g., "Enter your age:").
Whether you type letters, numbers, or symbols, Python always stores it as a string by default.
If you need another data type (like integer or float), you must convert it manually using typecasting.
"""

name = (input("Enter your name : "))
print("Welcome,",name)

age = int(input("Enter your age: "))
print("Your age is :", age)
