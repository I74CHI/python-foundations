"""TUPLE"""
# A tuple in Python is a collection of items stored in a fixed order. It is similar to a list, but once a tuple is created, its values cannot be changed. A tuple can store different type of data, like numbers and strings. The main features of a tuple are that it is ordered, can store different data types, and is immutable(cannot be modified).
# The length of the tuple can be found by len() function.


"""Creating a Tuple"""
# A tuple is created by placing all the items inside a parentheses ()m seperated by commas. A Tuple can have any number of items and they can be of different data types.


"""
1. Using String"""

tup = ('Aman','Singh')
print(tup)


"""
2. Using List"""

li = [1,2,3,4,5]
print(tuple(li))


"""
3. Using Built-in Function"""

tup = tuple('Aman')
print(tup)


"""
5. Single element tuple"""

t = (55,) # Comma is required for the single element tuple
print(t) # Without comma python treats it as an integer


"""
6. Tuple with nested tuples"""

t1 = (0,1,2,3,4)
t2 = ('python','programming')
t3 = (t1,t2)
print(t3)


"""
7. Tuple with repetition"""

tu = ('Aman',)*4
print(tu) # Output : ('Aman', 'Aman', 'Aman', 'Aman')


"""Basic Operations"""


"""1. Accessing of Tuples"""
# We can get items from a tuple using index numbers, just like a list. The first item has index 0. We can also use negative numbers, where -1 gives the last item and moves backward.


"""
a. Accessing with indexing"""

tup = tuple('Aman')
print(tup[1])


"""
b. Accessing a range of element using slicing"""

print(tup[1:])
print(tup[3:4])


"""
c. Tuple unpacking"""

tup = ('Shashi','Kumar','Singh')
f,m,l = tup

print(f)
print(m)
print(l)


"""2. Concatenation"""
# Tuples can be joined using the + operator. This joins two or more tuples to make a new tuple. Only tuples can be joined with other tuples. If you try to join a tuple with list, it will throw an error.

tup1 = (0,1,2,3,4)
tup2 = ('Shashi','Singh')
tup3 = tup1+tup2
print(tup3) # Output : (0, 1, 2, 3, 4, 'Shashi', 'Singh')


"""3. Deleting a tuple"""

del tup3
# print(tup3)


"""4. index()"""
# returns index of the first occurrence

tup = (2,1,3,1,2)
print(tup.index(3))


"""5. count()"""
# counts total occurrences

print(tup.count(2))
