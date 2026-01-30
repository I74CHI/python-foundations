"""PRACITICE"""
# WAP to check if a list contains a palindrome of elements.
# A palindrome is a word,number, or sentence that read the same forward and backword.

lis = [1,2,1,2,2]
print(lis)
r = lis.copy()
r.reverse()
print(r)

if r == lis :
    print("It contains palindrome.")
else :
    print("It does not contain palindrome.")