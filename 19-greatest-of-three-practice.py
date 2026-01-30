"""PRACTICE"""
# WAP to find the greatest of 3 numbers entered by the user.

num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
num_3 = float(input("Enter the third number: "))

if (num_1>num_2 and num_1>num_3):
    print(num_1," is greatest")
elif (num_2>num_1 and num_2>num_3):
    print(num_2," is greatest")
else:
    print(num_3," is greatest")