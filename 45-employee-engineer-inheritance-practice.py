"""PRACTICE"""
"""Q. Define a Employee class with attributes role, department & salary. This class also a showDetails( ) method.
Create an Engineer class that inherits properties from Employee & has additional attributes : name & age."""

class Employee():
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self. salary = salary
    
    def showDetails(self):
        print("Role: ",self.role)
        print("Department: ",self.department)
        print("Salary: ",self.salary)
    
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Enginner","IT","75000")

eng1 = Engineer("Asif Ali",25)
eng1.showDetails()

