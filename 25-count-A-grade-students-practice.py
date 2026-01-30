"""PRACITICE"""
# WAP to count the number of students with the "A" grade in the following tuple.
# ["C","D","A","A","B","B","A"]
# Store the above values in a list & sort them from "A" to "D".

tup = ('C','D','A','A','B','B','A')
print("Number of students with A grade are",tup.count('A'))

lis = list(tup)
lis.sort()
print(lis)

