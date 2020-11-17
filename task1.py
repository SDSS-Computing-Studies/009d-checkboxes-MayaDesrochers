#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""

#! python3

import tkinter as tk 
from tkinter import *
import math 

win=tk.Tk()
win.title("Binary / Decimal Converter!")
win.geometry("300x100")

cb1 = IntVar()                      
cb1.set(0)
cb2 = IntVar()
cb2.set(0)
cb3 = IntVar()
cb3.set(0)
cb4 = IntVar()
cb4.set(0)
cb5 = IntVar()
cb5.set(0)
cb6 = IntVar()
cb6.set(0)
cb7 = IntVar()
cb7.set(0)
cb8 = IntVar()
cb8.set(0)

def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    
    # binary: 128,64,32,16,8,4,2,1
    decimal=0
   
    if binary[0]==1:                
        decimal=decimal+128             
    if binary[1]==1:                
        decimal=decimal+64              
    if binary[2]==1:                
        decimal=decimal+32              
    if binary[3]==1:                
        decimal=decimal+16              
    if binary[4]==1:                
        decimal=decimal+8               
    if binary[5]==1:                
        decimal=decimal+4                
    if binary[6]==1:                
        decimal=decimal+2               
    if binary[7]==1:                
        decimal=decimal+1               
 
    return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    decimal=decimal
    value1=0
    value2=0
    value3=0
    value4=0
    value5=0
    value6=0
    value7=0
    value8=0

    if decimal>=128:
        value1=1
        decimal=decimal-128
        
    if decimal>=64:
        value2=1
        decimal=decimal-64
        
    if decimal>=32:
        value3=1
        decimal=decimal-32
       
    if decimal>=16:
        value4=1
        decimal=decimal-16
        
    if decimal>=8:
        value5=1
        decimal=decimal-8
        
    if decimal>=4:
        value6=1
        decimal=decimal-4
        
    if decimal>=2:
        value7=1
        decimal=decimal-2
        
    if decimal>=1:
        value8=1
        decimal=decimal-1
        

    binary=[value8,value7,value6,value5,value4,value3,value2,value1]
    return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    
    decimal=int(entry1.get())
    
    
    binary = decimal_to_binary(decimal)

    cb1.set(binary[0])
    cb2.set(binary[1])
    cb3.set(binary[2])
    cb4.set(binary[3])
    cb5.set(binary[4])
    cb6.set(binary[5])
    cb7.set(binary[6])
    cb8.set(binary[7])

def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    a=cb1.get()
    b=cb2.get()
    c=cb3.get()
    d=cb4.get()
    e=cb5.get()
    f=cb6.get()
    g=cb7.get()
    h=cb8.get()

    binary.append(h)
    binary.append(g)
    binary.append(f)
    binary.append(e)
    binary.append(d)
    binary.append(c)
    binary.append(b)
    binary.append(a)

    decimal = binary_to_decimal(binary)

    entry1.delete(0,END)
    entry1.insert(0,decimal)

label=Label(win, text="Binary / Decimal Converter!")
b1 = Button(win, text="Convert to Binary", command=get_binary)
b2 = Button(win, text="Convert to Decimal", command=get_decimal)
#reverse the order of the binary list
check1=Checkbutton(win,variable=cb8)
check2=Checkbutton(win,variable=cb7)
check3=Checkbutton(win,variable=cb6)
check4=Checkbutton(win,variable=cb5)
check5=Checkbutton(win,variable=cb4)
check6=Checkbutton(win,variable=cb3)
check7=Checkbutton(win,variable=cb2)
check8=Checkbutton(win,variable=cb1)
entry1=Entry(win)


#fix the location of these using place:
label
check1
check2
check3
check4
check5
check6
check7
check8
b1
b2
entry1

win.mainloop()
