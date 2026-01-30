"""PRACTICE"""
# WAP to find the sum of first n numbers. (using while)

num = int(input("Enter the number: "))

sum = 0

i = 0

while i<=num:
    sum += i
    i+=1
print(sum)


# WAP to find the factorial of first n numbers. (using for)

num = int(input("Enter the number: "))
fact = 1

for i in range(num,0,-1):
    fact *= i
print(fact)