"""SETS"""
# A Set is used to store a collection of items with the following properties:
"""
1. It does not allow duplicate elements; repeated items appear only once.
2. A set is unordered, so elements have no fixed position. We cannot access elements using indexes like in lists.
3. Sets use hashing, which makes searching, inserting, and deleting very fast.
4. Sets are mutable, so we can add or remove elements. Individual elements in a set cannot be changed directly.
5. Each element in the set must be unique and immutable
6. It is created using {}.
"""

s1 = {10,20,21,60,'a'}
print(s1)
print(len(s1)) # does not consider duplicate values
print(type(s1))


coll = set() # This is how we create empty set
print(coll)


# Set creation using set() method
s2 = set([21,23,41,'a','b','c'])
print(s2)


"""Methods of Sets"""
# 1. add() : insert new elements into a set. (ignores duplicates)
# 2. union() : combines two sets and return a new set with all unique elements
# 3. intersection() : returns a new set containing elements that are common to both sets
# 4. difference() : returns a set containing elements that are in the first set but not in the second
# 5. clear() : removes all elements from a set, leaving it empty
# 6. remove() : removes the element
# 7. pop() : removes a random value


s2.add("d")
print(s1)

u = s1.union(s2)
print(u)

i = s1.intersection(s2)
print(i)

d = s1.difference(s2)
print(d)

s2.clear()
print(s2)

s1.remove('a')
print(s1)

s1.pop()
print(s1)


"""
    Operators	    Notes
1   key in s	    containment check
2   key not in s	non-containment check
3   s1 == s2	    s1 is equivalent to s2
4   s1 != s2	    s1 is not equivalent to s2
5   s1 <= s2	    s1 is subset of s2
6   s1 < s2	        s1 is proper subset of s2
7   s1 >= s2	    s1 is superset of s2
8   s1 > s2	        s1 is proper superset of s2
9   s1 | s2	        the union of s1 and s2
10  s1 & s2	        the intersection of s1 and s2
11  s1 - s2	        the set of elements in s1 but not s2
12  s1 ˆ s2	        the set of elements in precisely one of s1 or s2
"""
