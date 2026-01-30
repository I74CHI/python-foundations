"""PRACTICE"""
"""Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"""

li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in li:
    print(i)

"""Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"""

# search = int(input("Enter the number: "))
# for i in range(len(li)):
#     if li[i]==search:
#         print('Position: ',i+1)
#         break

"""OR"""
tu = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
search = int(input("Enter the number: "))
idx = 1
for i in tu:
    if i==search:
        print('Position: ',idx)
        break
    idx += 1


"""Print numbers from 1 to 100."""

for i in range(1,101):
    print(i)

"""Print numbers from 100 to 1."""

for i in range(100,0,-1):
    print(i)

"""Print the multiplication table of a number n."""

table = int(input("Enter the number of which table you want: "))
till = int(input("Enter the number till which you want the table: "))

for i in range(1,till+1):
    print(f"{table} X {i} = {table*i}")