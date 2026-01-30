"""PRACTICE"""
"""WAF to print the length of a list. ( list is the parameter)"""

def li_len(lst):
    print(len(lst))

li = [50,60,20,44,22,1,4]
li_len(li)

"""WAF to print the elements of a list in a single line. ( list is the parameter)"""

def eleprint(lst):
    
    for i in lst:
        print(i,end=" ")
    print("\n")
    
    
li = [3, 9, 1, 7, 4]
eleprint(li)

"""WAF to find the factorial of n. (n is the parameter)"""

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

"""WAF to convert USD to INR."""

def rupee(x):
    return x*(91.63)

usd = float(input("Enter the money: "))
print(f"{usd} USD will be {rupee(usd)} rupees.")