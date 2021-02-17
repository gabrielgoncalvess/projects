# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:36:35 2021

@author: gabre
"""

from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    
def button_add():
    current = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(current)
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
        
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
        
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    current = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(current)
    e.delete(0, END)
    

def button_multiply():
    current = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(current)
    e.delete(0, END)
    

def button_divide():
    current = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(current)
    e.delete(0, END)
    

# ERROR: button click always "0"
'''
timer=0
r=1
c=0
for i in [7,8,9,4,5,6,1,2,3,0]:
    myButton = Button(root, text=str(i), padx=40, pady=20, command=lambda: button_click(i))
    myButton.grid(row=r, column=c)
    c+=1
    timer+=1
    if timer==3:
        timer=0
        c=0
        r+=1
'''


myButton1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
myButton2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
myButton3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
myButton4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
myButton5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
myButton6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
myButton7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
myButton8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
myButton9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
myButton0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))


button_plus = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)


myButton1.grid(row=3, column=0)
myButton2.grid(row=3, column=1)
myButton3.grid(row=3, column=2)
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButton7.grid(row=1, column=0)
myButton8.grid(row=1, column=1)
myButton9.grid(row=1, column=2)
myButton0.grid(row=4, column=0)



button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_multiply.grid(row=6, column=1)
button_subtract.grid(row=6, column=0)
button_divide.grid(row=6, column=2)



root.mainloop()
