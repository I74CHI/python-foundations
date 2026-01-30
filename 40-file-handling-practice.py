"""PRACTICE"""
"""Create a new file "practice.txt" using python. Add the following data in it: 
Hi everyone 
we are learning File I/O 
using Java. 
I like programming in Java."""

with open("practice.txt",'w+') as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
    f.seek(0)
    txt = f.read()
    print(txt)

"""WAF that replace all occurrences of "java" with "python" in above file."""

def replace():
    with open("practice.txt","r") as f:
        txt = f.read()
        
    new_txt = txt.replace("Java","Python")
    print(new_txt)

    with open("practice.txt","w") as f:
        wr = f.write(new_txt)
        print(wr)

"""Search if the word "learning" exists in the file or not."""

def search():
    with open("practice.txt",'r') as fi:
        txt = fi.read()
    if txt.find('learning') != -1:
        print("Learning exist")
    else:
        print("Learning does not exist")

replace()
search()

"""WAF to find in which line of the file does the word "learning" occur first"""

def line():
    with open("practice.txt",'r') as lf:
        x = True
        flag = 1
        while x == True:
            txt = lf.readline()
            if txt.find('learning') != -1:
                print(f"Learning exist in line {flag}")
                x = False
            flag += 1

line()

"""From a file containing numbers separated by comma, print the count of even numbers"""

def even():
    with open("numbers.txt",'r') as n:
        txt = n.read()
        new_txt = (txt.split(','))
        print(new_txt)
        cnt = 0
        for i in new_txt:
            digi = int(i)
            if digi%2 == 0:
                cnt += 1
        print(f"Number of even numbers are {cnt}")

even()