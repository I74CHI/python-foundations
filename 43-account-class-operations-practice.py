"""PRACTICE"""
""" Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance. """

class Account():
    def __init__(self, bal, acc_no):
        self.bal = bal
        self.acc_no = acc_no

    def debit(self):
        deb = float(input("Enter the ammount:"))
        self.bal -= deb
        print(self.bal," balance of ", self.acc_no," after debit.")

    def credit(self):
        cred = float(input("Enter the ammount:"))
        self.bal += cred 
        print(self.bal," balance of ", self.acc_no," after credit.")

    def balance(self):
        print(f"Balance of {self.acc_no} is {self.bal}")

a1 = Account(10000,123456789)
a1.debit()
a1.credit()
a1.balance()