"""PRACTICE"""
""" Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average. """

class student():
    def __init__(self, name, hindi, english,maths):
        self.name = name
        self.hindi = hindi
        self.english = english
        self.maths = maths
    
    def avgMarks(self):
        total = self.english + self.hindi + self.maths
        print(f"Average Marks of {self.name} is {total/3}")

name = input("Enter your name :")
hindi_marks = int(input("Enter your hindi marks :"))
english_marks = int(input("Enter your english marks :"))
maths_marks = int(input("Enter your maths marks :"))

s1 = student(name,hindi_marks,english_marks,maths_marks)
s1.avgMarks()