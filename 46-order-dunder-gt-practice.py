"""PRACTICE"""
"""Q. Create a class called Order which stores item & its price.
Use Dunder function __gt__() to convey that:
order1 > order2 if price of order1 > price of order2"""

class Order():
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price
    
o1 = Order("Chips", 20)
o2 = Order("Cake",200)

print(o2 > o1)