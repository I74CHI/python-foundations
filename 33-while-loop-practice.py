"""PRACTICE"""
# While loop
# Q. Print numbers from 1 to 100.

i = 1
while i<=100:
    print(i)
    i+=1

# Q. Print numbers from 100 to 1.

i = 100
while i>=1:
    print(i)
    i-=1

# Q. Print the multiplication table of a number n.

table = int(input("Enter the number of which table you want: "))
till = int(input("Enter the number till which you want the table: "))

i = 1
while i<= till:
    print(f"{table} X {i} = {table*i}")
    i+=1

# Q. Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in li:
    print(i)

# Q. Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

search = int(input("Enter the number: "))
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i=0
while i <= len(tup):
    if tup[i]==search:
        print('Position: ',i+1)
        break
    i+=1