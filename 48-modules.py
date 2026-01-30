"""MODULES"""
#   A module in python a file that contains code such as functions, classes, and variables. Modules help organize code into separate files, making programs easier to maintain, and reuse. Instead of writing all code in one file, related code can be placed in a module and imported whenever needed.

"""Create a Module"""
#   To create a Python module, write the desired code and save that in a file with .py extension.

# Example : Let's create a calc.py in which we define two functions, one add and another subtract.

# 49-calc.py

"""Import Module"""
#   We can use a module in another Python file usng the import statement. When Python encounters an import, it looks for the module in its search path and loads it if it is found.

# Example : Here, we are importing the calc that created earlier to perform add operation.

import calc
print(calc.add(10,2))
print(calc.subtract(11,1))

# Explanation : import calc loads the module and calc.add() accesses a function through dot notation.

"""Types of Import Statements"""
"""
1. Import From Module"""
#   This allows importing specific functions, classes, or variables rather than the whole module.

from math import sqrt, factorial
print(sqrt(16))
print(factorial(6))

# Explanation : Only sqrt and factorial are brought into the local namespace, so the prefix math. is not required.

"""
2. Import All Names"""
#   * imports everthing from a module into the current namespace.

from math import *
print(sqrt(16))
print(factorial(6))

# Explanation : Every public name of math becomes directly accessible. (Not recommended in large projects due to namespace conflicts.)

"""
3. Import With Alias"""
#   You can shorten a module's name using as.

import math as m
print(m.pi)

# Explanation : math is accessed through the shorter alias m.

"""Types of Modules"""
#   Python provides several kinds of modules. Each type plays a different role in applicaion development.

"""
1. Built-in Modules"""
#   These come bundled with python and require no installation.
# Example : math, random, os, etc.

import random
print(random.randint(1,5))

# Explanation : random.randint() returns a random number within the given range

"""
2. User-Defined Modules"""
#   These are modules you create yourself, such as calc.py

import calc
print(calc.subtract(5,3))

# Explanation: The module is created manually and then imported into another script.

"""
3. External (third-party) Modules"""
#   These modules are installed using pip
# Example : NumPy, Pandas, Requests

import requests
r = requests.get("https://www.google.com")
print(r.status_code)

# Explanation : requests is intalled separately (pip install requests) and provides HTTPS utilities.

"""
4. Package Modules"""
#   A package is a directory containing multiple modules, usually with __init__.py file.

# Example Directory
"""
    mypkg/
        __init__.py
        calc.py
        utils.py"""

# Using a module from a package

"""
from mypkg import utils
print(utils.some_func())
"""

# calls a function named some_func(), the output will be whatever that function returns.
# If utils.py contains something like:
"""
def some_func():
    return "Hello" """
# Output : Hello

"""Locating a Module"""
#   Python searches for modules in a predefined list of directories known as the module search path. You can view the list using sys.path.

import sys
for p in sys.path:
    print(p)

# Explanation : Python checks each path in order until it finds the module you're trying to import