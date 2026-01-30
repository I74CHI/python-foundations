"""LISTS"""
# A list is used to store multiple values in one variable.
# Lists are ordered, changeable(mutable), and allow duplicate values.
# Items in list is seperated by comma ","
# It can store elements of different types (integer, float, string, etc.)
# It is a built-in data type.
# We can use len() function to find the lenght of the list


"""Creating a List
1. Using Square Brackets"""
# We use square bracets [] to create a list directly.

a = [1,2,3,4,5,6] # List of integers
b = ['apple','banana','cherry'] # List of strings
c = [1,'hello',3.14,True] # List of mixed data types

print(a,"\n",b,"\n",c)


"""
2. Using list() Constructor"""
# We can create a list using the list() function with a tuple, string or another list.

a = list((1,2,3,'apple',4.5))
print(a)

b = list('GFG') #iterate
print(b)


"""
3. Creating List with Repeated Elements"""
# We can use the multiplecation operator * to create a list with repeated items.

a = [2]*4
b = [0]*8

print(a,'\n',b)


"""Accessing List Elements"""
# We use index number to get items from a list. In Python, counting starts from 0, so the first item is at index 0. We can also use negative numbers to get items from the end of the list. For example -1 gives the last item.

a = [10,20,30,40,50]
print(a[0]) # First element
print(a[-1]) # Last element
print(a[2]) # Third element


"""List Slicing"""

print(a[0:3])
print(a[:]) # all the elements


"""Adding Element into list"""
# 1. append() : Adds an element at the end of the list
# 2. extend() : Adds multiple elements to the end of the list
# 3. insert() : Adds an element at a specific position
# 4. clear() : removes all items

a = []

a.append(10)
print("After append(10): ",a)

a.insert(0,5) # First the position and second is the element
print("After insert(0,5): ",a)

a.extend([15,20,25,7])
print("After extend: ",a)

a. clear()
print("After clear: ",a)


"""Updating Elements into List"""
# Since lists are mutable, we cn update elements by accessing them via thir index.

a = [10,20,30,40,50]
print("List before update:",a)

a[1] = 15
print("List after update:",a) # item at position 2 is updated as 15


"""Removing Elements from list"""
# 1. remove() : Removes the first occurrence of an element
# 2. pop() : Removes the element at a specific index or the last element if no index is specified
# 3. del statement : Deletes an element at a specified index

a = [10,20,30,40,50]

a.remove(30)
print("After remove(30): ",a)

pop = a.pop()
print("Popped element: ",pop)
print("After pop(): ",a)

del a[0]
print("After del a[0]: ",a)


"""Nested Lists"""
# A nested list is a list within another lust, which is useful for representing matrices or table. We can access nested elements by chaining indexes

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[0][1])


"""List Comprehension"""
# List comprehension is a concise way to create lists using a single line of code. It is useful for applying an operation or filter to items in an iterable, such as a list or range

multiple = [2*x for x in range(1,11)]
print(multiple)

square = [x**2 for x in range(1,6)]
print(square)


"""List Methods"""

# 1. sort() : sorts in ascending order
# 2. sort(reverse=True) : sorts in descending order
# 3. reverse() : reverses list

# It also works for strings

l = [3,4,2,6]
print(l)
l.sort()
print("List after sorting",l)
l.sort(reverse=True)
print("List after sort(reverse=True)",l)
l.reverse()
print("List after reverse()",l)


"""map() Function"""
# The map() function applies a function to each element of a collection like a list, tuple, or set. It returns a map object, which is an iterator. The map() function is used to perform the same operation on all elements, making the code shorter, cleaner and more efficient.

s = ["1","2","3","4","5"]
res = map(int,s)
print(list(res))
# map() applies int() to each element in s which changes their datatype from string to int.


"""Syntax:
map(function,iterable)"""
# function : the function to apply to every element of the iterable
# iterable : One or more iterable objects(list, tuple,etc.) whose elements will be processed
