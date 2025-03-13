import time
import os
import webbrowser


def selectOperation():
    while True:
        print("""
        a.	Display current date and time
        b.	List the names of the files in the directory
        c.	Rename a file 
        d.	Delete a file
        e.	Display the content of a file
        f.	Enter a URL and display the webpage
        g.	Exit
        """)
        op=input("Enter an operation a-g: ")
        if op>="a" and op<="g":
            print("Valid Entry")
            return op
        else: 
            print("Invalid Entry")
    
op=""
while op!="g":
    op=selectOperation()
    if op=="a":
        print(time.ctime())
    elif op=="b":
        print(os.listdir())
    elif op=="c":
        f1=input("Enter the file to rename: ")
        f2=input("Enter the new name of the file: ")
        os.rename(f1,f2)
    elif op=="d":
        f1=input("Enter the file name to delete: ")
        os.remove(f1)
    elif op=="e":
        f1=input("Enter the file name to view: ")
        fp=open(f1)     
        d=fp.read()
        print(d)
        fp.close()
    elif op=="f":
        url="https://www.manhattan.edu"
        webbrowser.open(url)