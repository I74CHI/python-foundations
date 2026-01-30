"""LOOPS"""
# Loops are used to repeat a block of code again and again.
# They are used to make programs easier and more efficient. They help us avoid writing the same code again and again by repeating it automatically. Loops are also very useful when working with collections like list, strings, and sets, because they allow us to process each item one by one. Overall, loops save time, reduce errors, and make programs shorter and clearer.


"""The range() function is used to generate a sequence of number.
SYNTAX:- range(start, stop, step)"""


"""Types"""


""" 1. For Loop """
#   For loops is used to iterate over a sequence such as a list, tuple, string or range. It allow to execute a block of code repeatedly, once for eacch item in the sequence.
# For loops are used for sequential traversal.


# iteration over number
n = 5
for i in range(0,n):
    print(i)


# iteration over list
li = ['Aman','Shashi','Alok']
for x in li:
    print(x)


# iteration over tuple
tu = ('Aman','Shashi','Alok')
for x in tu:
    print(x)


# iteration over string
s = 'Aman'
for x in s:
    print(x)


# iteration over dictonary
d = dict({'x':123,'y':321})
for x in d:
    print("%s %d"%(x, d[x]))


# iteration over sets
set1 = {10,21,31}
for x in set1:
    print(x)


# iterating by Index of Sequences
li = ['Aman','Shashi','Alok']
for index in range(len(li)): # The range(len(list)) generates indices from 0 to the length of the list minus 1
    print(li[index])


""" 2. While loop"""
# A while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the loop stops and the program continues with the next statement after the loop.

cnt = 0
while (cnt<3):
    print("Hello World")
    cnt += 1 


# Infinite while loop
#   An infinite while loop is used when we want a block of code to run forever. This happens when the condition os the while loop is always True. The loop will keep running until we stop it using the break statement or by applying some other stopping logic.

""" while(True):
    # print("Hello World") """


"""3. Nested loops"""
# Python Programming Language allows to use one loop inside another loop which is called nested loop.

for i in range(1,5):
    for j in range(i):
        print(i, end=' ')
    print()


# In this code, we use nested loops. The outer loop controls the rows, and the inner loop prints the value of i multiple time in each row. As the outer loop runs, the number of times i is printed increases. The print() function moves to a new line after eacch row is completed.


"""Loop Control Statements"""
# It changes the normal flow of the loop. They can stop the loop, skip an iteration, or do nothing temporarily. When a program exits a loop or block, any variable created inside that block are removed automatically.


"""1. Continue Statement"""
# It returns the control to the beginning of the loop.
# The continue statement is used to skip the current iteration of a loop and move to the next iteration. It is useful when we want to bypass certain conditions without terminating the loop.

for l in "AmanSingh":
    if l == 'S' or l == 'g':
        continue
    print('Current letter: ', l)


"""2. Break Statement"""
# The break statement brings control out of the loop.
# The break statement is used to stop a loop immediately when a certain condition is met.

for le in 'AmanSingh':
    if le == 'S':
        break
print("Current Letter: ",le) # It will give out as S


"""3. Pass Statement"""
# We use pass statement to write empty loops. Pass is also used for empty control statements, functions and classes.

for l in 'AmanSingh':
    pass
print('Last Letter: ',l)


# In this example, the loop goes thorugh each letter in 'AmanSingh' but does nothing inside the loop. After the loop ends, the variable holds the last letter, which is 'h', and that letter is printed.


"""Use of else in loops"""
# else can be used with loops(for and while). The else block runs only if the loop finishes normally(without break)


# without break
for i in range(5):
    print(i)
else:
    print("Loop finished")


# with break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished") # else block will not be executed


"""
• else runs after the loop completes
• else runs only if no break is used
• If break is used, else is skipped
"""
