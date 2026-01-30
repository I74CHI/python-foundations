"""OOP(OBJECT ORIENTED PROGRAMMING)"""
"""
Procedural programming -> Functional Programming -> Object Oriented Programming"""
#   OOP is a way of writing code using classes and objects that represent real-world things. An object has attributes (data or properties) and methods (actions it can perform).
# Python supports the main principle of OOP, which help in creating programs that are well-structured, reusable, and easy to maintain.

class Car:
    color = "Blue"
    brand = "BMW"
car1 = Car()
print(car1.color)
print(car1.brand)

"""Class"""
#   A class is a blueprint used to create objects.
#   It defines the attributes (data) and methods (functions) of objects.
#   Classes are created using the class keyword in Python.
#   Attributes are veriable that belong to a class.
#   Class attributes are accessed using the dot (.) operator.
#   Example : Myclass.my_attribute

"""
Creating a Class"""
# Here, class keyword indicates that we are creating a class followed by name of the class (Dog in this case).

class Dog:
    species = 'Canine' # Class attribute

    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute
"""Object Attribute > Class attribute (Preference)"""

# class Dog : creates a class named Dog, which acts as a blueprint for dog objects.
# species is a class attribute, meaning it is shared by all instences of the class.
# __init__ is a constructor method that runs automatically when a new object is created. It is used to initialize object data.
"""Without __init__() method, you would need to set properties manually for each object."""
# self refers to the current object, allowing each object to store and access its own data.
"""Without self, Python would not know which object's properties you want to access.
It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class."""
# self.name and self.age are instence attribute, unique to each Dog object created from the class.

"""Objects"""
#   An object is an instance of class.
#   It represents a real and specific version of a class.
#   Each object has its own data.

# An object consist of:
#   State : represented by attributes; it shows the properties of the object.
#   Behavior : represented by methods; it shows what the object can do.
#   Identity : gives the object a unique identity, allowing it to be distinguished from other objects.

"""
Creating Object"""
# Creating an object in Python means making an instance of a class. This process is called object instantiation, where a new object is created from a class.

class Dog:
    species = 'Canine' # Class atrribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.species)

"""
dog1 = Dog("Buddy",3) : Creates an object of the Dog class with name as "Buddy" and age as 3. 
dog1.name : Accesses the instance atrribute name of the dog1 object.
dog1.species : Accesses the class attribute species of the dog1 object
"""
"""Methods"""
# Methods are functions written inside a class.
# They are used to define the behavior (actions) of an object.
# Methods define what an object can do.
"""
Real-life example

A car 🚗:

Data → color, speed

Methods → start(), stop(), accelerate()"""

"""
Types of methods"""
# 1. Instance Methods
#   Use self
#   Can access and modify object data
class Person:
    def show(self, name):
        print("Name:", name)

"""Decorator (@)"""
#   A decorator wraps a function and adds something before or after it runs.
"""
Real-life example
Think of a gift wrap 🎁:
Gift = original function
Wrap = decorator
Gift still the same, but looks better"""

# 2. Class Methods
#   Use @classmethod
#   Take cls as parameter
#   Work with class-level data
class Demo:
    @classmethod
    def info(cls):
        print("This is a class method")


# 3. Static Methods
#   Use @staticmethod
#   Do not use self or cls
#   Behave like normal functions inside a class
class Math:
    @staticmethod
    def add(a, b):
        return a + b

m = Math()
print(m.add(12,5))

# 4. @property
#   The @property decorator lets you access a method like an attribute
#   It helps you protect data and add logic when getting or setting values without changing how you use the object.
# It is used to :
#   control access to an attribute
#   add validation while setting values
#   keep code clean and readable
#   make method dynamic
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.chem + self.math + self.phy)/3) + "%"

    @property
    def percentage(self):
        return str((self.chem + self.math + self.phy)/3) + "%"

stu1 = Student(55,66,77)
print(stu1.percentage)
# If I change maths mark here
stu1.math = 100
# The percentage will not change as it is fixed by previous given data but the value of phy will get changed
print(stu1.math)
print(stu1.percentage)

# We can call percentage method to recalculate the percentage but there is an better option called property decorator

        




class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message,"! Welcome to our website.") 

p1 = Person("Aman")
p1.welcome()



"""Four Pillers of OOP"""
#   The four pillers of OOP help us write code that is organized, reuseable, and easy to maintain.

# Parent Class
class Animal:
    def speak(self):
        print("Animal makes a sound")
        """If child has speak() → use child version
            Else → use parent version"""
#Child class
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
class Cow(Animal):
    def speak(self):
        print("Cow moos")
class Tiger(Animal):
    pass

#Driver code
dog = Dog()
cat = Cat()
cow = Cow()
tiger = Tiger()
dog.speak()
cat.speak()
cow.speak()
tiger.speak()

"""
1. Inheritance (reuse code)"""
#   Inheritence allows one class to use the properties and methods of another class.
#   The class that inherits is called the child class.
#   The class being inherited from is called the parent class.
#   It helps in code reuse and avoids repetition.
# Example : A Dog class, A Cat class and A Cow class can inherit from a Animal class.

# Type: Single Inheritance, Multi-level Inheritence (car -> toyota -> fortuner -> car) and Multiple Inheritance (for multiple inheritance we give all parent parameter like class car(a,b))

class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
print(car1.name)
print(car1.color)
car1.start()
car1.stop()

"""
2. Polymorphism (same method, different behavior)"""
#   Polymorphism means "one name, many forms."
#   The same method or function name can behave differently for different objects.
#   It allows flexibility and make code more dynamic.
# Example : A method sound() behaves differently for Dog and Cat
# Example : + operator like add, concatinate, merge, etc.

"""Dunder Function"""
#   Dunder functions are special functions in Python whose names start and end with double underscores: __function__
"""
1. Object Creation & Initialization
Method	    Purpose
__new__	    Creates a new object
__init__	Initializes the object
__del__	    Destructor (called when object is deleted)

2. String Representation
Method	    Purpose
__str__	    Output for print()
__repr__	Official string representation
__format__	Custom formatting

3. Comparison Operators
Operator	Method
==	        __eq__
!=	        __ne__
<	        __lt__
<=	        __le__
>	        __gt__
>=	        __ge__

4. Arithmetic Operators
Operator	    Method
+	            __add__
-	            __sub__
*	            __mul__
/	            __truediv__
(//)	        __floordiv__
%	            __mod__
**	            __pow__

5. Reverse Arithmetic (when right operand controls)
Operator	Method
+	        __radd__
-	        __rsub__
*	        __rmul__

6. Assignment Operators
Operator	Method
+=	        __iadd__
-=	        __isub__
*=	        __imul__

8. Type Conversion
Function	Method
int()	    __int__
float()	    __float__
bool()	    __bool__
str()	    __str__

9. Container / Collection Methods
Operation	    Method
len()	        __len__
x in y	        __contains__
y[x]	        __getitem__
y[x]=v	        __setitem__
del y[x]	    __delitem__
iteration	    __iter__
next value	    __next__

10. Callable Objects
Purpose	                        Method
Call object like function	    __call__
"""

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNum(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(5,6)
num1.showNum()

num2 = Complex(2,3)
num2.showNum()

num3 = num1 + num2
num3.showNum()

"""
3. Encapsulation (data + methods together)"""
#   Encapsulation means grouping data and methods together in a single unit (class).
#   It protects data by controlling access to it.
#   A class is an example of encapsulation because it contains variable and methods together.
# Simple idea :Data + function inside one class.

"""
4. Data Abstraction (hide details, show functionality)"""
#   Abstraction means hiding internal details and showing only what is necessary
#   It focuses on what the object does, not how it does it.
#   It makes program simpler and easier to use.
# Example : Using a function without knowing its internal code. Like print function.

"""Private(like) attributes & methods"""
# Private attributes & methods are meant tobe used inly within the class and are not accessible from outside the class.
# In Python, there is no true private access like in some other languages. Instead, Python uses naming conventions to indicate that something should be treated as private.

"""
Single Underscore '_' (Protected by convention)"""
#   This is for internal use.
#   You should not access it directly, but Python allows it.

"""
Double Underscore '__' (Name Mangling - Private - like)"""
#   Python renames private variables internally.
#   This is called name mangling.

class demo:
    def __init__(self):
        self._x = 10    # protected (by convention)
        self.__y = 20   # private-like (name-mangling)

    def show(self):
        print(self._x)
        print(self.__y)

obj = demo()
obj.show()

print(obj._x)       # allowed, but not recommended
# print(obj.__y)    # error
print(obj._demo__y) # works, but bad practice

"""
Simple explanation:
    _x → should be used inside the class
    _y → Python hides it using name mangling
    __y becomes _Demo__y internally"""



"""super()"""
#   The super() funtion is used in a child class to call methods of its paraent class. It helps us reuse the parent's code while extending or modifying it in the child class.

# Use :
#   super() lets us call parent class methods without writing the parent class name.
#   This is helpful if the class hierachy changes, because the code still works.
#   It works with single, multiple, and multilevel inheritance.
#   It help reuse code, so we don;t repeat the same logic.
#   It avoids duplicate initialization, especially when multiple parent classes are involved.
#   Overall, super() makes code cleaner, safer, and easier to maintain.

class Car:
    def __init__(self, typ):
        self.typ = typ

    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self, name,typ):
        super().__init__(typ)
        self.name = name
        super().start()
        
car1 = ToyotaCar("Fortuner", "Petrol")
# print(car1.typ) # error
print(car1.typ)
car1.start


"""Changing Data at class level"""

class Person:
    name = "anonymous"

    # def changeName(self, name):
        # self.name = name
        # Person.name = name # Changes at class level
        # self.__class__.name = name # Changes at class level

    """OR"""
    @classmethod
    def changeName(cls,name): # Changes at class level
        cls.name = name

p1 = Person()
p1.changeName("Aman Singh")
print(p1.name)
print(Person.name)