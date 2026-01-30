"""FILE HANDLING"""
#   File handling means working with files in a program. It includes creating a file, opening it, reading data from it, writing data into it, and closing it. File handling helps a program store and retrieve data from the computer's storage in a safe and efficient way.
# There are two types of file 
# 1. Text File : .txt, .docx, .log etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc.


"""Need of File Handling"""
# To store data permanently, even after the program ends.
# To access external files like .txt, .csv, .json, etc.
# To precess large files efficiently without using much memory.
# To automate tasks like reading configs or saving outputs.


"""Opening a File"""
# To open a file, we can use open() function, which requires file-path and mode as arguments.
"""
Syntax:
file = open("filename.txt",'mode')"""
# filename.txt : name (or path) of the file to be opened.
# mode : mode in which you want to open the file (read, write, append, etc.).
"""If you don't specify the mode, it is in 'r' (read mode) by default"""

f = open("python.txt","r")
print(f)
# OUTPUT : <_io.TextIOWrapper name='python.txt' mode='r' encoding='UTF-8'>


"""Closing A File"""
file = open("python.txt","r")
file.close()


"""Checking File Properties"""

f = open("python.txt","r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is closed?",f.closed)
f.close()
print("Is closed?",f.closed)


"""Reading a File"""

f = open("python.txt","r")
content = f.read()
print("\n",content)
print(type(content))
f.close()

"""
f.readline() : reads one line at a time 
"""

f = open("python.txt","r")
line_1 = f.readline()
print("\n",line_1)
f.close()

"""
Once the all data is read the readline will not give any output but blank space as the cursor is at the end.
To read the file again we need to reopen the file.
"""


"""Using with Statement"""

with open("python.txt","r") as f:
    content = f.read()
    print(content)


"""Writing a File"""

with open("new.txt","w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with python.")
print("File written successfully")


# Append Mode
with open("new.txt","a") as file:
    file.write("\n My name is Aman Singh.")
print("File written successfully")


"""Handling Exceptions When Closing a File"""

try:
    file = open("new.txt","r")
    content = file.read()
    print(content)
finally:
    file.close()


"""Deleting a File"""

import os
os.remove("new.txt")
print("File Deleted")

file = open("new1.txt",'w')
file.close()
from pathlib import Path
Path("new1.txt").unlink()


"""seek() : move the cursor to specific position. 0 means at starting"""


"""Differnet File Modes"""

"""
Mode    Description

'r'	    Read-only. Raises I/O error if file doesn't exist.
'+'     open a disk file for updating (reading and writing)
'r+'	Read and write. Raises I/O error if the file does not exist.
'w'	    Write-only. Overwrites file if it exists, else creates a new one.
'w+'	Read and write. Overwrites file or creates new one.
'a'	    Append-only. Adds data to end. Creates file if it doesn't exist.
'a+'	Read and append. Pointer at end. Creates file if it doesn't exist.
'rb'	Read in binary mode. File must exist.
'rb+'	Read and write in binary mode. File must exist.
'wb'	Write in binary. Overwrites or creates new.
'wb+'	Read and write in binary. Overwrites or creates new.
'ab'	Append in binary. Creates file if not exist.
'ab+'	Read and append in binary. Creates file if it does not exist.
'x'     create a new file and open it for writing
't'     text mode (default)
'b'     binary mode
"""

"""
                  | r   r+   w   w+   a   a+
------------------|--------------------------
read              | +   +        +        +
write             |     +    +   +    +   +
write after seek  |     +    +   +
create            |          +   +    +   +
truncate          |          +   +
position at start | +   +    +   +
position at end   |                   +   +
"""
