"""PRACTICE"""
"""Write a recursive function to calculate the sum of first n natural numbers."""

number = int(input("Enter the number: "))

def nSum(number):
    if number == 0:
        return 0
    else:
        return number + nSum(number-1)

print(nSum(number))

"""Write a recursive function to print all elements in a list. Hint : use list & index as parameters."""

li = [3, 9, 1, 7, 4]
idx = len(li) - 1
def pEle(lst, idx):
    if idx == 0:
        return 0
    else:
        print(lst[idx])
    return pEle(lst,idx-1)
pEle(li,idx)