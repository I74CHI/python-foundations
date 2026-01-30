"""PRACTICE"""
"""WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value."""

sub_marks = dict()

sub1 = input("Enter the subject: ")
marks1 = float(input(f"Enter the marks of {sub1}: "))
sub_marks.update({sub1 : marks1})

sub2 = input("Enter the subject: ")
marks2 = float(input(f"Enter the marks of {sub2}: "))
sub_marks.update({sub2 : marks2})

sub3 = input("Enter the subject: ")
marks3 = float(input(f"Enter the marks of {sub3}: "))
sub_marks.update({sub3 : marks3})

print(sub_marks)